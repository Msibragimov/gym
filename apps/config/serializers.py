from rest_framework import serializers
from pydantic import root_validator

from apps.config import models


class SpesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MetricsData
        fields = ['date', 'value']


class MetricsDataPointSerializer(serializers.ModelSerializer):
    x_data_type = serializers.ChoiceField(choices=models.CHOICES)
    y_data_type = serializers.ChoiceField(choices=models.CHOICES)
    x = SpesDataSerializer(many=True)
    y = SpesDataSerializer(many=True)

    class Meta:
        model = models.MetricsData
        fields = ['x_data_type', 'y_data_type', 'x', 'y']
    
    @root_validator(pre=True)
    def create(self, validated_data):
        x_data_type, y_data_type = validated_data.get('x_data_type'), validated_data.get('y_data_type')
        assert x_data_type != y_data_type, 'x_data_type and y_data_type MUST be different'
        x_values, y_values = validated_data.get('x'), validated_data.get('y')
        assert len(x_values) == len(y_values), 'x and y lengths mismatch'
        return validated_data

    
class CalculationPayload(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    data = MetricsDataPointSerializer()

    class Meta:
        model = models.UserData
        fields = ['user_id', 'data']


class CorrelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Correlation
        fields = ['value', 'p_value']


class CorrelationPayload(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    x_data_type = serializers.ChoiceField(choices=models.CHOICES)
    y_data_type = serializers.ChoiceField(choices=models.CHOICES)
    correlation = CorrelationSerializer()

    class Meta:
        model = models.Correlation
        fields = ['user_id', 'x_data_type', 'y_data_type', 'correlation']


    # def create(self, validated_data):
    #     for object in validated_data['data']['x']:
    #         if models.UserData.objects.filter(
    #             user_id=validated_data['user_id'],
    #             data_type=validated_data['data']['x_data_type'],
    #             date=object['date']):
    #                 models.UserData.objects.filter(
    #                     user_id=validated_data['user_id'],
    #                     data_type=validated_data['data']['x_data_type'],
    #                     date=object['date']).update(value=object['value'])
    #         else:
    #             models.UserData.objects.create(
    #                             user_id=validated_data['user_id'],
    #                             data_type=validated_data['data']['x_data_type'],
    #                             date=object['date'],
    #                             value=object['value'])

    #     for object in validated_data['data']['y']:
    #         if models.UserData.objects.filter(
    #                             user_id=validated_data['user_id'],
    #                             data_type=validated_data['data']['y_data_type'],
    #                             date=object['date']
    #         ):
    #             models.UserData.objects.filter(
    #                             user_id=validated_data['user_id'],
    #                             data_type=validated_data['data']['y_data_type'],
    #                             date=object['date']).update(value=object['value'])
    #         else:
    #             models.UserData.objects.create(
    #                             user_id=validated_data['user_id'],
    #                             data_type=validated_data['data']['y_data_type'],
    #                             date=object['date'],
    #                             value=object['value'])

    #     return validated_data