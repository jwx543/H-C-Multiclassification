import torch
import torch.nn.functional as F
from torch.autograd import Variable
from sklearn import metrics


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_hidden1, n_output):
        super(Net, self).__init__()
        self.hidden1 = torch.nn.Linear(n_feature, n_hidden1)
        self.hidden2 = torch.nn.Linear(n_hidden1, n_hidden)
        self.hidden3 = torch.nn.Linear(n_hidden, n_hidden1)
        self.predict = torch.nn.Linear(n_hidden1, n_output)

    def forward(self, x):
        x = F.softmax(self.hidden1(x), dim=1)
        x = self.hidden2(x)
        x = self.hidden3(x)
        x = self.predict(x)
        return x


def train_data(train, test):
    net = Net(len(train[0][0]), 128, 32, 5)
    # 优化器与梯度裁剪
    param_optimizer = list(net.named_parameters())
    no_decay = ['bias', 'LayerNorm.bias', 'LayerNorm.weight']
    # 设置模型参数的权重衰减
    optimizer_grouped_parameters = [
        {'params': [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
        {'params': [p for n, p in param_optimizer if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}]
    optimizer = torch.optim.Adam(optimizer_grouped_parameters, lr=0.1)
    # optimizer = torch.optim.SGD(net.parameters(), lr=0.1)
    loss_func = torch.nn.CrossEntropyLoss()

    for t in range(5000):
        net.train()
        outputs = net(Variable(torch.from_numpy(train[0]).type(torch.FloatTensor)))
        loss = loss_func(outputs, Variable(torch.from_numpy(train[1]).type(torch.LongTensor)))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if t % 10 == 0:
            train_acc = metrics.accuracy_score(train[1], torch.max(outputs.data, 1)[1])
            dev_acc, dev_loss = evaluate(net, test)
            msg = 'Train Loss: {0:>5.2},  Train Acc: {1:>6.2%},  Val Loss: {2:>5.2},  Val Acc: {3:>6.2%}'
            print(msg.format(loss.item(), train_acc, dev_loss, dev_acc))
            net.train()


def evaluate(net, test):
    net.eval()
    loss_func = torch.nn.CrossEntropyLoss()
    outputs = net(Variable(torch.from_numpy(test[0]).type(torch.FloatTensor)))
    loss = loss_func(outputs, Variable(torch.from_numpy(test[1]).type(torch.LongTensor)))

    acc = metrics.accuracy_score(test[1], torch.max(outputs.data, 1)[1])
    return acc, loss.item()
