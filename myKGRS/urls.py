from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',views.index),
    path('index/',views.index),
    path('activity/',views.activity),
    # path('activity2/',views.activity2),
    path('imglist/',views.imglist),

    path('getpng/',views.createImg),
    path('login/',views.login),#用于打开登录页面
    path('login/save',csrf_exempt(views.save)),#输入用户名密码后交给后台save函数处理
    path('login/query',csrf_exempt(views.query)),#输入用户名密码后交给后台query函数处理

]