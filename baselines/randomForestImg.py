import sklearn.datasets as datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA

# 导入数据，路径中要么用\\或/或者在路径前加r
dataset = pd.read_csv('petrol_consumption.csv')

# 输出数据预览
print(dataset.head())

# 准备训练数据
# 自变量：汽油税、人均收入、高速公路、人口所占比例
# 因变量：汽油消耗量
X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=0)
regr = RandomForestRegressor()
# regr = RandomForestRegressor(random_state=100,
#                              bootstrap=True,
#                              max_depth=2,
#                              max_features=2,
#                              min_samples_leaf=3,
#                              min_samples_split=5,
#                              n_estimators=3)
pipe = Pipeline([('scaler', StandardScaler()), ('reduce_dim', PCA()),
                 ('regressor', regr)])
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
export_graphviz(pipe.named_steps['regressor'].estimators_[0],
                out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('tree.png')
Image(graph.create_png())


