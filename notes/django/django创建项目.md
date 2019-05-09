# 项目创建步骤
创建项目：django-admin startproject mysite
启动服务：python manage.py runserver
创建app：python manage.py startapp polls
提交修改： python manage.py makemigrations polls
同步修改到数据库： python manage.py migrate polls
返回SQL同步命令： python manage.py sqlmigrate polls 001

创建超级用户: python manage.py createsuperuser


# 迁移同步报错ModuleNotFoundError: No module named 'name'


