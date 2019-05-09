TSNE即t-distributed Stochastic Neighbor Embedding.使用方法：

tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000); plot_only = 500 #只画前500个点
            #对中间层输出进行tsne降维
            low_dim_embs = tsne.fit_transform(flat_representation[:plot_only, :])
            #数据经过tsne以后是二维的  

            #画图传递数据二维的，和真实类别
sklearn.manifold.TSNE函数定义如下：
class sklearn.manifold.TSNE(n_components=2, perplexity=30.0, early_exaggeration=4.0, learning_rate=1000.0, n_iter=1000, n_iter_without_progress=30, min_grad_norm=1e-07, metric='euclidean', init='random', 


verbose=0, random_state=None, method='barnes_hut', angle=0.5)
参数：
n_components：int，可选（默认值：2）嵌入式空间的维度。
perplexity：浮点型，可选（默认：30）较大的数据集通常需要更大的perplexity。考虑选择一个介于5和50之间的值。由于t-SNE对这个参数非常不敏感，所以选择并不是非常重要。
early_exaggeration：float，可选（默认值：4.0）这个参数的选择不是非常重要。
learning_rate：float，可选（默认值：1000）学习率可以是一个关键参数。它应该在100到1000之间。如果在初始优化期间成本函数增加，则早期夸大因子或学习率可能太高。如果成本函数陷入局部最小的最小值，则学习速率有时会有所帮助。
n_iter：int，可选（默认值：1000）优化的最大迭代次数。至少应该200。
n_iter_without_progress：int，可选（默认值：30）在我们中止优化之前，没有进展的最大迭代次数。
0.17新版​​功能：参数n_iter_without_progress控制停止条件。
min_grad_norm：float，可选（默认值：1E-7）如果梯度范数低于此阈值，则优化将被中止。
metric：字符串或可迭代的，可选，计算特征数组中实例之间的距离时使用的度量。如果度量标准是字符串，则它必须是scipy.spatial.distance.pdist为其度量标准参数所允许的选项之一，或者是成对列出的度量标准.PAIRWISE_DISTANCE_FUNCTIONS。如果度量是“预先计算的”，则X被假定为距离矩阵。或者，如果度量标准是可调用函数，则会在每对实例（行）上调用它，并记录结果值。可调用应该从X中获取两个数组作为输入，并返回一个表示它们之间距离的值。默认值是“euclidean”，它被解释为欧氏距离的平方。
init：字符串，可选（默认值：“random”）嵌入的初始化。可能的选项是“随机”和“pca”。 PCA初始化不能用于预先计算的距离，并且通常比随机初始化更全局稳定。
random_state：int或RandomState实例或None（默认）
伪随机数发生器种子控制。如果没有，请使用numpy.random单例。请注意，不同的初始化可能会导致成本函数的不同局部最小值。
method：字符串（默认：'barnes_hut'）
默认情况下，梯度计算算法使用在O（NlogN）时间内运行的Barnes-Hut近似值。 method ='exact'将运行在O（N ^ 2）时间内较慢但精确的算法上。当最近邻的误差需要好于3％时，应该使用精确的算法。但是，确切的方法无法扩展到数百万个示例。0.17新版​​功能：通过Barnes-Hut近似优化方法。
angle：float（默认值：0.5）
仅当method ='barnes_hut'时才使用这是Barnes-Hut T-SNE的速度和准确性之间的折衷。 'angle'是从一个点测量的远端节点的角度大小（在[3]中称为theta）。如果此大小低于'角度'，则将其用作其中包含的所有点的汇总节点。该方法对0.2-0.8范围内该参数的变化不太敏感。小于0.2的角度会迅速增加计算时间和角度，因此0.8会快速增加误差。

#################################莫烦TSNE可视化############################################

"""

Know more, visit my Python tutorial page: https://morvanzhou.github.io/tutorials/
My Youtube Channel: https://www.youtube.com/user/MorvanZhou


Dependencies:
tensorflow: 1.1.0
matplotlib
numpy
"""
# encoder结果使用tsne对结果进行降维，显示
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt


tf.set_random_seed(1)
np.random.seed(1)


BATCH_SIZE = 50
LR = 0.001              # learning rate


