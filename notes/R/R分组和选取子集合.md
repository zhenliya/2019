# 1. cut() 将数值转换为Factor
将数值型（向量）按照区间进行分组
可以对日期进行分组
labels指定区间的类别。
cut(x, breaks, labels, include.lowset, right, dig.lab, ordered_result)
```R
#可以z按breaks分类的，各类别数量。
table(cut(Z, labels=c(1:12),breaks = -6:6)) 
# 将各个值用指定的labels代替
cut(Z, labels=c(1:12),breaks = -6:6)

# 对日期进行分组
vDate <- as.Date("2019-5-20","2019-5-31","2019-6-01","2019-6-22")
vDate.bymonth <- cut(vDate, breaks="month")

Dates <- data.frame(vDate, vDate.bymonth)
```

# dplyr  选择和筛选
合并
dplyr::left_join(a,b, by="x1")
dplyr::right_join(a,b, by="x1")
dplyr::inner_join(a,b, by="x1")
dplyr::full_join(a,b, by="x1")

筛选
dplyr::semi_join(a,b, by="x1") 所有行
dplyr::anti_join(a,b, by="x1")

操作
intersect(y,z)
union(y,z)
setdiff(y,z)

bind_rows(y,z)  将z按行添加到y中
bind_cols(y,z)

# aggregate()
`aggregate(sal~gen, data, mean)`
sal 和gen表示待分组的变量，
# tapply() 对不规则数组使用函数
将函数应用于不规则数组的每个单元格， 即对不同的组使用
tapply(X, INDEX, FUN = NULL, ..., default = NA, simplify = TRUE)
- x为使用split方法的对象
- INDEX 为一个factors的list ，该列表的元素通过as.factor强制转换为factors
- FUN 使用函数，按数名必须引号引起来。如果为NULL 返回一个向量，可以使用tapply提供的方法
- simplify 如果FALSE返回一个列表的数据。dim 属性有一个list 如果TRUE默认，返回标量
# by()
# table() 对数据进行分类汇总
# asplit() Split an array or matrix by its margins


asplit(x, MARGIN)
asplit(x, c(1, 2))  1部分行，两部分列，可用vector分
# split() 分多组并重新集合
split(x, f, drop = FALSE, ...)
split(x, f, drop = FALSE, sep = ".", lex.order = FALSE, ...)

split(x, f, drop = FALSE, ...) <- value
unsplit(value, f, drop = FALSE)

选择
# subset()
# which()
# sqldf()
# seq()
生成序列
seq.int 比较快
seq(...)
Default S3 method:
seq(from = 1, to = 1, by = ((to - from)/(length.out - 1)),
    length.out = NULL, along.with = NULL, ...)
seq.int(from, to, by, length.out, along.with, ...)
seq_along(along.with)
seq_len(length.out)

 seq(0, 1, length.out = 11)
 [1] 0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0

# %in%  选择值在多个类别的行
match(x, table, nomatch = NA_integer_, incomparables = NULL)
x %in% table
