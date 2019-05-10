
import  pandas as pd


# pandas一些设置
## 打印所有输出值
 pd.set_option('display.max_rows', None)

## pandas读取文件
pd.read_csv(win_file,sep='\t', encoding='gbk',index_col=False, names=index_win )

# 新建DataFrame
## 创建一个空的 DataFrame
df_empty = pd.DataFrame(columns=['A', 'B', 'C', 'D'])

## 新建一个DateFrame
```python
ne = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'age':['15','20','s18','30','22'],
         'scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
```

# DataFrame操作
## 遍历dataframe 每一行
df.iterrows()    返回一个元组

# 索引和选择数据

- df.loc（） 基于标签  ，未匹配标签，返回KeyError
    可以使用单个标签，标签列表，切片对象，布尔数组进行选取，单个范围之间用"，"分割，第一个表示行，第二个表示列。
    df.loc[:,'a']
    df.loc[:,['a','b']]
    df.loc[['a','b','c'],['A','B']]
    df.loc['a']>0

- df.iloc() 基于整数
    使用整数索引，第一个位置为0，可以是整数值、整数列表、系列值
    df.iloc[4]
    df.iloc[:4]
    df.iloc[1:5,2:4]
    df.iloc[[1,3,5],[2,3,4]]

- df.ix() 基于标签和整数
	df.ix[:,'A']
	df.ix[:4]

## 选择满足某列的值为特定条件的行

df.loc[df['region']== '大连']

## 选择为空的所有行
```python
# 选择非空
df = df[(df[col].notnull) & (df[col] != "")]

```

## 填充空值
df.fillna()
删除含有空值的行
df.dropna()

df.fillna()

df.isnull()

df.isna()

## 使用多轴索引从Pandas对象获取值
Series : s.loc[indexer]    返回： 标量值
DataFrame: df.loc[row_index, col_index]    返回：标量对象
Panel: p.loc[item_index, major_index, minor_index]  

- .iloc与.ix应用相同的索引选项和返回值

df['a'] : 返回 属性为a的一列值 与索引， 可以使用.来选择列，df.a



## 设置索引
df.set_index    将dataFrame中某列作为索引
df.reset_index  使索引按0,1,2,3,4开始递增
df.reindex      设置新索引，不存在的index对应数据为'NaN'

### reindex
`DataFrame.reindex(labels=None, index=None, columns=None, axis=None, method=None, copy=True, level=None, fill_value=nan, limit=None, tolerance=None)`
- labels: 指定axis方向的新的索引，类似数组
- index, columns, 指定索引或者标题，需要使用键值对，防止重复最好传入对象

- axis 轴
- method 填充DataFrame中的空值，仅适用于单调的DataFrames / Series。
	- 默认填充空隙
	- pad/ffill ： 填充值为前一个有效值
	- backfill/bfill : 填充值为后一个有效值
	- nearest: 填充最近的有效值
- copy 布尔值，默认True 是否返回一个新的对象
- level： int or name 跨级别广播，匹配传递的MultiIndex级别的索引值
- fill_value: 默认np.NaN   标量 ，填充缺失值
- toleranc 新标签与原始标签最大允许距离

使用方式：
- （index = index_lavels, columns=culumn_labels, ...)
- (labels, axis={'index', 'columns'}, ...)

# 数据处理
## DataFrame 去重
df.drop_duplicates()

## DataFrame 级联 

1. `pd.concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False)`
- objs是Series，DataFrame或Panel对象的序列或映射
- axis - {0，1，...}，默认为0，这是连接的轴
- join - {'inner', 'outer'}，默认inner。如何处理其他轴上的索引。联合的外部和交叉的内部。
- ignore_index − 布尔值，默认为False。join_axes - 这是Index对象的列表。用于其他(n-1)轴的特定索引，而不是执行内部/外部集逻辑。
- join_axes - 这是Index对象的列表。用于其他(n-1)轴的特定索引，而不是执行内部/外部集逻辑。

2. pd.DataFrme.append(objs)  返回一个新的对象
- 沿axis=0连接
- 可以带多个对象 a.append([b,c,d])   a/b/c/d都为DataFrame或Series

3. join

## axis=0 与axis=1
https://blog.csdn.net/weixin_41576911/article/details/79339044
axis=0代表往跨行（down)，而axis=1代表跨列（across)  市动作，不是单单的行或者列

使用0值表示沿着每一列或行标签\索引值向下执行方法
使用1值表示沿着每一行或者列标签模向执行对应的方法

```python

import pandas as pd
df = pd.DataFrame([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
columns=["col1", "col2", "col3", "col4"])
df
```
	col1	col2	col3	col4
0	1	1	1	1
1	2	2	2	2
2	3	3	3	3

`df.mean(axis=1)`  按列方向求平均值，求每行的平均值
0    1.0
1    2.0
2    3.0
dtype: float64

`df.drop("col4", axis=1)`  删除列"col4"

## 在指定位置添加列
可以使用df.reindex , pd.concat

在后面直接添加一列： df['D'] = 33

1. 使用concat 添加多列，不能制定位置
pd.concat([df, pd.DataFrame(columns=list('DE'))])
- 默认是按0方向添加，即按行方向添加

2. 利用reindex来重排和增加列名 df.reindex(columns=list('ABCD'), fill_value=0)    fill_value 填充空值
可以改变列的相对位置，且保留原始位置的值，df.reindex(columns=list('DCBA'))

3. 使用list.insert方法   list.insert(index, obj)
- obj为要插入列表中的对象，现获取原列名集合，赋值给新变量，然后insert

```python
# 先获取列名
col_name = df.columns.tolist()

# 在索引为1前插入D列
col_name.insert(1, 'D')
# 在B列前插入D列
col_name.insert(col_name.index('B'), 'D')
# 在B列后插入D列
col_name.insert(col_name.index('B')+1, 'D')

# 执行插入操作
df.reindex(columns=col_name)


```

# 分组 groupby

`ataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, **kwargs)`

可以通过字典或者元素进行分组

axis 默认为0 沿x轴方向对数据表进行纵向切分

```python
# 按两列分组时， 是一个列表
dfg = df['sale_amount'].groupby([s_year, s_month])
df.groupby('group').apply(lambda x: x.resample('1D').ffill())
```

## 获取分组数据
df.get_group(key)
## Grouper
```python
df.groupby(['name', pd.Grouper(key='date', freq='A-DEC')])['ext price'].sum()

```

# 修改某一列数据
```python
s = ndf.loc[:,'temperature'].map(lambda x: x.replace('℃','').split('/')[0])

```
# 将数据转换为时间格式
```python
df["date"] = pd.to_datetime(df['date'])
# 按月统计
df.set_index('date').resample('M')['ext price'].sum()



```


# 插入新的列
```python

ol_name = ndf.columns.tolist()
col_name.insert(col_name.index('temperature'),'low_temp')
ndf = ndf.reindex(columns=col_name, fill_value= '0')

```

# pandas 读取txt文件
papa=pandas.read_csv('papa.txt',sep='\t')

# pandas DataFrame数据处理方法速度比较
at 比iloc性能好些
 选择单个元素用at
 df.at[i, 'A']

 apply性能更好

 # pandas排序
df.sort_values("station_id")