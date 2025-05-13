from rest_framework import viewsets
from taskflow.apps.accounts.models import UserAccount
from taskflow.apps.accounts.serializers.useraccount_serializer import UserAccountSerializer
from taskflow.core.views.mixins.soft_delete_mixin import SoftDeleteMixin


class UserAccountView(SoftDeleteMixin, viewsets.ModelViewSet):

    lookup_field = 'uuid'

    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.filter(is_active=True)

    class Meta:
        model = UserAccount
