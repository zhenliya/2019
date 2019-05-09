import copy
import shelve
import time

import numpy
from matplotlib import pyplot
from sklearn import metrics, datasets, manifold




def cal_matrix_P(X, neighbors):
    """
        计算高维空间分布P
        neighbors 为邻近点个数
        pairwise_distances_chunked : performs the same calculation as this
            function, but returns a generator of chunks of the distance matrix, in
            order to limit memory usage.
        paired_distances : Computes the distances between corresponding
            elements of two arrays
    """
    entropy = numpy.log(neighbors)
    n1, n2 = X.shape
    # pairwise_distances(X)返回一个距离矩阵D,D_{i,j}表示X矩阵中第i各向量与第j各向量直接的距离
    # pairwise_distances(X,Y)D_{i,j}表示矩阵X第i各向量与矩阵Y第j各向量之间的距离
    D = numpy.square(metrics.pairwise_distances(X))
    # 对数据进行排序，选取排序前面k个点作为邻域点
    D_sort = numpy.argsort(D, axis=1)  # 按y方向排序，返回原数组下表
    P = numpy.zeros((n1, n1))
    for i in range(n1):
        Di = D[i, D_sort[i, 1:]]
        P[i, D_sort[i, 1:]] = cal_p(Di, entropy=entropy)
    P = (P + numpy.transpose(P)) / (2 * n1)
    P = numpy.maximum(P, 1e-100)
    return P


def cal_p(D, entropy, K=50):
    beta = 1.0
    H = cal_entropy(D, beta)
    error = H - entropy
    k = 0
    betamin = -numpy.inf
    betamax = numpy.inf
    while numpy.abs(error) > 1e-4 and k <= K:
        if error > 0:
            betamin = copy.deepcopy(beta)
            if betamax == numpy.inf:
                beta = beta * 2
            else:
                beta = (beta + betamax) / 2
        else:
            betamax = copy.deepcopy(beta)
            if betamin == -numpy.inf:
                beta = beta / 2
            else:
                beta = (beta + betamin) / 2
        H = cal_entropy(D, beta)
        error = H - entropy
        k += 1
    P = numpy.exp(-D * beta)
    P = P / numpy.sum(P)
    return P


def cal_entropy(D, beta):
    # P=numpy.exp(-(numpy.sqrt(D))*beta)
    P = numpy.exp(-D * beta)
    sumP = sum(P)
    sumP = numpy.maximum(sumP, 1e-200)
    H = numpy.log(sumP) + beta * numpy.sum(D * P) / sumP
    return H


# 计算低维空间分布Q
def cal_matrix_Q(Y):
    n1, n2 = Y.shape
    D = numpy.square(metrics.pairwise_distances(Y))
    # Q=1/(1+numpy.exp(D))
    # Q=1/(1+numpy.square(D))
    # Q=1/(1+2*D)
    # Q=1/(1+0.5*D)
    Q = (1 / (1 + D)) / (numpy.sum(1 / (1 + D)) - n1)
    Q = Q / (numpy.sum(Q) - numpy.sum(Q[range(n1), range(n1)]))
    Q[range(n1), range(n1)] = 0
    # Q[[i for i in range(len(n1))],range(n1)]=0
    Q = numpy.maximum(Q, 1e-100)
    return Q


# 计算梯度
def cal_gradients(P, Q, Y):
    n1, n2 = Y.shape
    DC = numpy.zeros((n1, n2))
    for i in range(n1):
        E = (1 + numpy.sum((Y[i, :] - Y) ** 2, axis=1)) ** (-1)
        F = Y[i, :] - Y
        G = (P[i, :] - Q[i, :])
        E = E.reshape((-1, 1))
        G = G.reshape((-1, 1))
        G = numpy.tile(G, (1, n2))
        E = numpy.tile(E, (1, n2))
        DC[i, :] = numpy.sum(4 * G * E * F, axis=0)
    return DC


# 计算损失函数Kl离散度

def cal_loss(P, Q):
    C = numpy.sum(P * numpy.log(P / Q))
    return C


"""
迭代采用的是探测步长的进退法，就是给定一个步长，
如果误差下降了，而且下降速度比上一步快了，
我就增加一点步长，如果下降了，但是没有比上一步快，我就继续保持这个，
如果误差上升了，我就减小步长，退回上一步。
"""


