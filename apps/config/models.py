from django.utils import timezone
from django.db import models

from apps.account.models import Account


CHOICES =[     
    ("AVG_HEARTBEAT", 'avg_heartbeat'),
    ("CALORIES_CONSUMED", 'calories_consumed'),
    ("SLEEP_HOURS", 'sleep_hours'),
    ("MORNING_PULSE", 'morning_pulse')
]


class DataDate(models.Model):
    date = models.DateField(default=timezone.now)
    value = models.FloatField()   


class DataTypes(models.Model):
    x_data_type = models.CharField(max_length=50, choices=CHOICES)
    y_data_type = models.CharField(max_length=50, choices=CHOICES)
    x = models.ForeignKey(DataDate, related_name='x_data', null=True, on_delete=models.CASCADE)
    y = models.ForeignKey(DataDate, related_name='y_data', null=True, on_delete=models.CASCADE)


class UserData(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    data = models.ForeignKey(DataTypes, on_delete=models.CASCADE, null=True)
