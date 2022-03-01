from django.contrib import admin

from apps.config.models import DataDate, DataType, UserData



admin.site.register(DataDate)
admin.site.register(DataType)
admin.site.register(UserData)