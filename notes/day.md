
# 奇异矩阵
该矩阵的秩不是满秩的， 对应行列式等于0的方阵
非奇异矩阵还可以表示为若干个初等矩阵的乘积，证明中往往会被用到
`如果A(n×n)为奇异矩阵（singular matrix）<=> A的秩Rank(A)<n.
如果A(n×n)为非奇异矩阵（nonsingular matrix）<=> A满秩，Rank(A)=n`

判断奇异矩阵：
1. 矩阵是否方阵
2. 看方阵的行列式|A|是否等于0，若等于0为奇异矩阵，若不等于0则为非奇异矩阵
由|A|!=0 可知矩阵A可逆，这样可以得出另外一个重要结论:可逆矩阵就是非奇异矩阵，非奇异矩阵也是可逆矩阵。

# dot 可视化
```python
from sklearn import tree
tree.export_graphviz(cl, out_file='sales.dot')
```
命令行 `dot -Tpng sales.dot -o sales.png`

# 读取excel文件
```python
import xlrd

excelFile = xlrd.open_workbook(r'aa.xlsx', sheetname=0)
names = excelFile.sheet_names()

```
# 平方、开方、乘方、平方根
mport numpy

numpy.square()
pow(x, x)
numpy.sqrt()
pow(x, 0.5)

import math
math.sqrt()

# 删除mysql数据
　如果要清空表中的所有记录，可以使用下面的两种方法：

　　DELETE FROM table1
　　TRUNCATE TABLE table1
如果要删除表中的部分记录，只能使用DELETE语句。

　　DELETE FROM table1 WHERE ...;
如果一个表中有自增字段，使用TRUNCATE TABLE和没有WHERE子句的DELETE删除所有记录后，如果用delete的时候想让起始值变为1 才要加上用针的where1或where true 如果不加,下次 添加还是从上次自增的位置开始的 

　　DELETE FROM table1 WHERE 1;

重设表的自增值：
ALTER TABLE test AUTO_INCREMENT=151

## mysql导入csv文件
MYSQL导出数据出现The MySQL server is running with the --secure-file-priv option

1.进入mysql查看secure_file_prive的值

$mysql -u root -p

mysql>SHOW VARIABLES LIKE "secure_file_priv";
secure_file_prive=null   -- 限制mysqld 不允许导入导出
secure_file_priv=/tmp/   -- 限制mysqld的导入导出只能发生在/tmp/目录下
secure_file_priv=""         -- 不对mysqld 的导入 导出做限制

2.更改secure_file_pri的值

/usr/local/mysql/support-files中的my-default.cnf配置文件，就把它复制到/private/etc中，重命名为“my.cnf”，并加入secure_file_priv=''，重启mysql服务器即可。


 基本语法：
