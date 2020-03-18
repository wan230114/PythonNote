

# 《Django 项目之网络云笔记》
## 目录
[TOC]

## 网络云笔记项目
- 功能:
    1. 注册
    1. 登陆
    1. 退出登陆
    1. 查看笔记列表
    1. 创建新笔记
    1. 修改笔记
    1. 删除笔记
### 数据库设计
- 模型类
    1. 用户模型类
        ```python
        class User(models.Model):
            username = models.CharField("用户名", max_length=30, unique=True)
            password = models.CharField("密码", max_length=30)
        create_time = models.DateTimeField('创建时间', auto_now_add=True)
        
            def __str__(self):
                return "用户" + self.username
        ```
    2. 笔记模型类

    ~~~python
    from django.db import models
    from user.models import User
    class Note(models.Model):
        title = models.CharField('标题', max_length=100)
        content = models.TextField('内容')
        create_time = models.DateTimeField('创建时间', auto_now_add=True)
        mod_time = models.DateTimeField('修改时间', auto_now=True)
    user = models.ForeignKey(User)
    
    ```
    ~~~


### 设计规范
- 登陆设计规范(在user应用中写代码)
    | 路由正则 | 视图函数 | 模板位置 | 说明 |
    |-|-|-|-|
    | /user/login | def login_view(request): | templates/user/login.html | 用户登陆 |
    | /user/reg | def reg_view(request): | templates/user/register.html| 用户注册 |
    | /user/logout  | def logout_view(request):| 无 | 退出用户登陆 |

    - 参考界面:
        - 登陆界面
            - ![](cloud_note_images/login.png)
        - 注册界面
            - ![](cloud_note_images/reg.png)

- 主页设计规范(在index应用中写代码)
    | 路由正则 | 视图函数 | 模板位置 | 说明 |
    |-|-|-|-|
    | / | def index_view(request): | templates/index/index.html | 主页 |

    - 参考界面
        - 登陆前
            - ![](cloud_note_images/index1.png)
        - 登陆后
            - ![](cloud_note_images/index3.png)
    
- 云笔记设计规范
    | 路由正则 | 视图函数 | 模板位置 | 说明 |
    |-|-|-|-|
    | /note/ | def list_view(request): | templates/note/list_note.html | 显示笔记列表功能 |
    | /note/add | def add_view(request): | templates/note/add_note.html| 添加云笔记 |
    | /note/mod/(\d+)  | def mod_view(request, id): | templates/note/mod_note.html | 修改之前云笔记 |
    | /note/del/(\d+) | def del_view(request, id): | 无(返回列表页) | 删除云笔记|
    | /note/(\d+) | def show_view(request, id): | templates/note/note.html | 查看单个云笔记 |
    - 参考界面
        - 登陆界面
            - ![](cloud_note_images/login.png)
        - 注册界面
            - ![](cloud_note_images/reg.png)
        - 添加新笔记界面
            - ![](cloud_note_images/new_note.png)
        - 显示笔记列表
            - ![](cloud_note_images/list_note.png)
        - 修改云笔记
            - ![](cloud_note_images/mod_note.png)
        - 主页
            - 登陆前
                - ![](cloud_note_images/index1.png)
            - 登陆后
                - ![](cloud_note_images/index2.png)

