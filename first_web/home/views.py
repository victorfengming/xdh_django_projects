from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

# 创建一个试图函数,输出Helloween
def index(request):
    return render(request,'abc/b.html')
    # 在试图函数中进行响应
    # return HttpResponse('试图函数执行的结果')

def abc(request):
    return HttpResponse('访问我嘎哈!!!')

def demo(request):

    # 假装从数据库中取到了一条记录
    cont = ['成了','bicheng']
    data = {'info':cont}
    # return render(request,'a.html',data)

def article(request,para):
    return HttpResponse('接受到的参数是:'+para)

def article2(request,aa):

    return HttpResponse('接受到的参数是2是:'+aa)

def user_index(request,page=1):
    print(page)
    return HttpResponse('用户列表数据的显示')
    # raise Http404('纳尼@_@')
