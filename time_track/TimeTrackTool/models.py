from django.db import models

# Create your models here.
class Task(models.Model):

    #作業中フラグ用定数
    WORKING = 1
    NOT_WORKING = 0


    # 項番
    Number = models.IntegerField()
    # タスク名
    Task = models.CharField(max_length=50)
    # 作業開始時間
    TimeStart = models.TimeField()
    # 作業終了時間
    TimeEnd = models.TimeField()
    # 作業中判定フラグ
    OnWorkFlag = models.IntegerField()