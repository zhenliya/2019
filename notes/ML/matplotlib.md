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
# 轴标签
plt.xlabel('number')
plt.ylabel('sales')
图例
plt.legend(labels=['predict values','actual values']，loc='best')
plt.savefig('./ols.png')
plt.show()


```
# 绘制岭迹图
