from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.account.models import Account
from apps.account.permissions import AccountPermission
from apps.account.serializers import AccountSerializer, GroupSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    permission_classes = [AccountPermission]

    @action(methods=['get'], detail=False, url_path='me')
    def get_me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

