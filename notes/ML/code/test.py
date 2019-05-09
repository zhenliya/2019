# 区域与销量的关系
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

t1 = time.time

# 获取测试数据集
df = pd.read_csv('./data/sales_2018.csv', encoding='gb18030')
hd  = pd.read_csv('./data/holidays2018.csv', encoding='gbk')

#                    站点编号  2018/1/1  2018/1/2  2018/1/3  2018/1/4  2018/1/5  \
# 区域                                                                           
# 东洲区           2146429319    144126    173070    157542    190260    134110   
# 东港市           1958908184    253358    340768    296462    366482    293310   
# 中山区           1997821100    216300    419838    213892    384856    191222   
# 义县             906101623     78102    104908     73600    101188     79536   
# 于洪区           4917156422    437700    618884    472882    588348    449988  

gp = df.groupby('区域').sum()
# print(gp.head())
regions = list(gp.index)

# Series  > str
holiday = hd['date']

# 生成新的数据集 y 销量  x 区域
# 2018/1/1数据
sales = gp.iloc[0, 1:-1]


ndf = pd.DataFrame({
    'sales':first,
    'regions':regions   
})


t2 = time.time()



 # 用于训练的数据集为ndf
# 将类别数据数字化
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

Y = ndf['regions'].values
# print(Y)

labelencoder = LabelEncoder()
Y = labelencoder.fit_transform(Y)
onehotencoder = OneHotEncoder(categories='auto')
# Y = onehotencoder.fit_transform(Y.reshape(-1,1)).toarray()
# print(Y)


X = ndf['sales'].values



# 拆分数据集

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)
X_train, X_test=X_train.reshape(-1,1), X_test.reshape(-1,1 )
Y_train, Y_test=Y_train.reshape(-1,1), Y_test.reshape(-1,1 )

print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
# print(Y_train)
print(Y_test.shape)

# 选择简单线性回归模型

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

print(regressor)

Y_pred = regressor.predict(Y_test)

plt.scatter(X_train , Y_train, color = 'red')
plt.plot(X_train , regressor.predict(X_train), color ='blue')
plt.show()

# 测试集结果可视化
plt.scatter(X_test , Y_test, color = 'red')
plt.xlabel('sales')
plt.ylabel('regions')
plt.plot(X_test , regressor.predict(X_test), color ='blue')
plt.show()

        
t3 = time.time()  


print(t3-t2)
