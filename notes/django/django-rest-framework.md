# serializers
serializers允许querysets 和model实例转换为，能够容易渲染为JSON,XML或其他类型的python数据类型。
同时支持反序列化接受的数据为复杂了类型。

类似于django中的Form 和 ModelForm

Serializer类用于控制response输出， ModelSerializer类提供快捷方式创建处理instances和querysets的Serializers 

## 创建serializer
```python

from rest_framework import serializers

def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    # 可以在Serializer对象中使用验证器
    score = IntegerField(validators=[multiple_of_ten])
    room_number = serializers.IntegerField(choices=[101, 102, 103, 201])


    # 也可以将validators声明在Meta中
        class Meta:
        # Each room only has one event per day.
        validators = UniqueTogetherValidator(
            queryset=Event.objects.all(),
            fields=['room_number', 'date']
        )


```
## 序列化对象
与Django中Form类使用类似
```python
serializer = CommentSerializer(comment)
serializer.data
# {'email': 'leila@example.com', 'content': 'foo bar', 'created': '2016-01-27T15:17:10.375877'}
```
## 将对象转换为json

```python
from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
json
# b'{"email":"leila@example.com","content":"foo bar","created":"2016-01-27T15:17:10.375877"}'

```

##  反序列化对象

反序列化数据前需要调用is_valid()后才能使用验证后的数据
```python
import io
from rest_framework.parsers import JSONParser

# 1. 传入数据流
stream = io.BytesIO(json)
data = JSONParser().parse(stream)

# 2. 将合法数据存储数据为字典或
serializer = CommentSerializer(data=data)
serializer.is_valid()

# Return a 400 response if the data was invalid.
# serializer.is_valid(raise_exception=True)
# True
# 反序列化后的数据，字典的key为字段名
serializer.validated_data
# {'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.datetime(2012, 08, 22, 16, 20, 09, 822243)}

```


## 将验证过的数据保存为实例
使用.create() 和 .update()方法
```python
class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)
        # return Comment.objects.create(**validated_data)

    
    # validated_data 中接受传入的数据
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        # 如果instance是model实例，可以保存到数据库
        # instance.save()
        return instance

    # 返回实例对象，当实例存在时更新，不存在时创建
    comment = serializer.save()

    # .save() will create a new instance.
serializer = CommentSerializer(data=data)

# .save() will update the existing `comment` instance.
serializer = CommentSerializer(comment, data=data)
```
调用.create() 或.update() 时， 增加的关键字参数包含在 serializer.validated_data 参数中

## 重写save()
```python

# 发送邮件
class ContactForm(serializers.Serializer):
    email = serializers.EmailField()
    message = serializers.CharField()

    def save(self):
        email = self.validated_data['email']
        message = self.validated_data['message']
        send_email(from=email, message=message)

```

## serializer 制定字段级别验证
使用 .validate_字段名  类似Djiango中 .clean_字段名 
如果字段名 在serializers 

If your <field_name> is declared on your serializer with the parameter required=False then this validation step will not take place if the field is not included.

```python
from rest_framework import serializers

class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value

```

## serializer 制定对象级别验证

在Serializer中实现一个方法  validate(data)

```python
from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    # 传入的参数为字段组成的字典
    # 可以返回错误serializers.ValidationError 或者返回验证过后的数据
    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
```
## initial_data
当传入数据到serializer实例时存在，否则为None


## 部分更新数据
serializers必须传递所有required字段，否则报错validation errors
可以使用partial参数，允许部分更新
```python
# Update `comment` with partial data
serializer = CommentSerializer(comment, data={'content': 'foo bar'}, partial=True

```

## 处理嵌套对象 
Serializer类本身是一种Field,可以用来代表关联
```python
# comment 是user表的子表

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class CommentSerializer(serializers.Serializer):
   # required=False 表示接受None 值， many=True,表示多个值一个user对应多个comment
    user = UserSerializer(required=False)
    edits = EditItemSerializer(many=True)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

```
## 保存关联表对象
```python
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

```