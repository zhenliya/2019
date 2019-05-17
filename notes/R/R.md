# R安装与环境搭建
R官网：https://www.r-project.org/

R&Bioconductor 说明文档：
http://manuals.bioinformatics.ucr.edu/home/R_BioCondManual

R下载路径：https://cran.r-project.org/mirrors.html
清华源：https://mirrors.tuna.tsinghua.edu.cn/CRAN/
R文档：https://mirrors.tuna.tsinghua.edu.cn/CRAN/

R-devel build 下载路径：https://mirrors.tuna.tsinghua.edu.cn/CRAN/bin/windows/base/rdevel.html
R包管理：https://blog.csdn.net/qq_32811489/article/details/81067877

一般，在开发测试阶段用debug版本，而上线发布用release版本。 使用Makefile定制编译不同版本，避免修改程序和Makefile文件，

## R的包
安装包列表：
https://cran.r-project.org/web/packages/

1. R安装包：
1）使用install.packages(“vcd”)命令下载包。选择china（Beijing）[https]
2）安装成功后使用 help(package = "vcd")查看vcd包的信息

2. 查看已加载的包：
(.packages())

3. 卸除已加载的包
detach(“package:RMySQL”)
注意是卸除，不是卸载，也就是说不是把包从R运行环境中彻底删除，只是不希望该包被加载使用。
在包使用函数冲突，检验函数依赖时比较有用。

4. 彻底删除已安装的包：
remove. packages(c(“pkg1”,”pkg2”) , lib = file .path(“path”, “to”, “library”))
注：“pkg1”,”pkg2”表示包名，即一次可以卸载多个包；
“path”, “to”, “library”表示R的库路径，字符向量，通常情况下只输一个路径即可。使用命令.libPaths()可以查看库路径。示例：
remove.packages(c(‘zoom’),lib=file.path(‘C:\\Program Files\\R\\R-3.2.2\\library’))

5. 查看已安装的包
installed.packages()[,c(‘Package’,’Version’,’LibPath’)]
其中c(‘Package’,’Version’,’LibPath’) 表示显示包名、版本、库路径信息，若无[,c(‘Package’,’Version’,’LibPath’)]参数，则显示所有信息。

6. 查看某个包提供的函数
help(package=’TSA’)

7. 查看某个函数属于哪个包
Help（函数名）

8. 查看安装包版本
 	browseVignettes("CATALYST")
	packageVersion("snow")

9. R语言修改下载安装包install.package的默认路径
https://blog.csdn.net/sinat_35187039/article/details/80239668

10. 更新R
运行 update.packages(checkBuilt=TRUE, ask=FALSE) 在新的R中，然后删除旧版本。不同版本可以同时存在。
11. 设置默认启动包
查看默认启动包
getOption("defaultPackages")
通过设置文件.Rprofile  初始化设置为环境变量R_DEFAULT_PACKAGES  设置R_DEFAULT_PACKAGES=NULL 保证只加载基本的包
Rscript 也能检查环境变量R_SCRIPT_DEFAULT_PACKAGES， 优先于R_DEFAULT_PACKAGES 
12. 管理包
R的包安装到libraries（路径）中，"D:\Program Files\R\R-3.6.0\library"  是".Library"的值
.libPaths() 可以用来添加已安装包的路径

## 离线安装R包以及依赖包
直接用Rgui > 程序包 > 本地安装
https://www.jianshu.com/p/24adf5914303
1）下载所有R包到本地
linux 终端（或windows cmd窗口）
$ cd /work/software/R/contrib
$ wget -c ftp://cran.r-project.org/pub/R/src/contrib/*.tar.gz

2）将所有下载的R包相关信息写到配置文件
R 终端
path <- c("/work/software/R/contrib")
write_PACKAGES(path,type="source")

3）写一个安装R包的脚本
install_Rpkg.R 脚本代码
```R
library(tools)

args=commandArgs(T)

if(length(args) == 0 ){

cat("Usage: Rscript install_Rpkg.R package1 package2 package3 ...")
cat("\n")
quit("no")

}

path <- c("/work/software/R/contrib")

install.packages(args, contriburl=paste("file:",path,sep=''),type="source")
```
4）安装R包

$ Rscript install_Rpkg.R ggplot2

## R自定义启动环境
https://www.cnblogs.com/cloudtj/articles/7119077.html
自定义启动详解1
打开R安装位置里的etc文件夹中的配置文件Rprofile.site文件：

