https://www.jb51.net/article/120804.htm

getpass模块提供了平台无关的在命令行下输入密码的方法;

该模块主要提供:
两个函数: getuser, getpass
一个报警: GetPassWarning(当输入的密码可能会显示的时候抛出，该报警为UserWarning的一个子类)

## getpass.getuser() 
该函数返回登陆的用户名,不需要参数
该函数会检查环境变量LOGNAME,USER,LNAME 和USERNAME, 以返回一个非空字符串。如果这些变量的设置为空的话，会从支持密码的数据库中获取用户名，否则会触发一个找不到用户的异常！

## getpass.getpass([prompt[, stream]])
会显示提示字符串, 关闭键盘的屏幕回显，然后读取密码
可带提示符, 不带提示符，则会输入默认提示符'Password: 