mnist = input_data.read_data_sets('./mnist', one_hot=True)  # they has been normalized to range (0,1)
test_x = mnist.test.images[:2000]
test_y = mnist.test.labels[:2000]


# plot one example
print(mnist.train.images.shape)     # (55000, 28 * 28)
print(mnist.train.labels.shape)   # (55000, 10)
plt.imshow(mnist.train.images[0].reshape((28, 28)), cmap='gray')
plt.title('%i' % np.argmax(mnist.train.labels[0])); plt.show()


tf_x = tf.placeholder(tf.float32, [None, 28*28]) / 255.
image = tf.reshape(tf_x, [-1, 28, 28, 1])              # (batch, height, width, channel)
tf_y = tf.placeholder(tf.int32, [None, 10])            # input y


# CNN
conv1 = tf.layers.conv2d(   # shape (28, 28, 1)
    inputs=image,
    filters=16,
    kernel_size=5,
    strides=1,
    padding='same',
    activation=tf.nn.relu
)           # -> (28, 28, 16)
pool1 = tf.layers.max_pooling2d(
    conv1,
    pool_size=2,
    strides=2,
)           # -> (14, 14, 16)
conv2 = tf.layers.conv2d(pool1, 32, 5, 1, 'same', activation=tf.nn.relu)    # -> (14, 14, 32)
pool2 = tf.layers.max_pooling2d(conv2, 2, 2)    # -> (7, 7, 32)
flat = tf.reshape(pool2, [-1, 7*7*32])          # -> (7*7*32, )
output = tf.layers.dense(flat, 10)              # output layer


loss = tf.losses.softmax_cross_entropy(onehot_labels=tf_y, logits=output)           # compute cost
train_op = tf.train.AdamOptimizer(LR).minimize(loss)


accuracy = tf.metrics.accuracy(          # return (acc, update_op), and create 2 local variables
    labels=tf.argmax(tf_y, axis=1), predictions=tf.argmax(output, axis=1),)[1]


sess = tf.Session()
init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer()) # the local var is for accuracy_op
sess.run(init_op)     # initialize var in graph


# following function (plot_with_labels) is for visualization, can be ignored if not interested
from matplotlib import cm
try: from sklearn.manifold import TSNE; HAS_SK = True
except: HAS_SK = False; print('\nPlease install sklearn for layer visualization\n')
def plot_with_labels(lowDWeights, labels):
    plt.cla(); X, Y = lowDWeights[:, 0], lowDWeights[:, 1]
    for x, y, s in zip(X, Y, labels): #下边是画图和显示标签
        c = cm.rainbow(int(255 * s / 9)); plt.text(x, y, s, backgroundcolor=c, fontsize=9)
    plt.xlim(X.min(), X.max()); plt.ylim(Y.min(), Y.max()); plt.title('Visualize last layer'); plt.show(); plt.pause(0.01)


plt.ion()
for step in range(600):
    b_x, b_y = mnist.train.next_batch(BATCH_SIZE)
    _, loss_ = sess.run([train_op, loss], {tf_x: b_x, tf_y: b_y})
    if step % 50 == 0:
        accuracy_, flat_representation = sess.run([accuracy, flat], {tf_x: test_x, tf_y: test_y})
        print('Step:', step, '| train loss: %.4f' % loss_, '| test accuracy: %.2f' % accuracy_)


        if HAS_SK:
            # Visualization of trained flatten layer (T-SNE)
            tsne = TSNE(perplexity=30, n_components=2, init='pca', n_iter=5000); plot_only = 500 #只画前500个点
            #对中间层输出进行tsne降维
            low_dim_embs = tsne.fit_transform(flat_representation[:plot_only, :])
            #数据经过tsne以后是二维的  
            #画图传递数据二维的，和真实类别
            labels = np.argmax(test_y, axis=1)[:plot_only]; plot_with_labels(low_dim_embs, labels)
plt.ioff()


# print 10 predictions from test data
test_output = sess.run(output, {tf_x: test_x[:10]})
pred_y = np.argmax(test_output, 1)
print(pred_y, 'prediction number')
print(np.argmax(test_y[:10], 1), 'real number')



作者：curious_girl 
原文：https://blog.csdn.net/qq_23534759/article/details/80457557 