def tsne(X, n=2, neighbors=30, max_iter=200):
    tsne_dat = shelve.open('tsne.dat')
    data = []
    n1, n2 = X.shape
    P = cal_matrix_P(X, neighbors)
    Y = numpy.random.randn(n1, n) * 1e-4
    Q = cal_matrix_Q(Y)
    DY = cal_gradients(P, Q, Y)
    A = 200.0
    B = 0.1
    for i in range(max_iter):
        data.append(Y)
        if i == 0:
            Y = Y - A * DY
            Y1 = Y
            error1 = cal_loss(P, Q)
        elif i == 1:
            Y = Y - A * DY
            Y2 = Y
            error2 = cal_loss(P, Q)
        else:
            YY = Y - A * DY + B * (Y2 - Y1)
            QQ = cal_matrix_Q(YY)
            error = cal_loss(P, QQ)
            if error > error2:
                A = A * 0.7
                continue
            elif (error - error2) > (error2 - error1):
                A = A * 1.2
            Y = YY
            error1 = error2
            error2 = error
            Q = QQ
            DY = cal_gradients(P, Q, Y)
            Y1 = Y2
            Y2 = Y
        if cal_loss(P, Q) < 1e-3:
            return Y
        if numpy.fmod(i + 1, 10) == 0:
            print('{} iterations the error is {}, A is {}'.format(str(i + 1), str(round(cal_loss(P, Q), 2)),
                                                                  str(round(A, 3))))
    tsne_dat['data'] = data
    tsne_dat.close()
    return Y


def test_iris():
    data = datasets.load_iris()
    X = data.data
    target = data.target
    t1 = time.time()
    Y = tsne(X, n=2, max_iter=300, neighbors=20)
    t2 = time.time()
    print(f"Custom TSNE cost time: {str(round(t2-t1,2))}")
    figure1 = pyplot.figure()
    pyplot.subplot(1, 2, 1)
    pyplot.plot(Y[0:50, 0], Y[0:50, 1], 'ro', markersize=30)
    pyplot.plot(Y[50:100, 0], Y[50:100, 1], 'gx', markersize=30)
    pyplot.plot(Y[100:150, 0], Y[100:150, 1], 'b*', markersize=30)
    pyplot.title('CUSTOM')
    pyplot.subplot(1, 2, 2)
    t1 = time.time()
    Y1 = manifold.TSNE(2).fit_transform(data.data)
    t2 = time.time()
    print("Sklearn TSNE cost time: %s" % str(round(t2 - t1, 2)))
    pyplot.plot(Y1[0:50, 0], Y1[0:50, 1], 'ro', markersize=30)
    pyplot.plot(Y1[50:100, 0], Y1[50:100, 1], 'gx', markersize=30)
    pyplot.plot(Y1[100:150, 0], Y1[100:150, 1], 'b*', markersize=30)
    pyplot.title('SKLEARN')
    pyplot.show()


def test_digits():
    data = datasets.load_digits()
    X = data.data
    target = data.target
    t1 = time.time()
    Y = tsne(X, n=2, max_iter=100, neighbors=50)
    t2 = time.time()
    t = t2 - t1
    print("Custom TSNE cost time: %s" % str(round(t, 2)))
    figure1 = pyplot.figure()
    pyplot.subplot(1, 2, 1)
    for i in range(10):
        xxx1 = Y[target == i, 0]
        xxx2 = Y[target == i, 1]
        color = xxx2.ravel()
        pyplot.scatter(xxx1, xxx2, c=color[i])
    pyplot.xlim(numpy.min(Y) - 5, numpy.max(Y) + 5)
    pyplot.xlim(numpy.min(Y) - 5, numpy.max(Y) + 5)
    pyplot.title('CUSTOM: %ss' % str(round(t, 2)))
    pyplot.subplot(1, 2, 2)
    t1 = time.time()
    Y1 = manifold.TSNE(2).fit_transform(data.data)
    t2 = time.time()
    t = t2 - t1
    print("Sklearn TSNE cost time: %s" % str(round(t, 2)))
    for i in range(10):
        xxx1 = Y1[target == i, 0]
        xxx2 = Y1[target == i, 1]
        color = xxx1.ravel()
        pyplot.scatter(xxx1, xxx2, c=color[i])
    pyplot.xlim(numpy.min(Y1) - 5, numpy.max(Y1) + 5)
    pyplot.xlim(numpy.min(Y1) - 5, numpy.max(Y1) + 5)
    pyplot.title(f'SKLEARN: {str(round(t,2))}')
    pyplot.show()


# test_iris()
test_digits()