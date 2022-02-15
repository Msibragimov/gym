from django.contrib import admin

from apps.config.models import DataDate, DataTypes



admin.site.register(DataTypes)
admin.site.register(DataDate)
