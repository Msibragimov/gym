from rest_framework import serializers
from rest_framework import serializers

from apps.config.models import DataDate, DataTypes, UserData


class SpesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataDate
        fields = ['date', 'value']     
        

class MetricsDataPointSerializer(serializers.ModelSerializer):
    x = SpesDataSerializer()
    y = SpesDataSerializer()

    class Meta:
        model = DataTypes
        fields = ['x_data_type', 'y_data_type', 'x', 'y'] 
        

class DataSerializer(serializers.ModelSerializer):
    data = MetricsDataPointSerializer()

    class Meta:
        model = UserData
        fields = ['user', 'data']

    def create(self, validated_data):
        data_type = DataTypes.objects.create(**validated_data)
        return data_type

    def to_representation(self, data):
        representation = super(DataSerializer, self).to_representation(data)
        return representation