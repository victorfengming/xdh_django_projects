from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 创建一个试图函数,输出Helloween
def index(request):

    # 在试图函数中进行响应
    return HttpResponse('试图函数执行的结果')