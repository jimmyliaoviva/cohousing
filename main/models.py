from django.db import models


# Create your models here.
class house(models.Model):
    hName = models.CharField(max_length=50, null=False)
    hAddress = models.CharField(max_length=50, null=False)
    hClass = models.CharField(max_length=10, null=False)
    hType = models.CharField(max_length=10, null=False, default="")
    hPing = models.PositiveIntegerField(default="")
    hFloor = models.PositiveIntegerField(default="")
    hFloorAll = models.PositiveIntegerField(default="")
    hEle = models.BooleanField(default=True)
    hMoney = models.PositiveIntegerField(default="")
    hAge = models.PositiveIntegerField(default="")
    hPic = models.ImageField(upload_to='media')

def __str__(self):
    return self.hName

class old_distribute_sm(models.Model):
    COUNTY_ID = models.PositiveIntegerField()
    COUNTY = models.CharField(max_length=5)
    TOWN_ID = models.PositiveIntegerField()
    TOWN = models.CharField(max_length=5)
    FLD01 = models.PositiveIntegerField()
    FLD02 = models.FloatField()
    FLD03 = models.PositiveIntegerField()
    FLD04 = models.PositiveIntegerField()
    FLD05 = models.PositiveIntegerField()
    FLD06 = models.PositiveIntegerField()
    INFO_TIME = models.CharField(max_length=5)

class houseHolder(models.Model):
    pic = models.ImageField(upload_to='media')
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    introduction = models.CharField(max_length=100)
    interesting = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)




