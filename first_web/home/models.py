from django.db import models

# Create your models here.
# 模型的作用,降低程序的耦合性
# 更换数据库就改个配置文件就行了

class Users(models.Model):
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    sex = models.IntegerField()
    addtime = models.DateTimeField(auto_now_add=True)


    # 魔术方法:当对该类对象进行字符串操作时会自动触发
    def __str__(self):
        return self.username

#
# class Stu(models.Model):
#     sid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     age = models.IntegerField(default=20)
#     email = models.CharField(max_length=100,null=True)
    #
    # # 元选项
    # class Meta():
    #     # 指定表明
    #     db_table = 'stus'

# 创建学员模型
class Stu(models.Model):
    sname = models.CharField(max_length=6)
    age = models.IntegerField()

# 创建学员详情模型
class StuInfo(models.Model):
    jiguan = models.CharField(max_length=10)
    xueli = models.CharField(max_length=10)
    # 在用户详情表中，关联用户表，让两个表的数据产生联系
    # 第一个参数：是被关联的模型名称
    # 第二个参数：当user用户表中的一条数据被删除的时候
    # ，与之对应的详情表数据也会被删除,
    # 说白了就是同步记录删除学生了还要啥学生详情啊
    uid = models.OneToOneField(Stu, on_delete=models.CASCADE)
    # 这里在Stu不用引号,要是换了顺序,
    # 就是Stu在下面了,就要加上引号了,不然找不到
    # 因为咱们python并没有类或者函数的欲仙加载,毕竟是脚本语言嘛,还想咋地!
    # 那你还能在类定义之前去实例化对象啊, 你不得先定义在用啊
