from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from . import models
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

def mod_demo(request):
    # 使用模型进行操作数据库 数据的查询操作
    res = models.Users.objects.all()
    print(res)
    # < QuerySet[ < Users: Users object >] >
    # 一个查询集
    for x in res:
        print(x.username)
    return HttpResponse('模型你给的操作演示')


# 用户数据管理 用户列表

def stu_index(request):
    # 调用模型,获取用户数据
    data = models.Stu.objects.all()
    # 分配数据
    context = {'userlist':data}
    # 加载模板,返回数据
    # 显示一个添加的页面
    return render(request,'stu/index.html',context)

def stu_add(request):
    # 显示一个添加的页面
    return render(request,'stu/add.html')

# 执行用户的添加
def stu_insert(request):

    # 接收用户发送的表单数据
    data = request.POST.dict()
    # 删除csrf
    data.pop('csrfmiddlewaretoken')
    print(data)
    # request是请求对象,请求的一切信息都有
    # {添加到数据库'username': '张三', 'password': '3456', 'age': '23'}
    obj = models.Stu(**data)
    # 调用save方法进行保存
    obj.save()
    # 添加到数据库
    # 返回到列表页

    # return HttpResponse('<script> alert("添加成功!"); location.href = "/stu/index";</script>')
    # 在python代码中不能{% 这样写了 %},所以应该这样
    return HttpResponse('<script> alert("添加成功!"); location.href = "'+reverse('stu_index')+'";</script>')


# 执行用户的删除
def stu_del(request):
    print('uid是')
    # 接收id对象
    uid = request.GET.get('uid')
    print(uid)
    # 获取用户对象
    ob = models.Stu.objects.get(sid=uid)
    # 执行删除
    ob.delete()
    # 跳转到列表页面
    return HttpResponse('<script> alert("删除成功!"); location.href = "'+reverse('stu_index')+'";</script>')


# 用户数据的编辑
def stu_edit(request):
    # 获取用户id
    uid = request.GET.get('uid')
    # 根据id 获取用户对象
    ob = models.Stu.objects.get(sid=uid)
    # 吧用户数据显示到编辑的表单中
    content = {'uinfo':ob}
    # 加载模板
    return render(request,'stu/edit.html',content)


def stu_update(request):
    # 获取表单数据
    data = request.POST.dict()
    data.pop('csrfmiddlewaretoken')
    # 接收id
    uid = request.GET.get('uid')
    # 根据id获取对象
    ob = models.Stu.objects.get(sid=uid)
    # 修改对象的属性
    ob.name = request.POST.get('name')
    print('-'*80)
    print(ob.name)
    print('-'*80)
    ob.email = request.POST.get('email')
    ob.age = request.POST.get('age')
    # 执行修改
    ob.save()
    # 跳转到列表页面
    return HttpResponse('<script> alert("更新成功!"); location.href = "' + reverse('stu_index') + '";</script>')
