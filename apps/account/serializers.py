from django.contrib.auth.models import Group
from rest_framework import serializers

from apps.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']