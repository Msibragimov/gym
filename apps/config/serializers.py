from rest_framework import serializers
from apps.config import models


class SpesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataDate
        fields = ['date', 'value']


class MetricsDataPointSerializer(serializers.ModelSerializer):
    x_data_type = serializers.ChoiceField(choices=models.CHOICES)
    y_data_type = serializers.ChoiceField(choices=models.CHOICES)
    x = SpesDataSerializer(many=True)
    y = SpesDataSerializer(many=True)

    class Meta:
        model = models.DataType
        fields = ['x_data_type', 'y_data_type', 'x', 'y']


class MainDataSerializer(serializers.ModelSerializer):
    data = MetricsDataPointSerializer()

    class Meta:
        model = models.UserData
        fields = ['user_id', 'data']
    
    def create(self, validated_data):
        for object in validated_data['data']['x']:
            models.UserData.objects.create(
                user_id=validated_data['user_id'],
                x_data_type=validated_data['data']['x_data_type'],
                date=object['date'],
                value=object['value'])

        for object in validated_data['data']['y']:
            models.UserData.objects.create(
                user_id=validated_data['user_id'],
                y_data_type=validated_data['data']['y_data_type'],
                date=object['date'],
                value=object['value'])

        return validated_data