load data [low_priority] [local] infile 'file_name txt' [replace | ignore]
into table tbl_name
[character set gbk]
[fields
[terminated by't']
[OPTIONALLY] enclosed by '']
[escaped by'\' ]]
[lines terminated by'n']
[ignore number lines]
[(col_name, )]

最后加上set update_time=current_timestamp；

```SQL

load data infile 'D:\jupyter_notes\\data_analysis\\data\\category everyday\\category_everyday_site_2017.csv'
replace into table b_category_everyday_2017
fields terminated by ','
optionally enclosed by '"'
lines terminated by 'n'
ignore 1 lines
set add_time=now();

```

导出：
select * from 表名
into outfile '导出路径\\test.csv' 
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\n';

# 定位到 MySQL 数据文件的存储位置方法
show global variables like "%datadir%";

# 查找含有sql的服务名，分为SERVICE_NAME服务名和DISPLAY_NAME显示名
sc query |findstr "SQL"

# 解决前后端分离跨域问题
pip install django-cors-headers
```python

一、DEBUG = False  修改
二、ALLOWED_HOSTS = ['*']  修改
三、MIDDLEWARE_CLASSES = ('corsheaders.middleware.CorsMiddleware',  # 放最前面 
 'django.middleware.common.CommonMiddleware', # 注意顺序    ...)
四、CORS_ORIGIN_ALLOW_ALL= True  添加
五、CORS_ALLOW_CREDENTIALS= True  添加
六、CORS_ALLOW_HEADERS = ('*')  添加
七、
INSTALLED_APPS = [
    ....
    'corsheaders', 添加这一行
    ...
]


```

# queryset 转为dataframe
```python
Method 1:
    queryset = models.xxx.objects.values("A","B","C","D")
    df = pd.DataFrame(list(queryset))  ## consumes much memory
    #df = pd.DataFrame.from_records(queryset) ## works but no much change on memory usage

Method 2:
    queryset = models.xxx.objects.values_list("A","B","C","D")
    df = pd.DataFrame(list(queryset), columns=["A","B","C","D"]) ## this will save 50% memory
    #df = pd.DataFrame.from_records(queryset, columns=["A","B","C","D"]) ##It does not work. Crashed with datatype is queryset not list.

```
```python
import pandas as pd
import datetime
from myapp.models import BlogPost

df = pd.DataFrame(list(BlogPost.objects.all().values()))
df = pd.DataFrame(list(BlogPost.objects.filter(date__gte=datetime.datetime(2012, 5, 1)).values()))

# limit which fields
df = pd.DataFrame(list(BlogPost.objects.all().values('author', 'date', 'slug')))

```

# numpy合并数组
Python中numpy数组的合并有很多方法，如

np.append() 
np.concatenate() 
np.stack() 
np.hstack() 
np.vstack() 
np.dstack() 
其中最泛用的是第一个和第二个。第一个可读性好，比较灵活，但是占内存大。第二个则没有内存占用大的问题


# ndarray转为list
d=np.array([1, 2, 3，4,5 ])
e=d.tolist()


# django显示本地图片链接 
1. 获取协议
`http = urlsplit(request.build_absolute_uri(None)).scheme`
2. 获取ip和端口号
`host = request.META['HTTP_HOST']`
3. 拼接本地路径
`url = http + '://' + host + '/media/images/11.png'.format(algorithm, crt)`
4. urls.py中配置
```python
from django.urls import re_path
from django.views.static import serve

re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),


```
MEDIA_ROOT 在setting的配置为：
```python
STATIC_URL = '/static/'
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
```
访问拼接好的路径就能够访问到对应的图片

# graphiv显示中文
1. 修改graphiv配置文件：
字体配置文件 fonts.conf 路径：`C:\Program Files (x86)\Graphviz2.38\fonts`

    将 `<dir>#FONTDIR#</dir>            <dir>~/.fonts</dir> `更改为
       ` <dir>C:/Windows/Fonts</dir>    <dir>~/.fonts</dir>`

2. 修改sklear中tree/export.py中的out_file.write(', fontname=KaiTi')

# django rest frame 将url相对路径改为绝对路径
## reverse 类似`django.urls.reverse`
通过request决定hot和port，返回合法的url
`reverse(viewname, *args, **kwargs)`
```python
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from django.utils.timezone import now

class APIRootView(APIView):
    def get(self, request):
        year = now().year
        data = {
            ...
            'year-summary-url': reverse('year-summary', args=[year], request=request)
        }
        return Response(data)

```
## reverse_lazy
`reverse(viewname, *args, **kwargs)`
需要将request作为参数
```python

api_root = reverse_lazy('api-root', request=request)
```

# numpy.dot()
返回矩阵的积
```python
In : a = np.arange(1,5).reshape(2,2)
Out:
array([[1, 2],
       [3, 4]])

In : b = np.arange(5,9).reshape(2,2)
Out: array([[5, 6],
            [7, 8]])

In : np.dot(a,b)
Out:
array([[19, 22],
       [43, 50]])

```

## numpy.argsort()
numpy.argsort(a, axis=-1, kind=’quicksort’, order=None) 
功能: 将矩阵a按照axis排序，并返回排序后的下标 
参数: a:输入矩阵， axis:需要排序的维度 
## numpy.exp()
返回e的幂次方，e是一个常数2.71828

# python的shelve模块
https://www.cnblogs.com/caibao666/p/6531044.html
shelve是一额简单的数据存储方案，他只有一个函数就是open()，这个函数接收一个参数就是文件名，并且文件名必须是.bat类型的。然后返回一个shelf对象，你可以用他来存储东西，就可以简单的把他当作一个字典，当你存储完毕的时候，就调用close函数来关闭。
key必须为字符串，而值可以是python所支持的数据类型
```python
import shelve

li = [1, 2, 3]

she = shelve.open('test.dat')
she['d'] = li
she['d'].append('f')
print(she['d'])
# 没有返回f 

she = shelve.open('test.dat')
she['d'] = li
temp = she['d']
temp.append('f')
she['d'] = temp
print(she['d'])
```

# python 读取json文件

load，读取的是整个文件，每个json之间用”,”分割开。此时文件开头”[” ，末尾加”]”
loads，写在for循环里面一行一行的读取。每个json之间没有”,”的时候使用

# ValueError:Trailing data
pandas.read_json('./weather.json',lines=True)
用pandas读取json文件时报错，原因是文件中的json格式如下是由无数个字典组成：
{"region": "清原 ", "day": "2019年03月02日", "weatherConditions": "晴/多云", "temperature": "12℃/-7℃", "windConditions": "西南风3-4级/西南风3-4级"}
{"region": "清原 ", "day": "2019年03月03日", "weatherConditions": "霾/多云", "temperature": "13℃/-5℃", "windConditions": "西南风1-2级/西南风1-2级"}

需要转换为格式：[{"region": "清原 ", "day": "2019年03月02日", "weatherConditions": "晴/多云", "temperature": "12℃/-7℃", "windConditions": "西南风3-4级/西南风3-4级"},
{"region": "清原 ", "day": "2019年03月03日", "weatherConditions": "霾/多云", "temperature": "13℃/-5℃", "windConditions": "西南风1-2级/西南风1-2级"}]

或者在后面加上 lines=True

# 解决pandas读取文件中文乱码问题

读取文件时加上encoding
df = pandas.read_json('./weather.json',lines=True,encoding='utf


# python写入csv文件增加空行解决办法

加上newline=''
writerows 写入的参数为包含字典或者列表的列表
```python 

        with open("holidays.csv", "a+",encoding='utf-8', newline='') as csvfile:

            writer = csv.writer(csvfile)  # 存入表时所使用的格式
            writer.writerow(['date', 'is_holiday'])
            writer.writerows(item)

```

# 遍历dateframe 每一行
df.iterrows()

# 创建一个空的 DataFrame
df_empty = pd.DataFrame(columns=['A', 'B', 'C', 'D'])

# 选择值为特定内容的所有行
df.loc[df['region']== '大连']