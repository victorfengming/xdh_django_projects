from django.db import models

# Create your models here.
# 模型的作用,降低程序的耦合性,更换数据库就改个配置文件就行了

class Users(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50)