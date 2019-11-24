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
