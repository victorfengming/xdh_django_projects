from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from django.shortcuts import render




def index(request):

    return HttpResponse('helloworld')

def tmp_demo(request):
    # 分配数据
    content = {
        'var':"I love you",
        'arr':['aa','bb','btb','xcc','3bb'],
        'con':"<h1>知乎</h1>",
    }
    return render(request,'tmp/1.html',content)