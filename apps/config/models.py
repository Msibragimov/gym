from django.utils import timezone
from django.db import models

from apps.account.models import Account


CHOICES =[     
    ("avg_heartbeat", 'AVG_HEARTBEAT'),
    ("calories_consumed", 'CALORIES_CONSUMED'),
    ("sleep_hours", 'SLEEP_HOURS'),
    ("morning_pulse", 'MORNING_PULSE')
]


class MetricsData(models.Model):
    data_type = models.CharField(max_length=50, choices=CHOICES)
    date = models.DateField(default=timezone.now)
    value = models.FloatField()


class UserData(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    data = models.ForeignKey(MetricsData, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.data_type} - {self.date} : {self.value}"


class Correlation(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    data_type = models.CharField(max_length=50, choices=CHOICES)
    value = models.DateField(default=timezone.now)
    p_value = models.FloatField()