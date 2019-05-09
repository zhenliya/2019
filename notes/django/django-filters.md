# 安装
pip install django-filter

settings.py 中配置
```python

INSTALLED_APPS = [
    ...
    'django_filters',
]
```
## requirements
Python: 3.4, 3.5, 3.6, 3.7
Django: 1.11, 2.0, 2.1, 2.2
Django REST Framework (DRF): 3.8+

# 开始
## filter
```python
import django_filters

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['price', 'release_date']
```
##  filters 

```python
class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()

    # 1. 声明filters

    # field_name lookup_expr 用于构建完整的ORM中在.filter()左边的表达式
    # field_name 表示用于过滤的字段， 可以使用__表示关系字段  比如 manufacturer__name
    # lookup_expr 被查找字段的表现形式。默认为exact , 
    # in, range, and isnull
    #如果表达式部分与ORM查找结合可以包含语法转换规则，使用__分割，例如：查找日期中的年部分 year__gt如下
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    release_year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    release_year__gt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
    release_year__lt = django_filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')

    manufacturer__name = django_filters.CharFilter(lookup_expr='icontains')
    
    # 2. 使用Meta.fields生成filters
    class Meta:
        model = Product 
        # 可以返回筛选字段列表
        # fields = ['price', 'release_date']
        # 也可以以字典的形式指定筛选字段，需要在上面生成price__lt’, ‘price__gt’, ‘release_date’, 和‘release_date__year__gt’filters 
        fields = {
	        'price': ['lt', 'gt'],
	        # 默认为'exact' ,不需要再__exact 形式表示
	        'release_date': ['exact', 'year__gt'],
	    }
	    # fields 可以包含关联字段
	    # fields = ['manufacturer__country']

	 # 3. 可以在Meta中重写默认的filters
		 filter_overrides = {
	            models.CharField: {
	                'filter_class': django_filters.CharFilter,
	                'extra': lambda f: {
	                    'lookup_expr': 'icontains',
	                },
	            },
	            models.BooleanField: {
	                'filter_class': django_filters.BooleanFilter,
	                'extra': lambda f: {
	                    'widget': forms.CheckboxInput,
	                },
	            },
```
# 基于request的filtering

由于不能保证request请求总是提供FilterSet实例，任何依赖request请求的代码需要处理 None 的情况

## 筛选主键
通过request对象过滤主键queryset,只需要重写FilterSet.qs属性

例如：过滤已发布并且所有者已登录的博客文章
```python
class ArticleFilter(django_filters.FilterSet):

    class Meta:
        model = Article
        fields = [...]

    @property
    def qs(self):
        parent = super(ArticleFilter, self).qs
        author = getattr(self.request, 'user', None)

        return parent.filter(is_published=True) | parent.filter(author=author)

```

## 筛选关系字段
filters.ModelChoiceFilter 
filters.ModelMultipleChoiceFilter  支持可调用行为
```python 
def departments(request):
    if request is None:
        return Department.objects.none()

    company = request.user.company
    # 附表字段查询子表
    return company.department_set.all()

class EmployeeFilter(filters.FilterSet):
    department = filters.ModelChoiceFilter(queryset=departments)
    ...
```
## 使用Filter.method 自定义过滤
https://django-filter.readthedocs.io/en/latest/guide/usage.html
```python

class F(django_filters.FilterSet):
    username = CharFilter(method='my_custom_filter')

    class Meta:
        model = User
        fields = ['username']

    def my_custom_filter(self, queryset, name, value):
        return queryset.filter(**{
            name: value,
        })

```

# 与DRF集成
## 1.导入
```python
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    ...
```
## 2. 增加DjangoFilterBackend
需要增加 DjangoFilterBackend 到filter_backends中
```python
	filter_backends = (filters.DjangoFilterBackend,)

```
默认使用，可以在全局配置：
```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        ...
    ),
}

```
## 3. 使用filterset_class添加FilterSet 
```python

from rest_framework import generics
from django_filters import rest_framework as filters
from myapp import Product


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'in_stock', 'min_price', 'max_price']


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
```
## 4. 使用filter_fields 配置过滤字段
```python
from rest_framework import generics
from django_filters import rest_framework as filters
from myapp import Product


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', 'in_stock')


# Equivalent FilterSet:
class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ('category', 'in_stock')

```
不允许同时使用filterset_fields和filterset_class

## 5. 自定义FilterSet创建

在ViewSet中自定义如下方法
.get_filterset(self, request, queryset, view)
.get_filterset_class(self, view, queryset=None)
.get_filterset_kwargs(self, request, queryset, view)

## 6.Schema Generation with Core API 

```python

class IssueViewSet(views.ModelViewSet):
    queryset = models.Issue.objects.all()

    def get_project(self):
        try:
            return models.Project.objects.get(pk=self.kwargs['project_id'])
        except models.Project.DoesNotExist:
            return None

    def get_queryset(self):
        project = self.get_project()

        if project is None:
            return self.queryset.none()

        return self.queryset.filter(project=project) .filter(author=self.request.user)
```