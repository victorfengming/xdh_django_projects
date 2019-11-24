"""first_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from home import views





urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/index/(?P<page>[0-9]+)/$', views.user_index),
    url(r'^user/index/$', views.user_index,name="user_index"),
    url(r'^mod/demo/$', views.mod_demo,name="mod_demo"),
    url(r'^demo/$', views.demo,name="demo"),

    # 用户数据的管理
    url(r'stu/index$',views.stu_index,name='stu_index'),
    # 执行用户的添加
    url(r'stu/insert$',views.stu_insert,name='stu_insert'),
    # 显示添加的表单
    url(r'stu/add$',views.stu_add,name='stu_add'),
    # 执行用户的删除
    url(r'stu/del$',views.stu_del,name='stu_del'),
    # 用户的编辑表单
    url(r'stu/edit$',views.stu_edit,name='stu_edit'),
    # 执行用户数据的更新
    url(r'stu/update$',views.stu_update,name='stu_update'),

]
