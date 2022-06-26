from django.shortcuts import render
from rest_framework import viewsets
from tags.serializers import TagSerializer
from tags.models import TagModel
from rest_framework.response import Response


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    model = TagModel

    def get_queryset(self):
        return TagModel.objects.filter(user=self.request.user)

    def create(self, request: dict) -> dict:
        _, created = TagModel.objects.get_or_create(**request.data, user=self.request.user)
        if not created:
            return Response({'message': 'tag already exists!'}, 400)

        return Response({'message': 'created!'}, 201)

    def update(self, request, validated_data=None, pk=None) -> dict:
        instance = self.get_object()

        if TagModel.objects.filter(**request.data, user=self.request.user).exists():
            return Response({'message': 'tag already exists!'}, 400)

        instance.description = request.data.get('description')
        instance.save()

        return Response({'message': 'updated!'}, 200)
