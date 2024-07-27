# Django框架学习

### 本项目主要是是记录自己学习后端过程，后端组件如何沟通，如何向前端API进行展示

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

`Signal`：`django`中[`signal`](https://docs.djangoproject.com/en/5.0/topics/signals/)的传递，用来判断用户创建时的一系列操作，从而可以创建一系列连锁条件数据库。

`post_save`:

`post_delete`:

#### 2024.7.25

user login ，logout and Flash message (django message)

#### 2024.7.26

实现了register page，将login和register页面进行美化

#### 2024.7.27

添加了`account`页面，将前端页面和数据库中存储的信息进行对接





