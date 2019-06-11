# 使用R
1. 安装IRkernel
```R
install.packages("devtools")
devtools::install_gethub("IRkernel/IRkernel")
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