from django.shortcuts import render
from rest_framework import viewsets
from tags.serializers import TagSerializer
from tags.models import TagModel
from rest_framework.response import Response


class TagViewSet(viewsets.ModelViewSet):
    """
    Create, Update, Destroy, List and Retrieve tags.

    """
    serializer_class = TagSerializer
    model = TagModel

    def get_queryset(self):
        return TagModel.objects.filter(user=self.request.user)

    def create(self, request: dict) -> dict:
        """
        Description: Overwrite the default create django method. Create a new tag if it doesn´t exist yet.

        Parameters:
            request: data of the request.

        Return:
            Json with message and a status code 201 if the data is created.
            Json with message and a status code 400 if the data already exists.

        """
        _, created = TagModel.objects.get_or_create(**request.data, user=self.request.user)
        if not created:
            return Response({'message': 'tag already exists!'}, 400)

        return Response({'message': 'created!'}, 201)

    def update(self, request: dict, validated_data=None, pk=None) -> dict:
        """
        Description: Overwrite the default update django method. Update a the description of a existing tag if one doesn´t exist yet.

        Parameters:
            request: data of the request.
            validate_data: data from the form body.
            pk: tag primary key.

        Return:
            Json with message and a status code 200 if the data is updated.
            Json with message and a status code 400 if the data already exists.

        """
        instance = self.get_object()

        if TagModel.objects.filter(**request.data, user=self.request.user).exists():
            return Response({'message': 'tag already exists!'}, 400)

        instance.description = request.data.get('description')
        instance.save()

        return Response({'message': 'updated!'}, 200)
