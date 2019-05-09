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