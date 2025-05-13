from rest_framework import serializers
from taskflow.apps.accounts.models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)

    class Meta:
        model = UserAccount
        exclude = ('id',)