这个文件里，设置的内容包括默认编辑器，CRAN镜像选取，自动加载包等等。如果你想要将常用的package和function在启动的时候让R自动加载，则可以将其写入到Rprofile.site文件的自定义函数里，重新启动R即可实现。
在Rprofile.site 文档的最后加上如下代码：
```R
# 方式1:
.First <- function(){
library(praise)
  cat(praise("${EXCLAMATION}! ${EXCLAMATION}! Handsome man,you have done this ${adverb_manner}!"),"\n",praise(),"\n",praise(),"\n",date(),"\n")
}

# 方式2:
.First <- function(){
  # 加载程序包跟平常一样用library或require
  library(data.table)
  library(RMySQL)
  library(dplyr)
  library(ggplot2)
  # 你可以将自定义函数的代码脚本保存到"D:/myfunctions.R"文件里
  # 如果有的话，加载函数用source函数
  # source("D:/myfunctions.R") 
  library(praise)
  # 启动提示语，可有可无
  cat(praise("${EXCLAMATION}! ${EXCLAMATION}! Handsome man,you have done this ${adverb_manner}!"),"\n",praise(),"\n",praise(),"\n",date(),"\n") 
}



```
c:\R\etc\Rprofile.site
```R
# Things you might want to change
# 下面是常规设置，包括，默认编辑器、制表符宽度等等
# options(papersize="a4")
# options(tab.width=2)
# options(editor="notepad")
# options(pager="internal")
# set the default help type
# options(help_type="text")
  options(help_type="html")

# 可以设置加载R包时，默认R包所在的目录
.libPaths(c("D:\\Program Files\\R\\R-3.2.4\\library","H:\\R\\Plus-Packages"))

# set a site library
# 自定义库路径，便于备份
# .Library.site <- file.path(chartr("\\", "/", R.home()), "site-library")
# set a CRAN mirror
# 设置CRAN镜像，选一个最近源，这样安装和更新包时就不用手动选取CRAN镜像了
 local({r <- getOption("repos")
       r["CRAN"] <- "
       options(repos=r)})

# Give a fortune cookie, but only to interactive sessions
# (This would need the fortunes package to be installed.)
#  if (interactive())
#    fortunes::fortune()
.First <- function(){
    # 设置R启动时加载的包
    library(TSA)
    library(MASS)
    # 启动时交互，可自定义
    cat("\nWelcome at",date(),"\n")
}

# 退出时交互
.Last <- function(){
    cat("\nGoodnye at",date(),"\n")
}





```
.First()函数中除了加载常用package之外，还可以加载保存自己编写的常用函数的源代码文件
.Last()函数可以执行推出时清理工作，如保存命令历史记录、保存数据输出和数据文件等等
如果需要长期使用某个包的话，每次开启都需要输入library()，比较麻烦，因此可以让R启动时自动加载某些包。在R的安装目录/etc/Rprofile.site加入下载语句：
```R
# 例如让R启动时自动加载ggplot2包

    local({old <- getOption("defaultPackages")
            options(defaultPackages = c(old, "ggplot2"))})

    # 在文章中引用R软件包，例如引用ggplot2包：

    citation(package="ggplot2")
    To cite ggplot2 in publications, please use:
    
      H. Wickham. ggplot2: elegant graphics for data analysis. Springer New
      York, 2009.
    
    A BibTeX entry for LaTeX users is
    
      @Book{,
        author = {Hadley Wickham},
        title = {ggplot2: elegant graphics for data analysis},
        publisher = {Springer New York},
        year = {2009},
        isbn = {978-0-387-98140-6},
        url = {http://had.co.nz/ggplot2/book},
      }


    # get noisy package imports to shut up
    #   we have to jump through hoops to get the
    #   call to "library()" to work because it
    #   will try to load a package even if it is not
    #   a string literal
    sshhh <- function(a.package){
      suppressWarnings(suppressPackageStartupMessages(
        library(a.package, character.only=TRUE)))
    }
    
    # list of packages to auto-load if interactive
    auto.loads <-c("dplyr", "ggplot2", "magrittr", "assertr", "reshape")
    
    # auto-load dplyr and ggplot2
    if(interactive()){
      invisible(sapply(auto.loads, sshhh))
    }


```


