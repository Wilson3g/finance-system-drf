from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet
from tags.views import TagViewSet
from account.views import AccountViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'account', AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
]