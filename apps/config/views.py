from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.config.models import DataTypes
from apps.config.serializers import DataSerializer

# Create your views here.

class BaseDataView(viewsets.ModelViewSet):
    queryset = DataTypes.objects.all()
    serializer_class = DataSerializer

    @action(methods=['get'], detail=False, url_path='me')
    def get_me(self, request):
        data = DataTypes.objects.all()
        serializer = self.get_serializer(data, request.user, many=True)
        return Response(serializer.data)