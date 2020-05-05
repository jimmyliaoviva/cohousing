from django.contrib import admin
from main.models import house
from main.models import old_distribute_sm

# Register your models here.

class houseAdmin(admin.ModelAdmin):
    list_display = ('id', 'hName', 'hAddress', 'hClass', 'hType',  'hFloor', 'hFloorAll', 'hEle', 'hMoney')
    list_filter = ('hName', 'hAddress', 'hClass', 'hType', 'hPing', 'hFloor', 'hFloorAll', 'hEle', 'hMoney')
    search_fields = ('hMoney',)
    ordering = ('id',)

class old_distribute_smAdmin(admin.ModelAdmin):
    list_display = ('id','COUNTY_ID','COUNTY','TOWN_ID','TOWN','FLD01','FLD02','FLD03','FLD04','FLD05','FLD06','INFO_TIME')

admin.site.register(house, houseAdmin)
admin.site.register(old_distribute_sm)
