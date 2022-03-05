from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.config.models import UserData
from apps.config.serializers import CalculationPayload

# Create your views here.

class BaseDataView(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = CalculationPayload

    @action(methods=['get'], detail=False, url_path='me')
    def get_creat(self, request):
        user = UserData.objects.all()
        serializer = self.get_serializer(user, request.user, many=True)
        serializer.save()
        return Response(serializer.data)