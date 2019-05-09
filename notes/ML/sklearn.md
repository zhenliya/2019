# 简介
对常用的机器学习方法进行了封装，包括：回归(Regression)、降维(Dimensionality Reduction)、分类(Classfication)、聚类(Clustering)

# 安装
pip install -U scikit-learn

# 通用学习模式
1. 引入需要训练的数据
    sklearn自带数据集，自定义构造
2. 选择方法进行训练
    返回特征变量和目标值
3. 预测新数据
4. 可视化
5. 保存训练和的Model

# 模型
1. 监督学习
```python
sklearn.neighbors #近邻算法
sklearn.svm #支持向量机
sklearn.kernel_ridge #核-岭回归
sklearn.discriminant_analysis #判别分析
sklearn.linear_model #广义线性模型

sklearn.ensemble #集成学习
sklearn.tree #决策树
sklearn.naive_bayes #朴素贝叶斯
sklearn.cross_decomposition #交叉分解
sklearn.gaussian_process #高斯过程

sklearn.neural_network #神经网络
sklearn.calibration #概率校准
sklearn.isotonic #保守回归
sklearn.feature_selection #特征选择
sklearn.multiclass #多类多标签算法

```
2. 无监督学习
```python
sklearn.decomposition #矩阵因子分解
sklearn.cluster # 聚类
sklearn.manifold # 流形学习
sklearn.mixture # 高斯混合模型
sklearn.neural_network # 无监督神经网络
sklearn.covariance # 协方差估计
```
3. 数据变化
```python
sklearn.feature_extraction # 特征提取
sklearn.feature_selection # 特征选择
sklearn.preprocessing # 预处理
sklearn.random_projection # 随机投影
sklearn.kernel_approximation # 核逼近
```

# 常用命令
```python

# 作用：将数据集划分为 训练集和测试集
# 格式：train_test_split(*arrays, **options)
from sklearn.mode_selection import train_test_split
X, y = np.arange(10).reshape((5, 2)), range(5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
"""
参数
---
arrays：样本数组，包含特征向量和标签

test_size：
　　float-获得多大比重的测试样本 （默认：0.25）
　　int - 获得多少个测试样本

train_size: 同test_size

random_state:
　　int - 随机种子（种子固定，实验可复现）
　　
shuffle - 是否在分割之前对数据进行洗牌（默认True）

返回
---
分割后的列表，长度=2*len(arrays), 
　　(train-test split)
"""

```
# sklearn数据预处理

数据集的标准化对于大部分机器学习算法来说都是一种常规要求，如果单个特征没有或多或少地接近于标准正态分布，那么它可能并不能在项目中表现出很好的性能。

在实际情况中,我们经常忽略特征的分布形状，直接去均值来对某个特征进行中心化，再通过除以非常量特征(non-constant features)的标准差进行缩放。
1. 数据归一化
训练数据的标准化规则与测试数据的标准化规则同步
```python

data = [[0, 0], [0, 0], [1, 1], [1, 1]]
# 1. 基于mean和std的标准化
scaler = preprocessing.StandardScaler().fit(train_data)
scaler.transform(train_data)
scaler.transform(test_data)

# 2. 将每个特征值归一化到一个固定范围
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit(train_data)
scaler.transform(train_data)
scaler.transform(test_data)
#feature_range: 定义归一化范围，注用（）括起来
```
2. 正则化
计算两个样本的相似度时必不可少的一个操作，就是正则化。其思想是：首先求出样本的p-范数，然后该样本的所有元素都要除以该范数，这样最终使得每个样本的范数都为1
```python

X_normalized = preprocessing.normalize(X, norm='l2')
```
3. one-hot编码
one-hot编码是一种对离散特征值的编码方式，在LR(Logistic Regression)模型中常用到，用于给线性模型增加非线性能力。
```python


```


# 交叉验证
交叉验证的基本思想是将原始数据进行分组，一部分做为训练集来训练模型，另一部分做为测试集来评价模型。

交叉验证用于评估模型的预测性能，尤其是训练好的模型在新数据上的表现，可以在一定程度上减小过拟合。还可以从有限的数据中获取尽可能多的有效信息。

# 机器学习任务数据处理
将原始数据集分为三部分： 训练集、验证集和测试集

 训练集用于训练模型
 验证集用于模型的参数选择配置
 测试集对于模型来说是未知数据，用于评估模型的泛化能力。不同的划分会得到不同的最终模型。

# 过拟合（overfitting)问题