# R的函数
## 从网络下载文件 download.file()
download.file(url, destfile, method, quiet = FALSE, mode = "w",
              cacheOK = TRUE,
              extra = getOption("download.file.extra"),
              headers = NULL, ...)
被下载的文件url必须以http://, https://, ftp:// or file://.开头
- url   资源下载的链接a character string (or longer vector
- destfile  a character string (or vector, see url) with the name where the downloaded file is saved
- method  Method to be used for downloading files. Current download methods are "internal", "wininet" (Windows only) "libcurl", "wget" and "curl", and there is a value "auto": see ‘Details’ and ‘Note’
- quiet If TRUE, suppress status messages (if any), and the progress bar.
- mode character. The mode with which to write the file. Useful values are "w", "wb" (binary), "a" (append) and "ab". Not used for methods "wget" and "curl". See also ‘Details’, notably about using "wb" for Windows.
- cacheOK  logical. Is a server-side cached value acceptable?
- extra  character vector of additional command-line arguments for the "wget" and "curl" methods.
- headers  named character vector of HTTP headers to use in HTTP requests. It is ignored for non-HTTP URLs. The User-Agent header, coming from the HTTPUserAgent option (see options) is used as the first header, automatically.
例如：
```R
url <- "http://imlspenticton.uzh.ch/robinson_lab/cytofWorkflow"
fcs_zip <- "PBMC8_fcs_files.zip"
download.file(paste0(url, "/", fcs_zip), destfile = fcs_zip, mode = "wb")

```

## 读取FCS文件为flowSet
### flowFrame
flowFrame-class{flowCore}
'flowFrame'：用于存储来自FACS运行的细胞群的观察到的定量特性的类
此类表示FCS文件或类似数据结构中包含的数据。数据包含三个部分：
1. 原始测量值的数字矩阵，其中rows = events和columns = parameters
2. 参数的注释（例如，测量通道，污点，动态范围e.g., the measurement channels, stains, dynamic range）
3. 通过FCS文件中的关键字提供的附加注释

类flowFrame的对象可用于保存在流式细胞术中获得的细胞群的任意数据。
flowframe创建：
1. new("flowFrame",
exprs = ...., Object of class matrix
parameters = ...., Object of class AnnotatedDataFrame
description = ...., Object of class list
)
2. flowFrame(exprs, parameters, description=list())   后两个参数可选s

exprs: 包含测量强度（measured intensities）的类矩阵的对象。 行对应于单元，列对应于不同的测量通道（ measurement channels）。 矩阵的colnames属性应该包含通道的名称或标识符。 通常不会设置rownames属性。
parameters:AnnotatedDataFrame，包含有关flowFrame每列的信息。 这通常由read.FCS或类似函数使用来自描述参数的FCS关键字的数据填充。
description:包含FCS文件中的元数据的列表。

3. 直接从FCS文件创建flowFrame 使用通过read.FCS
该方式是建议和最安全的对象创建方式，因为read.FCS将在导入时执行基本数据质量检测。不建议使用new或构造函数创建对象。

检查流式细胞仪的有效性和读数据文件标准
isFCSfile(files)

read.FCS(filename, transformation="linearize", which.lines=NULL,
         alter.names=FALSE, column.pattern=NULL, invert.pattern = FALSE,
         decades=0, ncdf = FALSE, min.limit=NULL, 
         truncate_max_range = TRUE, dataset=NULL, emptyValue=TRUE, 
         channel_alias = NULL, ...)

- filename 文件名字符串
- transformation 定义转换类型的字符串.Valid values are linearize (default), linearize-with-PnG-scaling, or scale
  - linearize 变化，应用合适的幂（power）转换数据。
  - linearize-with-PnG-scaling 对存储在对数刻度上的参数应用适当的幂变换，并且还对基于存储在线性刻度上的参数的“增益”（FCS \ $ PnG关键字）进行线性缩放变换。
  - scale 比例转换将所有列缩放到$ [0,10 ^ decade] $。 在FCS4规范中默认为decade = 0
  - 也可以使用logical TRUE 等于linearize  FASLE（或NULL）对应于无变化，当FCS的header设为‘custom'或’applied'，对应也无变化。
- which.lines  数字向量，用于指定要读取的行的索引。 如果为NULL，则读取所有记录，如果长度为1，则读入由which.lines指示的大小的随机样本。
- alter.names  boolean指示我们是否应该使用make.names将列重命名为有效的R名称。 默认值为FALSE。
- column.pattern 默认NULL,可选的正则表达式
-invert.pattern  logical FALSE默认，如果TRUE, 如果为TRUE，则反转column.pattern中指定的正则表达式。 这对于指示我们不想读取的通道名称很有用。 如果column.pattern设置为NULL，则忽略此参数。
-decades 激活scaling时， 输出的decades
-ncdf  已过时
-min.limit  允许的数据范围中的最小值。 有些仪器会产生极端的人为值。 每个参数的正数据范围完全由仪器的测量范围定义，所有较大的值都设置为此阈值。 较低的数据边界定义不明确，因为补偿可能会使某些值低于仪器的原始测量范围。 这可以设置为任意数字或NULL（默认值），在这种情况下保留原始值。
-truncate_max_range 逻辑类型。 默认值为TRUE。 可以选择关闭以避免将极端正值截断到仪器测量范围。如'$ PnR'。
-dataset FCS文件规范允许在单个文件中包含多个数据段。 由于read.FCS的输出是单个flowFrame，因此我们无法自动读取所有可用集。 此参数允许选择其中一个子集进行导入。 它的值应该是可用数据集范围内的整数。 如果FCS文件中只有一个数据段，则忽略此参数。
-emptyValue boolean指示我们是否允许TEXT段中的关键字值为空值。 它会影响双分隔符的处理方式。 如果为TRUE，则双分隔符将被解析为一对空值的起始和结束单分隔符。 否则，将双分隔符解析为字符串的一部分作为关键字值。 默认为TRUE。
-channel_alias data.frame用于提供通道的别名，以标准化和解决FCS文件之间的差异。它应包含“别名”和“通道”列。 每个行/条目指定通道集合的公共别名（以逗号分隔）。 
-files

```R
## a sample file
fcsFile <- system.file("extdata", "0877408774.B08", package="flowCore")

## read file and linearize values
samp <-  read.FCS(fcsFile, transformation="linearize")
exprs(samp[1:3,]) #包含测量强度的类矩阵的对象。 行对应于单元，列对应于不同的测量通道。 矩阵的colnames属性应该包含通道的名称或标识符 。
"""
     FSC-H SSC-H      FL1-H    FL2-H     FL3-H FL1-A     FL4-H Time
[1,]   382    77 259.455272  1.00000  7.566695    55  13.09747    1
[2,]   628   280   9.057978 48.26071 10.273508     0  28.13318    1
[3,]  1023   735 537.611747 56.23413  6.915821   143 310.59002    1
"""
description(samp)[3:6] #包含FCS文件中的元数据的列表

"""
$`$DATATYPE`
[1] "F"

$`$NEXTDATA`
[1] "0"

$`$SYS`
[1] "Macintosh System Software 9.2.2"

$CREATOR
[1] "CELLQuest<aa> 3.3"
"""
class(samp)
"""
[1] "flowFrame"
attr(,"package")
[1] "flowCore
""""

## Only read in lines 2 to 5
subset <- read.FCS(fcsFile, which.lines=2:5, transformation="linearize")
exprs(subset)

## Read in a random sample of 100 lines
subset <- read.FCS(fcsFile, which.lines=100, transformation="linearize")
nrow(subset)  

#manually supply the alias vs channel options mapping as a data.frame
map <- data.frame(alias = c("A", "B")
                  , channels = c("FL2", "FL4")
)
fr <- read.FCS(fcsFile, channel_alias = map)
fr

```

### flowframe的方法：
1. 获取子集
flowFrame[i,j]   flowFrame[1:3] 获取1-3行
flowFrame[filter,]
flowframe[filterResult,]
- filter 对象，filter类是flowCore中所有过滤器/选通对象的虚拟基类
  - 方法 %in% 以通常的方式使用它返回一个值向量，用于标识过滤器接受哪些事件。 单个过滤器可以编码多个群体，因此这可以返回逻辑向量，因子向量或过滤器接受该事件的概率的数值向量。最低限度，您必须在创建新类型的过滤器时实现此方法.
  -&, |, ! 逻辑符合比较两个filters
  - %subset%, %&%  将过滤器定义为另一个过滤器的子集。  \&
  -%on%  与transformList结合使用以创建transformFilter。 此过滤器类似于子集过滤器，因为过滤操作发生在变换值而不是原始值上。
  - filter 这个方法是％in％的更正式版本，它返回一个filterResult对象，该对象可用于后续过滤操作，并提供有关过滤操作结果的更多元数据。 
  -summarizerFilter 实现新过滤器时，此方法用于更新filterResult的filterDetails槽。 它是可选的，通常只需要为数据驱动的过滤器实现。
- filterResult对象,对flowFrame对象使用filter返回的结果，保存的容器。
获取flowFrame子集时，drop被忽略。

2. $ 获取channel名称
frame$FSC.H 等价于 frame[,"FCS.H"]
如果列名不是合法R标记，应该用引号括起来 如 frame$"FSC-H"

3. exprs, exprs<-
提取或替换原始数据强度。 替换值必须是具有与参数定义匹配的名称的数字矩阵。 允许隐式子集（即，与原始flowFrame相比，替换值中的列数更少，但必须在那里定义）
使用：
exprs(flowFrame)
exprs(flowFrame) <- value

4. head, tail 显示原始数据矩阵的第一个/最后一个元素
head(flowFrame)
tail(flowFrame)

5. description, description<-
提取或替换整个注释关键字列表。 通常只会对关键字的子集感兴趣，在这种情况下，关键字方法更合适。 可选的hideInternal参数可用于排除以$开头的内部FCS参数。
description(flowFrame)
description(flowFrame) <- value

6. keyword, keyword<-
按关键字从描述槽中提取或替换一个或多个条目。 为字符向量（按名称选择关键字），函数（通过评估其内容上的函数选择关键字）和列表（上述组合）定义方法。
keyword(flowFrame)
keyword(flowFrame, character)
keyword(flowFrame, list)
keyword(flowFrame) <- list(value)

7. parameters, parameters<-

提取参数并返回AnnotatedDataFrame类的对象，或替换此类对象。 要访问实际参数注释，请使用pData（参数（帧））。 替换仅对包含所有varLabels名称，desc，range，minRange和maxRange的AnnotatedDataFrames以及name列中与exprs矩阵的colnames匹配的条目有效。 有关详细信息，请参阅参数
parameters(flowFrame)
parameters(flowFrame) <- value

8. show
显示有关flowFrame对象的详细信息。

9. summary
返回每个通道的描述性统计汇总（最小值，最大值，平均值和分位数）
summary(flowFrame)

10. plot
flowFrame对象的基本图。 如果对象只有一个参数，则会产生直方图。 对于两个参数，我们绘制了一个双变量密度图（参见smoothScatter，对于两个以上的参数，我们生成一个简单的splom图。要从flowFrame中选择特定参数进行绘图，可以将对象子集化，也可以将参数指定为字符向量。 绘图的第二个参数。平滑参数允许您在密度类型smoothScatter图和常规散点图之间切换。有关流式细胞仪数据的更复杂的绘图，请参阅flowViz包。
plot(flowFrame, ...)
plot(flowFrame, character, ...)
plot(flowFrame, smooth=FALSE, ...)

11. ncol, nrow, dim 提取数据矩阵的维度。
ncol(flowFrame)
nrow(flowFrame)
dim(flowFrame)

12. featureNames, colnames, colnames<-
 colnames和featureNames是同义词，它们提取参数名称（即数据矩阵的名称）。 对于colnames，还有一种替代方法。 这也将更新参数槽中的name列。

featureNames(flowFrame)
colnames(flowFrame)
colnames(flowFrame) <- value

13. names
提取参数的漂亮格式名称，包括参数描述
names(flowFrame)

14. identifier
提取flowFrame的GUID。 如果没有可用的GUID，则返回文件名。 请参阅标识符以获取详

15. range
取flowFame的仪器或实际数据范围。 请注意，仪器动态范围不一定与实际数据值的范围相同，而是测量仪器能够捕获的理论值范围。 使用flowFrames的变换方法时，将转换动态范围的值。
参数：
x: flowFrame object.
type: Range type. either "instrument" or "data". Default is "instrument"

range(x, type = "data")

16. each_row, each_col
在数据矩阵的行或列上应用函数。 这些是方便的方法。
each_row(flowFrame, function, ...)
each_col(flowFrame, function, ...)

17. transform
在flowFrame对象上应用转换函数。 这通过将flowFrame视为常规data.frame来使用R的转换函数。 flowCore为转换提供了一个额外的内联机制（参见％on％），它严格限制在此处描述的外部转换。

transform(flowFrame, translist, ...)

18. filter
在flowFrame对象上应用过滤器对象。 这将返回类filterResult的对象，然后可以将其用于数据的子集化或计算摘要统计信息。 有关详情，请参见过滤
filter(flowFrame, filter)

19. split
根据过滤器，filterResult或factor分割flowFrame对象。 对于大多数类型的过滤器，可选的flowSet = TRUE参数将创建一个flowSet而不是一个简单的列表。 有关详情，请参阅拆分

split(flowFrame, filter, flowSet=FALSE, ...)
split(flowFrame, filterResult, flowSet=FALSE, ...)
split(flowFrame, factor, flowSet=FALSE, ...)

20. Subset
根据过滤器或逻辑向量子集FlowFrame。 使用带有filter，filterResult或逻辑向量作为第一个参数的标准子集运算符可以完成相同的操作。

Subset(flowFrame, filter)
Subset(flowFrame, logical)

21. cbind2
通过相同长度的数字矩阵中的数据扩展flowFrame。 矩阵的列名必须与flowFrame的列名不同。 数字的附加方法仅引发有用的错误消息。

cbind2(flowFrame, matrix)
cbind2(flowFrame, numeric)

22. compensate
在flowFrame对象上应用补偿矩阵（或补偿对象）。 这将返回补偿的flowFrame。
compensate(flowFrame, matrix) compensate(flowFrame, data.frame)

23. decompensate
在flowFrame对象上反转补偿矩阵（或补偿对象）的应用。 这将返回一个经过反转补偿的矩阵flowFrame。

24. spillover
如果存在，从描述槽中提取溢出矩阵。 它等同于关键字（x，c("spillover", "SPILL")））因此，只会返回 "spillover" and "SPILL"的关键字值列表。
spillover(flowFrame)

25. == 比较两个flowFrame是否相等

26. <, >, <=, >= 
运算符，基本上将flowFrame视为数值矩阵。

27. initialize(flowFrame)
对象实例化，由new使用; 不要被用户直接调用。

```R
## load example data
data(GvHD)
frame <- GvHD[[1]]

## subsetting
frame[1:4,]  # row 选择几个cells col 几个observables
frame[,3]
frame[,"FSC-H"]  # 与下面相同
frame$"SSC-H"

## accessing and replacing raw values
head(exprs(frame))
exprs(frame) <- exprs(frame)[1:3000,]
frame
exprs(frame) <- exprs(frame)[,1:6]
frame

## access FCS keywords
head(description(frame))
keyword(frame, c("FILENAME", "$FIL"))

## parameter annotation
parameters(frame)
pData(parameters(frame))  # 返回各参数的desc, range, minRange, maxRange

## summarize frame data
summary(frame)

## plotting
plot(frame)
if(require(flowViz)){
plot(frame)
plot(frame, c("FSC-H", "SSC-H"))
plot(frame[,1])
plot(frame, c("FSC-H", "SSC-H"), smooth=FALSE)
}

## frame dimensions
ncol(frame)
nrow(frame)
dim(frame)

## accessing and replacing parameter names
featureNames(frame)
all(featureNames(frame) == colnames(frame))
colnames(frame) <- make.names(colnames(frame))
colnames(frame)
parameters(frame)$name
names(frame)  

## accessing a GUID
identifier(frame)
identifier(frame) <- "test"

##  range of a frame
range(frame) #instrument range
range(frame, type = "data") #actual data range
range(frame)$FSC.H

## iterators
head(each_row(frame, mean))
head(each_col(frame, mean))

## transformation
opar <- par(mfcol=c(1:2))
if(require(flowViz))
plot(frame, c("FL1.H", "FL2.H"))
frame <- transform(frame, transformList(c("FL1.H", "FL2.H"), log))
if(require(flowViz))
plot(frame, c("FL1.H", "FL2.H"))
par(opar)
range(frame)

## filtering of flowFrames
rectGate <- rectangleGate(filterId="nonDebris","FSC.H"=c(200,Inf))
fres <- filter(frame, rectGate)
summary(fres)

## splitting of flowFrames
split(frame, rectGate)
split(frame, rectGate, flowSet=TRUE)
split(frame, fres)
f <- cut(exprs(frame$FSC.H), 3)
split(frame, f)

## subsetting according to filters and filter results
Subset(frame, rectGate)
Subset(frame, fres)
Subset(frame, as.logical(exprs(frame$FSC.H) < 300))
frame[rectGate,]
frame[fres,]

## accessing the spillover matrix
try(spillover(frame))

## check equality
frame2 <- frame
frame == frame2
exprs(frame2) <- exprs(frame)*2
frame == frame2

```


### AnnotatedDataFrame
AnnotatedDataFrame由两部分组成。 有一组样本和在这些样本上测量的变量值。包含每个变量测量的描述。可以使用pData和varMetadata访问AnnotatedDataFrame的组件。
创建对象：
AnnotatedDataFrame(data, varMetadata, dimLabels=c("rowNames", "columnNames"), ...)
- data: 样本（rows)和被测量的变量（columns)的data.frame 
- varMetadata是一个data.frame，其行数等于data参数的列数，varMetadata描述了每个测量变量的各个方面。dimLabels为show方法中的行和列标记提供美学控制。可省略。

