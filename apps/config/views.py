from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.config.models import DataType, UserData
from apps.config.serializers import MainDataSerializer

# Create your views here.

class BaseDataView(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = MainDataSerializer

    def get_creat(self, request):
        user = UserData.objects.all()
        serializer = self.get_serializer(user, request.user, many=True)
        return Response(serializer.data)