# 保存模型
```python
from sklearn import svm
from sklearn import datasets

#引入和训练数据
iris=datasets.load_iris()
X,y=iris.data,iris.target
clf=svm.SVC()
clf.fit(X,y)

#引入sklearn中自带的保存模块
from sklearn.externals import joblib
#保存model
joblib.dump(clf,'sklearn_save/clf.pkl')

#重新加载model，只有保存一次后才能加载model
clf3=joblib.load('sklearn_save/clf.pkl')
print(clf3.predict(X[0:1]))
#存放model能够更快的获得以前的结果

```
# LinearRegression
from  sklearn.linear_model import LinearRegression

`class sklearn.linear_model.LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)[source]`
参数：
- fit_intercept:boolean, optional, default True
	- 是否计算模型的截距，为False时，在运算中不会使用截距
- normalize : boolean,optinal, default False
	- 为True时，在回归之前，回归量X将通过减去平均值并除以L2-norm来进行正则化，可通过`sklearn.preprocessing.StandardScaler`进行在调用fit之前标准化估计量(regressors)，在这里设置normalize=False。 当fit_intercept 为False时，此参数被忽略。
- copy_X: boolean, optional, default True
	- True, X被复制， False, X被替换
- n_jobs: int or None, optional(default=None)
	-  用于计算的作业数（设置多线程或进程并行）。n_targets>1并且问题足够大才提供加速。None表示1，除了在`joblib.parallel_backend`上下文中，-1表示使用所有的处理器。并行运行某些估算器或函数的多个副本对性能非常不利。
	When n_jobs is not 1, the estimator being parallelized must be picklable. This means, for instance, that lambdas cannot be used as estimator parameters.
属性：
- coef_: array, shape(n_features,) or (n_targets, n_features)
	 - 线性回归问题的估计系数。 权重系数，可以传递多个目标fit(y 2D), 如果只有一维，1D array of length n_features
- intercept_: array 线性模型中的独立项
方法：
- fit(X, y[,sample_weight]) 训练线性模型 返回线性回归实例
	 - sample_weight  numpy array of shape [n_samples] 每个样本的单独权重，
- get_params([deep]) 获取此估量工具的参数 (LinearRegression的参数)
	`{'copy_X': True, 'fit_intercept': True, 'n_jobs': None, 'normalize': False}`
	- deep : boolean , optional如果为True，将返回此估计器的参数并包含作为估算器的子对象。
- predict(X) 使用线性模型预测
- score(X, y[,sample_weight]) 返回预测的确定系数R^2。
	- R用来反映回归模型说明因变量可靠程度的一个统计指标
	确定系数：在Y的总平方和中，由X引起的平方和所占的比例，记为R2(R的平方)
	确定系数的大小决定了相关的密切程度。
- `set_params(**params)` 设置此估量工具的参数(调用LinearRegression的参数)

## 使用
```python
# 切分训练集和测试集
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=None)
    # 训练模型
    regression_model = LinearRegression()     
    regression_model = regression_model.fit(X_train, Y_train)

    # 在测试集上预测结果
    y_pred = regression_model.predict(X_test)
    # 检验模型结果
    # 均方误差
    # r = metrics.mean_squared_error(y_pred, Y_test)
    # 计算均方误差
    # mse = np.average((y_pred - Y_test) ** 2)

    # R2值
    # r2 = metrics.r2_score(Y_test, y_pred)  # 前面是实际值，后面是预测值
    # print('r_x',r_x)

    # # 计算R2
    # def calculater2(y_pred, y_test):
    #     RSS = ((y_pred - y_test) ** 2).sum()
    #     TSS = ((y_test - np.average(y_test)) ** 2).sum()
    #     return 1-(RSS/TSS)
    #
    # cr2 = calculater2(y_pred, Y_test)
    print('ytest', Y_test)
    print('xtest', X_test)
    print('coef_', regression_model.coef_)
    print('intecept_', regression_model.intercept_)
    print('predict:', regression_model.predict(X_test))
    print('score:', regression_model.score(X_test, Y_test))
    print('score:', regression_model.score(X_train, Y_train))

    # 训练结果可视化
    plt.figure(figsize=(9.6, 7.2))
    plt.subplot(1, 2, 1)
    plt.title = '测试集'
    plt.plot(range(len(y_pred)), y_pred, 'b', label="预测")
    plt.plot(range(len(y_pred)), Y_test, 'r', label="测试验证")
    
    plt.xlabel('销量数量', fontproperties=self.font_set)
    plt.ylabel('销量(十亿元)', fontproperties=self.font_set)
    
    plt.subplot(1, 2, 2)
    plt.title = '训练集自测'
    plt.plot(range(len(y_pred2)), y_pred2, 'b', label="预测")
    plt.plot(range(len(y_pred2)), Y_train, 'r', label="测试验证")
    
    plt.suptitle('人口GDP人均可支配收入多元回归')
    plt.savefig('./pictures/ridge_mult_predict.png')
    plt.show()
```


