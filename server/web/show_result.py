import json
from flask import Flask, request
import numpy as np
import torch
from torch.autograd import Variable
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/', methods=['POST'])
# @cross_origin(supports_credentials=True)
def get_result():
    result = request.get_json()
    temp = dict()
    if type(result) == type(list()):
        for i in result:
            temp.update(i)
        result = temp

    data = []
    datas = []
    for item in result:
        data.append(int(result.get(item)))

    datas.append(data)
    data = np.array(datas)
    net = torch.load('../save/net.pkl')
    net.eval()
    outputs = net(Variable(torch.from_numpy(data).type(torch.FloatTensor)))
    pre = torch.max(outputs.data, 1)[1]

    scores = pre.data.item() + 1
    scores = str(scores)

    return scores


app.run(host="0.0.0.0")
