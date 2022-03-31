import sklearn.datasets as datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA

from run import data_load

data = data_load('../data/all.csv')
X = data[:, : -1]
y = data[:, -1]

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=0)

classifier = RandomForestClassifier()
pipe = Pipeline([('scaler', StandardScaler()), ('reduce_dim', PCA()),
                 ('classifier', classifier)])
pipe.fit(X_train, y_train)
ypipe = pipe.predict(X_test)

from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
import os

# 执行一次
os.environ['PATH'] = os.environ['PATH']+';'+r"D:\Graphviz\bin"
dot_data = StringIO()
export_graphviz(pipe.named_steps['classifier'].estimators_[0],
                out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')
Image(graph.create_png())


