# 使用R
1. 安装IRkernel
```R
install.packages("devtools")
devtools::install_github("IRkernel/IRkernel")
IRkernel::installspec()
```
2. 使用ryp2 python包在R-py之间切换 
```Python
pipinstall ryp2
# 导入
%load_ext rpy2.ipython
# 将整个cell设为R代码
%%R
#将一行设为R代码：%R
%R print("R")
# 从R获取变量var
%R -o var
# 从python获取变量
%R -i var
```

# 修改默认路径
windows中生成配置文件
jupyter notebook --generate-config

修改配置文件中
c.NotebookApp.notebook_dir为指定目录