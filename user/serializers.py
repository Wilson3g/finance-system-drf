from rest_framework import serializers
from user.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer the user data

    """
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'name', 'password', 'phone')

        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 6},
            'phone': {'required': False}
        }

    def save(self):
        """
        Create a new user

        """
        password = self.validated_data['password']
        phone = self.validated_data.pop('phone', None)
        u = UserModel(
            name=self.validated_data['name'],
            email=self.validated_data['email'],
            phone=phone
        )
        u.set_password(password)
        u.save()
        return u
