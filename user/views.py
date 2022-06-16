from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from user.models import UserModel
from user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = UserModel
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = UserModel.objects.all()