```R
fcs_files <- list.files(pattern = ".fcs$")
fs <- read.flowSet(fcs_files, transformation = FALSE, truncate_max_range = FALSE)
```
## list.files()
list.files(path = ".", pattern = NULL, all.files = FALSE,
           full.names = FALSE, recursive = FALSE,
           ignore.case = FALSE, include.dirs = FALSE, no.. = FALSE)

       dir(path = ".", pattern = NULL, all.files = FALSE,
           full.names = FALSE, recursive = FALSE,
           ignore.case = FALSE, include.dirs = FALSE, no.. = FALSE)

list.dirs(path = ".", full.names = TRUE, recursive = TRUE)

- path 绝对路径的字符向量 getwd()可以获取工作路径。
- pattern 正则表达式，匹配的文件名才会返回。
- all.files 逻辑值，FALSE时只返回可视的文件，TRUE返回所有文件名，包含隐藏文件。
- full.names  TRUE 将目录路径添加到文件名前，返回相对路径，FASLE返回文件名
- recursive logical 是否递归到子文件夹
- ignore.case  logical 模式匹配应该不区分大小写
- include.dirs logical 子目录名称是否应包含在递归列表中？ （它们总是处于非递归的状态）。
- no.. loical “.” 和“..”两者是否应该被排除在非递归列表之外？

