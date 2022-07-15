from rest_framework import serializers
from account.models import AccountModel
from tags.serializers import TagSerializer


class AccountSerializer(serializers.ModelSerializer):
    """
    Serialize the account data

    """
    class Meta:
        model = AccountModel
        fields = ('id', 'created_at', 'updated_at', 'description','value','status','type','user','tags',)
        read_only_fields = ('user', 'created_at', 'updated_at', 'status',)
