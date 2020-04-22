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


def __str__(self):
    return self.hName
