from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Users, Stu, StuInfo, ClassInfo, Books, Tags


def index(request):
     # # 方法1
    # data = {
    #     'name':'zhansan',
    #     'age':20,
    #     'sex':'男'
    # }
    # # 返回json数据,这个是正儿八经的json
    # 这个更加标准
    # return JsonResponse(data)

    # 方法2
    import json
    data = {
        'name': 'zhansan',
        'age': 20,
        'sex': '男'
    }
    # 使用python 的json模块,转为json再返回
    # 这个其实是以html返回的
    return HttpResponse(json.dumps(data))