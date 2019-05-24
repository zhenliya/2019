# 基本绘图
```python
import matplotlib.pyplot as plt
# 解决中文问题
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# 解决负号
plt.rcParams['axes.unicode_minus'] = False 

# 图像大小
plt.figure(figsize=(9.6, 7.2))
# 绘制散点图
plt.scatter(X, Y, color='red')
# 绘制折线图
plt.plot(X, Y, 'r', label="predict values")
plt.plot(X, Y_test, 'b',  linewidth=1.0, color='red',label="actual values")

# 去掉坐标轴
plt.axis(‘off‘)

# 去掉刻度
plt.xticks([])
plt.yticks([])

# 轴标签
plt.xlabel('number')
plt.ylabel('sales')
图例
plt.legend(labels=['predict values','actual values']，loc='best')
plt.savefig('./ols.png')
plt.show()


```

# 子图
```python
plt.figure(figsize=(9.6, 7.2))
# 指定子图的行， 列，位置
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

plt.suptitle('人口G多元回归')
plt.savefig('./pictures/ridge_mult_predict.png')
plt.show()

```
# 图例
```python
https://blog.csdn.net/qq_14959801/article/details/80901711
    #给类群点加文字说明
    txts = []
    for i in range(5):
        xtext, ytext = np.median(x[colors == i, :], axis=0)    #中心点
        txt = ax.text(xtext, ytext, str(i), fontsize=24)
        txt.set_path_effects([PathEffects.Stroke(linewidth=5, foreground="w"),PathEffects.Normal()])    #线条效果
        txts.append(txt)



```