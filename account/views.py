from django.shortcuts import render
from rest_framework import viewsets
from account.serializers import AccountSerializer
from account.models import AccountModel
from tags.models import TagModel
from rest_framework.decorators import action
from rest_framework.response import Response


class AccountViewSet(viewsets.ModelViewSet):
    """
    Create, Update, Destroy, List and Retrieve accounts.

    """
    serializer_class = AccountSerializer
    model = AccountModel


    def get_queryset(self):
        return AccountModel.objects.filter(user=self.request.user).order_by('-created_at')

    def create(self, request: dict) -> dict:
        """
        Description: Overwrite the default create django method. Create a new account register associate with a user and a tag if it informed.

        Parameters:
            request: data of the request.

        Return:
            Json with message and a status code 201 if the data is created.
            Json with message and a status code 400 if the the tag doesn´t exist.

        """
        body = request.data
        tags_body = body.pop('tags', '')
        account = AccountModel.objects.create(**body, user=self.request.user)

        try:
            account.tags.add(*tags_body)
        except Exception as e:
            print(e)

        return Response({'message': 'created!'}, 201)
