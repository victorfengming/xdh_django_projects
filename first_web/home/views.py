from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render

from . models import Citys


def index(request):

    return HttpResponse('helloworld')

def citys(request):
    # 从数据库中获取所有的一级城市信息
    data = Citys.objects.filter(upid=0)
    # 分配数据
    content = {'data':data}
    return render(request,'citys.html',content)


# 获取城市信息
def get_city(request):
    # 获取请求的参数
    cid = request.GET.get('cid')
    # 根据请求的参数,查询对应的城市数据
    # .values将对象抓换成为字典
    # 而整个查询结果是一个查询集
    # 在用list转换成为list格式
    data = list(Citys.objects.filter(upid=cid).values())
    # selet * from citys where upid=15
    # 默认只解析字典数据,其他数据不行,
    # 对象无法进行json的序列化
    # 返回json数据{} [{},{}]
    return JsonResponse(data, safe=False)

