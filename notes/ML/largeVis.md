#LargeVise包windows 安装
https://github.com/lferry007/LargeVis
安装boost
命令运行boost_1_68_0目录下的 bootstrap.bat
安装报错：
Building Boost.Build engine
'cl' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

Failed to build Boost.Build engine.
Please consult bootstrap.log for further diagnostics.

网上解决办法：
安装Visual Studio并配置环境变量
	https://blog.csdn.net/kaige_zhao/article/details/80315697

To install the Python wrapper, modify setup.py to make sure that the BOOST path is correctly set and then run python setup.py install.