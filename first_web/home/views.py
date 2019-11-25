from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Users, Stu, StuInfo, ClassInfo, Books, Tags


def index(request):
    data = {
        'name':'zhansan',
        'age':20,
        'sex':'男'
    }
    # 返回json数据
    return JsonResponse(data)


# 设置 cookie
def cookie_set(request):
    # 设置 cookie
    # 1. 先获取响应对象
    res = HttpResponse()
    # 2. 使用响应对象设置cookie
    res.set_cookie('name',"yichuan")
    # 3.返回响应对象
    return res


#
def cookie_get(request):
    # 在请求对象中或区域cookie信息
    data = request.COOKIES.get('name')
    print(data)

    return HttpResponse('获取cookie')

def session_set(request):
    # 设置 session
    request.session['VipUser'] = {
        'name':'zhangsan',
        'age':20,
        'id':101,
    }
    request.session['username'] = '张三'
    request.session['age'] = 18
    return HttpResponse('session设置')

def session_get(request):
    # 获取session
    data1 = request.session.get('VipUser')
    data2 = request.session.get('username')
    data3 = request.session.get('age')
    print(data1,data2,data3)
    # # 删除指定key
    # del request.session['username']
    # 清楚会话的内容,当前内容没了,会话还在
    # request.session.clear()

    # # 删除会话,把当前会话相关的数据全部删除
    # request.session.flush()
    # 这个session比较常用的,比如登录注册
    # 更或者是用户加入购物车的数据都有可能放到session里面
    # 比如有的网站你不登录就不能加入购物车,这种网站就是把你购物车的数据放到数据库里面了
    # 还有一些网站你可以先加入购物车,然后后后登录在买,这就要将购物车的数据放到session里面了

    return HttpResponse('session获取')
