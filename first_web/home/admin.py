from django.contrib import admin



# Register your models here.
# 这个后台可NB坏了,但是不建议初学者这样用,因为你不知道他的实现原理

class UsersAdmin(admin.ModelAdmin):
    # 要展示的字段
    list_display = ('id', 'username', 'age', 'sex', 'email', 'addtime')

    # 指定可编辑字段
    list_editable = ['username', 'age','email']

    # 设置每页显示多少条数据
    list_per_page = 10

    # ordering 设置默认排序字段,符号表示降序排序
    ordering = ('-id',)

    # 过滤器(搜索)
    list_filter = ('username','age','email')

    # 搜索字段
    search_fields = ('username','age','email')
    # select * from users where username like '%ab%' or age like '%ab%' or email like '%ab%'

    # # 详细的时间分层筛选
    date_hierarchy = 'addtime'
