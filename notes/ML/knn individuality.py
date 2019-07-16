from sklearn.preprocessing import MinMaxScaler

import pandas as pd

df = pd.read_csv("epithelial individuality.csv")


# 获取n0 n1 m0 m1数据
N = df[(df['n.stage']=="N0") | (df['n.stage']=="N1")]
M = df[(df['m.stage']=="M0") | (df['m.stage']=="M1")]
print(N.shape)
print(M.shape)

# 選擇數據集
n_test = N.iloc[:,:-8]
n_test.head()


X= n_test.values

# 特征缩放
scaler = MinMaxScaler()
x_scale = scaler.fit_transform(X)

y = N['names']
y = list(y.apply(lambda x: "_".join(x.split("_")[1:3])))

import numpy as np
from collections import Counter


class Individuality:
    def __init__(self, k):
        assert k>=1,"k must be valid"
        self.k = k
        self._x_train = None
        self._y_train = None
        
    def fit(self, x_train, y_train):
        self._x_train = x_train
        self._y_train = y_train


    # 1. 计算样本点的最近邻
    # 一个样本点有m个特征
    def neighbors(self, x):
        """
            x为样本点，X为测试集，所有点
        """
        # 周围点与选定的点之间的距离
        distance = [np.sqrt(np.sum(i-x)**2) for i in self._x_train]
        # 对距离进行排序, 返回索引
        nbs = np.argsort(distance)
        top_k = [self._y_train[i] for i in  nbs[:self.k]]
        
        # 计算k个点中，属于各样本的数量
        votes = Counter(top_k)


        # 2 . 计算i属于某个样本的先验概率（c样本数与总数的比） 
        # 统计样本c的细胞数量
        counter =  Counter(self._y_train)
        P = {}
     
        for c, count in counter.most_common():
            # 计算y中某个样本的频率（先验概率）
            p = count/len([yi for yi in y if yi==c])
            # 通过计算属于样本name的近邻点数量，来计算近邻点中属于该样本的概率，将概率乘以权重（权重为该样本的先验概率）
            neighbors_p = (votes.get(c,0)/100)*p
            P[c] = neighbors_p

        # 对概率进行排序，获取最大的概率值的样本名 和概率值（此时i分配到c样本）
        samplec = sorted(P.items(), key=lambda x:x[1], reverse=True)[0]
        
        return samplec[0], samplec[1]

    def predict(self, X_predict):
        """
            计算每个点所属的样本（类）
        """
        # y_pred = [neighbors(x) for x in X_predict]
        y_pred = []
        probabilities = []

        for x in X_predict:
            y, p = self.neighbors(x)
            y_pred.append(y)
            probabilities.append(p)
            
        return y_pred, probabilities
    

 # 对于每一个细胞进行计算之后，得到每个细胞所属样本及其概率值

model  = Individuality(100)
ind = model.fit(x_scale, y)
time y, p = model.predict(x_scale)


# 计算每个样本的概率均值
groups = n_test[['probability',"sample"]].groupby('sample').mean()
groups