## 读取系列FCS文件 read.flowSet()
read.flowSet(files=NULL, path=".", pattern=NULL, phenoData,
             descriptions,name.keyword, alter.names=FALSE,
             transformation = "linearize", which.lines=NULL,
             column.pattern = NULL, invert.pattern = FALSE, decades=0, sep="\t",
             as.is=TRUE, name, ncdf=FALSE, dataset=NULL, min.limit=NULL,
             truncate_max_range = TRUE, emptyValue=TRUE, 
             ignore.text.offset = FALSE, channel_alias = NULL, ...)
- files   可选的文件名字符向量
- path    文件所在路径
- pattern  参数用于传递到dir 见上面的方法，list.dirs()
- phoneData AnnotatedDataFrame类的对象，要从flowFrame对象中提取的字符或值列表.
- descriptions  
- name.keyword
- alter.names   同read.FCS
-transformation
- which.lines
- column.pattern
- invert.pattern
- decades
- sep
- as.is logical 传到read.AnnotatedDataFrame
- name
- ncdf
- dataset
- min.limit
- truncate_max_range
- emptyValue
- ignore.text.offset
- channel_alias


```R
# 获取各文件各marker均值
setwd("E:/Biology/workspace/")
for (name in dir('./renamed')){
  file.name <- paste(getwd(), name, sep='/renamed/')
  fr <- read.FCS(file.name)
  frs <- summary(fr)
  frm <- frs[4,]
  names <- unlist(strsplit(name, '_'))
  rowNames <- paste(names[2], names[3], names[4], sep='_')
  ff <- data.frame(t(frm),row.names=rowNames)
  df <- rbind(df, ff)
  write.csv(df, file='the intensity of measured markers.csv', append=TRUE,quote=FALSE,sep="",row.names=TRUE, col.names=TRUE, fileEncoding='utf-8')
}

# 可视化各plate的marker值
library(reshape)
library(circlize)
# 设置颜色透明度
add_transparency("red",0.5)
# 将列表转化成矩阵

df <- read.csv('the intensity of measured markers.csv',encoding='gb18030')

```