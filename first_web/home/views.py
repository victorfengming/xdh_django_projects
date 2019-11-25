from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from . models import Users,Stu,StuInfo,ClassInfo
# Create your views here.

# 创建一个试图函数,输出Helloween
def index(request):
    return render(request,'abc/b.html')
    # 在试图函数中进行响应
    # return HttpResponse('试图函数执行的结果')


def demo(request):
    # 查询集方法
    """
    all()
    filter()
    exclude()
    order_by()
    values()：一个对象构成一个字典，然后构成一个列表返回
    """
    # 要是查询不到符合条件的结果会返回一个空的查询集
    data = Users.objects.all()
    data2 = Users.objects.filter(sex=0)
    data3 = Users.objects.exclude(username='zhangsan')
    data4 = Users.objects.order_by('id')
    data5 = Users.objects.values()
    # data6 = models.Users.objects.all().filter(sex=0).exclude(username='zhangsan').order_by('id').values()
    # print('-'*60)
    # print(data)
    # print('-'*60)
    # print(data2)
    # print('-'*60)
    # print(data3)
    # print('-'*60)
    # print(data4)
    # print('-'*60)
    # print(data5)
    # print('-'*60)
    # print(data6)
    # print('-'*60)
    '''
    # 返回单个值的方法 -get 只能返回一个结果
    get如果查询不到符合条件的数据 则抛出异常 
    DoesNotExist at /demo 
    Users matching query does not exist.
    get 如果查询到多条数据,还是要抛出异常
    MultipleObjectsReturned at /demo/
    get() returned more than one Users -- it returned 128!
    '''
    data7 = Users.objects.get(age=20)
    print('-'*60)
    print(data7)
    print('-'*60)
    return HttpResponse("模型查询")


# 创建视图函数 演示一对一模型关系的操作
def onetoone(request):

    # # 添加
    # # 创建学员信息
    # ob = Stu(sname='李四',age=24)
    # ob.save()
    # # 添加学员详情信息
    # obi = StuInfo()
    # obi.jiguan = "山西"
    # obi.xueli = '大专'
    # # 注意在给外键添加数据时,
    # # 只能选择对象,不能设为对象的id
    # obi.uid = ob
    # obi.save()
    #
    # # 查询
    # ob = Stu.objects.first()
    # print(ob.sname)
    # # 与之关联的模型类全小写就可以了
    # # ,另一个对象就出来了
    # print(ob.stuinfo.xueli)
    # # 通过学员 获取学员详情对象
    # print(ob.stuinfo.jiguan)
    #
    # # 通过学员详情,获取学员信息
    # ob = StuInfo.objects.last()
    # print(ob.jiguan)
    # print(ob.uid)
    # print(ob.uid.sname)
    # print(ob.uid.age)
    # # 有外键的一方使用外键
    # # 没有外键的一方,使用类名小写
    #
    # # 删除
    # # 删除一个表中的记录,应该同步都删除
    # ob = StuInfo.objects.last()
    # ob.delete()

    return HttpResponse('演示 一对一模型关系的操作')


# 一对多的操作
def onetomore(request):
    # # 添加
    # # 创建班级
    # ob = ClassInfo(cname='python17',code=707)
    # ob.save()
    #
    # # 创建学员
    # sob = Stu(sname='王五',age=23,cid=ob)
    # sob.save()

    # # 查询
    # # 通过班级,获取当前班级的所有学员
    # ob = ClassInfo.objects.first()
    # print(ob.cname)
    # # ob是当前这个班级
    # print(ob.stu_set.all())
    # # 注意 预支关联的模型类名 小写 _set.查询方法
    # # 这里的stu_set是与其相关联的表名加_加set固定写法

    # 通过学员,获取当前学员所在班级
    ob = Stu.objects.last()
    print(ob.sname)
    print(ob.cid.sname)


    return HttpResponse('一对多的操作')