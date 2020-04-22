from django.contrib import admin
from main.models import house


# Register your models here.

class houseAdmin(admin.ModelAdmin):
    list_display = ('id', 'hName', 'hAddress', 'hClass', 'hType', 'hPing', 'hFloor', 'hFloorAll', 'hEle', 'hMoney')
    list_filter = ('hName', 'hAddress', 'hClass', 'hType', 'hPing', 'hFloor', 'hFloorAll', 'hEle', 'hMoney')
    search_fields = ('hMoney',)
    ordering = ('id',)


admin.site.register(house, houseAdmin)
