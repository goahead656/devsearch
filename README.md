# Django项目学习

### 本项目主要是是学习后端内容，后端组件如何沟通，如何向前端api进行展示

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

