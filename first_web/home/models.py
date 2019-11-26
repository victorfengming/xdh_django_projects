from django.db import models


# 城市数据
class Citys(models.Model):
    '''
        # id name   levelupid
          1   北京   1    0
          2   昌平   2    1
    '''
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    upid = models.IntegerField()


    class Meta:
        db_table = 'citys'
