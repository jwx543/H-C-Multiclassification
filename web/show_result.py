import json
from flask import Flask, request
import numpy as np
import torch
from torch.autograd import Variable

app = Flask(__name__)


@app.route('/', methods=['POST'])
def get_result():
    result = request.get_json()

    data = []
    datas = []
    for key in result:
        data.append(result.get(key))

    datas.append(data)
    data = np.array(datas)
    net = torch.load('../save/net.pkl')
    net.eval()
    outputs = net(Variable(torch.from_numpy(data).type(torch.FloatTensor)))
    pre = torch.max(outputs.data, 1)[1]

    scores = pre.data.item() + 1
    scores = str(scores)

    return scores


app.run()
