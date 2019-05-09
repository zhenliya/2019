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

# 字符串find方法踩得坑
str.find() 返回索引，没找到返回-1  不是0