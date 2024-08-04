# Django框架学习

### 本项目主要是是记录自己学习后端过程以及一些心得

#### 2024.7.16

项目初始化

创建面板

整理数据库相关的知识

项目前期涉及到的命令

`django-admin startproject project_name`：创建一个`django`项目

`django-admin startapp app_name`：创建`django`项目下的`app_name`项目，与主项目`django`进行配置连接

`python manager.py runserver` : 启动`django`框架

`python manager.py migrate`：将 `django` 项目中的模型（Models）变更应用到数据库中

`python manager.py makemigrations`：生成描述模型（Models）变更的迁移文件。这个命令会检查项目中的模型，找出与当前数据库结构的不同之处，然后生成相应的迁移文件

[query相关操作](https://docs.djangoproject.com/en/5.0/topics/db/queries/)，具体操作直接查看官方文档，`django`的文档写的非常详细

#### 2024.7.17

CRUD操作

主要是利用表单的相关知识进行请求，只有发起请求，django后端才能进行相应的处理，同时如果你想简单的对后端进行测试，那么前端设置一个简单的html的form表单是最简单的方式

```html
<form method='POST'>
......

<input type='submit'>
</form>
```

关于django中template中表单请求的书写，可以参考这篇[document](https://docs.djangoproject.com/en/5.0/topics/forms/)，如果是基于已经创建好的数据库类创建model，可以参看这篇[document](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm)



#### 2024.7.20（model新增加一列特征）

```python
# install these library
pip install Pillow
pip install whitenoise
```

load static files：主要是加载一些静态文件，在实现项目的过程中，不可避免地会涉及到`image`文件，但是管理这些`image`文件又是非常的棘手，所以引入了静态文件，对这些文件进行管理。

其中最主要的也是最麻烦的点在于`url`和文件存储位置的映射，这些设置都在最主要的项目文件下的`setting.py`文件中进行设置，最后在`urls.py`这个文件中完成映射。

```python
STATIC_URL = "/static/"
# images store position(directory)
MEDIA_URL = "/images/"

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
# media files 
MEDIA_ROOT = os.path.join(BASE_DIR,'static/images')
# store all static files
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
```

`urls.py`文件中新增的内容（将对应的url和对应文件夹中的内容进行对应）：

```
# url mapping
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# static mapping 
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
```

重点：使用`MEDIA_URL`和`STATIC_URL`这个参数主要是为了实现后面的`url mapping`，不然后面的`url`很难做到准确的`mapping`。

其中涉及到`static files`的整合，此时需要使用`python .\manage.py collectstatic `,回生成`staticfiles`文件夹这个内容，这个文件夹会将所有的静态文件收集。但是也有一个问题，我们需要使用这些静态文件向外展示，所以此时就引入了[`whitenoise`](https://whitenoise.readthedocs.io/en/latest/)依赖，导入该依赖可以解决静态文件无法使用的问题。

#### 2024.7.21(实现theme的添加,添加users app，实现users app初始化界面)

##### 添加theme

将生成的前端文件结合`django`中`templates`语法进行结合，将重复的模块采取`for loop`的形式展示，从而减少代码量，注意：将添加的html文件粘贴到对应的templates模块中

[`templates language`](https://docs.djangoproject.com/en/5.0/ref/templates/language/)

##### 添加users app

`python manager.py startapp users`：添加users模块

配置`setting.py`文件，添加`users.apps.UsersConfig`到`INSTALLED_APPS`中，配置模块能被主项目识别到

配置`urls.py`文件，将`path("",include("users.urls"))`添加到`urlpattern`变量中，项目可以识别到`users`项目对应的`urls`

编写测试文件，首先书写`views`中`render`函数，创建`urls.py`文件，书写`url`的转向，编写`templates/users`文件夹下的`html`文件，还是继承自`main.html`，使用对应的`navbar.html`文件

书写`model.py`文件，编写对应的数据库文件，执行`python manage.py makemigrations`执行，最后执行`python manage.py migrate`实现数据库的迁移

注意：这里使用到了[`django user`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/)，可以参考这边文档了解`django user`的一些属性

#### 2024.7.22

实现了个人页面的书写，同时添加了`Skill`数据库内容，并将`Profile`数据库内容添加一行`location`特征

`Signal`：`django`中[`signal`](https://docs.djangoproject.com/en/5.0/topics/signals/)的传递，用来判断用户创建时的一系列操作，从而可以创建一系列连锁条件数据库。对应[post_save,post_delete](https://docs.djangoproject.com/en/5.0/ref/signals/)的参考对应`doc`. 代码中的[created](https://docs.djangoproject.com/en/5.0/ref/signals/#post-save)参数的文档链接在此处，点击即到.

#### 2024.7.25

添加用户的`login`页面，`logout`页面，在这里用到了[`authenticate`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#how-to-log-a-user-in)验证，具体细节直接参考这部分`documentation`，同时也建议看一看`doc`上面的`User`部分信息，加深对于核心模块的理解。

基于`Django`的[`message`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#displaying-messages)将登录遇到的一些报错信息进行展示，并且使用对应的`JS`实现`message`部分的信息，添加[`message`](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/#adding-a-message)部分的信息，例如`message.info()`等信息如何进行展示，参考文档即可，结合代码理解

#### 2024.7.26

添加了`register`页面，创建对应的`form`代码，用于将保存的数据提交到数据库中。在保存用户名的时候，统一将用户名保存为小写，避免在注册后出现两个同名用户。最后将`login`和`register`页面进行美化，结合对应`Django`的`template`语法进行优化代码。

#### 2024.7.27

添加了`account`页面，将前端页面和数据库中存储的信息进行对接。

添加用户信息编辑部分的内容，书写对应的`urls.py`，`views.py`以及对应的`html`文件，注意这部分的`form`需要自定义，只要是涉及到提交的内容，修改的内容，都需要自定义`form`模块。

注意最后将用户和他们的项目进行绑定，从`request`中获取到`user`，再从`user`中获取到对应的`profiles`和`projects`，将这些信息进行绑定。

一定要注意`Django`中的`ORM`，一对多，一对一这些关系都可以在`Django`中实现为双向绑定，`ORM`这部分内容容我补补相关博客再来总结。

补上之前的[`ORM`](https://opensource.com/article/17/11/django-orm)的相关内容，`Django`的`ORM`帮我们完成了数据库的一系列操作，包括数据库中的join操作，通过`ManytoManyField`、`OnetoOneField`等属性完成双向绑定，也就是关系型数据库中的`join`操作，使得在调用数据库的极大的提高了我们的效率，`Django`当之无愧的最好用的`WEB`开发框架。

要想进入对应的`python`命令行中操作，执行`python manager.py shell`，进入命令行之后就可以引入我们之前创建的一系列模型，并对他们进行[`CRUD`](https://tutorial.djangogirls.org/en/django_orm/)操作。

关于操作中的双下划线，可以参考以下英文解释，加深理解。关于`Django`的这些关系可以直接查看[`Django model`](https://docs.djangoproject.com/en/5.0/topics/db/models/)的官方文档。

Under the hood, the string is split by these underscores, and the tokens are processed separately. `name__contains` gets changed into `attribute: name, filter: contains`. In other programming languages, you may use arrows instead, such as `name->contains` in `PHP`

#### 2024.7.28

主要处理了`skills`的添加、编辑和删除操作，这些操作和`projects`中的操作基本一致

梳理一下添加的流程，首先简单书写一个`html`页面，页面中提供一个表单`POST`请求，然后去`Django`项目中`view.py`中书写一个对应的函数处理文件，刚开始只需要写一个`render`,然后在`urls.py`文件中书写对应的`url`映射和函数触发，同时并为这个`url`提供一个`name`，方便书写`html`文件的调用类似于这种`{% url 'login' %}`这种方式，这就是整个流程。

在刚开始，需要自己手动在`admin`页面中创建一些数据记录，然后使用`Django`的`ORM`特性以及一些方法取得对应的数据，此时你可能就会想到为什么不自己创建数据记录呢，别急，接下来就说如何自己创建数据记录，自己创建数据记录需要涉及到[`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm),这部分可以参考7.17的记录。update、delete都会涉及到表单，但是update同时还会涉及到[`ModelForm`](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/#django.forms.ModelForm),而delete只会涉及到`POST`的`form`请求，这里尤其需要注意，涉及到`POST`请求时，一定要注意需要`{% csrf_token %}`这个属性，并且这个属性一定要在单独一行，否则会报错。

#### 2024.7.29

今天主要完成`search`和`pageup`功能。

`search`功能的实现可以使用第三方库[`Django filter`](https://django-filter.readthedocs.io/en/stable/index.html)和自己手动实现相关搜索的内容。

首先介绍自己手动实现`search`功能的方法：由于`Django`中出色的`ORM`实现，使得开发者可以以较少的代码完成这个庞大的搜索过程。

搜索的核心过程为获取到前端传来的搜索参数，利用python语法从数据库中找到对应的对象，同时将搜索到的参数返回。部分核心代码如下所示，基本逻辑大同小异。

```PYTHON
from .models import Project,Tag


def searchProjects(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    print(search_query)

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )

    return projects,search_query
```

使用第三方库文件的方式稍后在学完[`pageup`](https://docs.djangoproject.com/en/5.0/topics/pagination/)之后进行实践，官方文档给出了很具体的解释，关于这些翻页的功能，以及一些属性的使用，直接调用`from django.core.paginator import Paginator`即可完成这个库文件的引用。

关于[page](https://docs.djangoproject.com/en/5.0/topics/pagination/#example)这个操作，参考案例中的代码进行书写即可，可以仔细查看这些方法和属性，利用`Paginator`的各种属性，结合`template`语法实现翻页功能，注意：在这里使用了一个以前没有用过的`template`语法，使用了`with`语法，将表单传来的数值传递给`include`的这个`html`文件，具体代码为`{% include 'pagination.html' with queryset=profiles custom_page=custom_page %}`.

##### `request.user`

关于`request.user`的使用，也是一个很关键的话题。`request.user` 是 Django 中的一个重要概念，表示当前登录的用户。`request.user` 是 Django 的 `User` 模型的一个实例，它提供了与当前用户相关的各种属性和方法。

```python
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Profiles(models.Model):
    # set null = true to debug some codes
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=500,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    short_intro = models.CharField(max_length=200,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(
        null=True,blank=True,upload_to='profiles/',default="profiles/user-default.png"
    )
    social_github = models.CharField(max_length=200,blank=True,null=True)
    social_twitter = models.CharField(max_length=200,blank=True,null=True)
    social_linkedin = models.CharField(max_length=200,blank=True,null=True)
    social_youtube = models.CharField(max_length=200,blank=True,null=True)
    social_website = models.CharField(max_length=200,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.username)
```

上述模型的定义中，可以使用`profile = request.user.profiles`访问与其关联的模型，这得益于`python`的`orm`特性， `User` 模型通过一对一关系与 `Profile` 模型相关联。这里的 `profiles` 是一个属性或方法，代表当前用户的 `Profile` 实例。如果 `User` 和 `Profile` 之间存在一对多关系，则需要使用 `request.user.profile` 或类似的方式来获取。

- 如果 `profiles` 是一个相关字段的名称，这可能是一个 `RelatedManager`，允许你访问与当前用户关联的 `Profile` 实例。
- 如果 `profiles` 是用户自定义的方法，它将返回该用户的 `Profile` 实例。

注意：

1. 确保 `User` 模型有一个有效的与 `Profile` 的关系。
2. 在 Django 中，`request.user` 只有在用户通过认证后才会被设置。若用户未登录，则 `request.user` 将是一个 `AnonymousUser` 对象。

#### 2024.7.31

添加了`review`模块：中规中矩的添加`review`模块，其中特别要注意的是`form`中的`action`的优先级是最高的,如果想要修改`form`提交的的`url`后面的`GET`参数，这个时候就不能填写`form`中action的参数，在`single-project`文件中第60行可以定位到这个文件，可以进一步观察这个参数，对应的文件修改在`login_register.html`的第67行。

添加了`message`模块：中规中举的添加流程，其中需要注意如果一个数据库中出现了两个同样的外键，此时就需要为其中一个外键添加`related_name`这个参数，在以后查询与这个外键相关的联系时，直接使用这个`related_name`这个参数的数值进行访问即可。另外还需要注意的是在保存`form`内容时，一定要将该`form`的所有的参数填写完整，注意登录用户有些数值可以直接在后端获取进行赋值即可，从而可以减少前端数值的填写内容。

#### 2024.8.1

[`django restframe`](https://www.django-rest-framework.org/) 模块:

- install：`pip install djangorestframework`

- [`request and response data `](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/)

- `model serialization`

  - [`modelserializers`](https://www.django-rest-framework.org/tutorial/1-serialization/#using-modelserializers)

  - [`use our Serializer`](https://www.django-rest-framework.org/tutorial/1-serialization/#writing-regular-django-views-using-our-serializer)

  - 同时可以自定义序列化模型的一些参数，例如如下所示的`model`

    - ```python
      class ProjectSerializer(serializers.ModelSerializer):
          # override some attribute
          owner = ProfileSerializer(many=False)
          tags = TagSerializer(many=True)
          # this is another way to use this model
          reviews = serializers.SerializerMethodField()
          
          class Meta:
              model = Project
              fields = '__all__'
              
          # get_reviews is correlated with reviews
          def get_reviews(self,obj):
              reviews = obj.review_set.all()
              serializer = ReviewSerializer(reviews,many=True)
              return serializer.data
      ```

    - owner和tags是该类中的属性，但是该属性并没有具体的信息，在此处对这些属性进行定义，并将其添加在后端进行显示，最终将该数据库中的信息补全。


[`django simple jwt`](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/):

- [install](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation)

- [setting配置](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html)

  - ```python
    # Django project settings.py
    
    from datetime import timedelta
    ...
    
    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
        "ROTATE_REFRESH_TOKENS": False,
        "BLACKLIST_AFTER_ROTATION": False,
        "UPDATE_LAST_LOGIN": False,
    
        "ALGORITHM": "HS256",
        "SIGNING_KEY": settings.SECRET_KEY,
        "VERIFYING_KEY": "",
        "AUDIENCE": None,
        "ISSUER": None,
        "JSON_ENCODER": None,
        "JWK_URL": None,
        "LEEWAY": 0,
    
        "AUTH_HEADER_TYPES": ("Bearer",),
        "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
        "USER_ID_FIELD": "id",
        "USER_ID_CLAIM": "user_id",
        "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    
        "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
        "TOKEN_TYPE_CLAIM": "token_type",
        "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    
        "JTI_CLAIM": "jti",
    
        "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
        "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
        "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    
        "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
        "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
        "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
        "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
        "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
        "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
    }
    ```

[django cors headers](https://pypi.org/project/django-cors-headers/)  :

- [`install and setting`](https://pypi.org/project/django-cors-headers/)
- 是一个Django插件，**用于处理跨域资源共享（CORS）问题**。 它允许从指定的来源或所有来源访问管理站点。
- 解决了一个文件跨域的问题，比如说前端文件无法访问到后端文件，比如报错`don't have access to have it set up`，这时候就要下载`djano_cors_header`，在`setting`中配置相关信息
