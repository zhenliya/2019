# 命令
创建项目：django-admin startproject mysite
启动项目：python manage.py runserver 8000

## url中的path
path() 参数： 必须：route 和view
route 是一个匹配 URL 的准则（类似正则表达式）。当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。

这些准则不会匹配 GET 和 POST 参数或域名。例如，URLconf 在处理请求 https://www.example.com/myapp/ 时，它会尝试匹配 myapp/ 。处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/。

view
当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入

kwargs
任意个关键字参数可以作为一个字典传递给目标视图函数

name
为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式

## django INSTALLED_APPS 
INSTALLED_APPS 默认包括了以下 Django 的自带应用：

django.contrib.admin -- 管理员站点， 你很快就会使用它。
django.contrib.auth -- 认证授权系统。
django.contrib.contenttypes -- 内容类型框架。
django.contrib.sessions -- 会话框架。
django.contrib.messages -- 消息框架。
django.contrib.staticfiles -- 管理静态文件的框架。
默认开启的某些应用需要至少一个数据表，所以，在使用他们之前需要在数据库中创建一些表。