# Ridge(岭回归)
sklearn.linear_model.Ridge
`class sklearn.linear_model.Ridge(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver=’auto’, random_state=None)`
参数：
- alpha : {float, array-like}, shape (n_targets)
	- 正则化程度，must be a positive float，正则化改善了问题的调节并减少了估计的方差。如果为数组，数量必须对应
- fit_intercept : boolean
	- 是否计算模型的截距，为False时，在运算中不会使用截距
- normalize : boolean, optional, default False 
	- 	- 为True时，在回归之前，回归量X将通过减去平均值并除以L2-norm来进行正则化，可通过`sklearn.preprocessing.StandardScaler`进行在调用fit之前标准化估计量(regressors)，在这里设置normalize=False。 当fit_intercept 为False时，此参数被忽略。
- copy_X : boolean, optional, default True
	- True, X被复制， False, X被替换
- max_iter : int, optional
	- 共轭梯度求解器（conjugate gradient solver）的最大迭代次数。 'sag'默认1000， sparse_cg 和lsqr由`scipy.sparse.linalg`决定。
- tol : float 解决方案的精确度
- solver : {‘auto’, ‘svd’, ‘cholesky’, ‘lsqr’, ‘sparse_cg’, ‘sag’, ‘saga’} 计算程序的解决方案
	- 'auto' 依据数据类型自动选择求解器
	- 'svd' 运用X奇异值分解（ Singular Value Decomposition ）来计算岭回归系数（Ridge coefficients），在奇异矩阵中比'cholesky'稳定
	- 'cholesky' 使用标准的`scipy.linalg.solve` 函数获得封闭(close-form)形式的解决方案
	- 'lsqr' 'lsqr'使用专用的正则化最小二乘例程`scipy.sparse.linalg.lsqr` 他是最快并且使用了迭代程序
	- 'sparse_cg' 使用`scipy.sparse.linalg.cg`中的共轭梯度求解器（ conjugate gradient solver）（可以设置max_iter 和tol) 作为迭代算法，对于大规模数据比'cholesky'更合适
	- 'sag' 使用迭代过程，使用随机平均梯度下降（Stochastic Average Gradient descent）当n_samples和n_features 数据量都很大时，比其他解决方案更快。
	- 'saga' sag的改进版，无偏版SAGA。“sag”和“saga”快速收敛仅在具有大致相同比例的要素上得到保证。可以使用sklearn.preprocessing中的缩放器预处理数据。

	- 以上解决器都支持稠密和稀疏数据。 当fit_intercept 为True时，只有sag 和saga支持稠密和稀疏数据
- random_state : int, RandomState instance or None, optional, default None
	- 伪随机数生成器的种子，用于在混洗数据时使用。 int 使用random number生成器， 如果为None RandoState实例，为np.random 。当slover == 'sag'时使用
Stochastic Average Gradient.随机平均梯度

属性：
- coef_ :array, shape (n_features,) or (n_targets, n_features) 权重向量
- intercept_ : float | array, shape = (n_targets,)
	- Independent term in decision function. Set to 0.0 if fit_intercept = False
- n_iter_ : array or None, shape (n_targets,)
	- 每个目标的实际迭代次数。 sag 和lsqr可以使用，其余解决器返回None

方法：
- fit(X, y[, sample_weight])
- get_params([deep])
- predict(X)
- score(X, y[, sample_weight]) 评价模型好坏的方法
- `set_params(**params)`

在sklearn中并没有提供直接的查看回归方程的函数，因此查看的时候需要自己转化一下。
sklearn就是把相关系数和残差分开保存了，因此，查看的时候要调用coef_和intercept_两个属性。

coef_：相关系数(array类型)
intercept_：截距，在fit_intercept=False的时候，将会返回

## 使用
```python
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import Ridge

    def ridge_model(self, size, state, alpha):
        X, Y = self.new_data()
        # 切分训练集和测试集
        size = size
        state = state
        alpha = alpha
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=size, random_state=state)
        # # 标准化处理
        ridge_model = Ridge(alpha=alpha,random_state=None)
        # 训练模型
        ridge_model = ridge_model.fit(X_train, Y_train)
        # 在测试集上预测结果
        y_pred = ridge_model.predict(X_test)
        y_pred2 = ridge_model.predict(X_train)
        # 检验模型结果
        # print('ytest', Y_test)
        # print('xtest', X_test)
        # print('coef_', ridge_model.coef_)
        # print('intecept_', ridge_model.intercept_)
        # print('predict:', ridge_model.predict(X_test))
        test_score = ridge_model.score(X_test, Y_test)
        train_score =  ridge_model.score(X_train, Y_train)

```
