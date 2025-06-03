from rest_framework import viewsets

from . import serializers
from taskflow.apps.accounts.models import UserAccount
from taskflow.core.views.mixins.soft_delete_mixin import SoftDeleteMixin


class UserAccountView(SoftDeleteMixin, viewsets.ModelViewSet):

    lookup_field = 'uuid'

    serializer_class = serializers.UserAccountSerializer
    queryset = UserAccount.objects.filter(is_active=True)

    class Meta:
        model = UserAccount
