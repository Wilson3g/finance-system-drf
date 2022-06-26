from django.urls import path, include
from rest_framework import routers
from user.views import UserViewSet
from tags.views import TagViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]