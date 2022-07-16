from rest_framework import serializers
from tags.models import TagModel


class TagSerializer(serializers.ModelSerializer):
    """
    Serialize the tag data

    """

    class Meta:
        model = TagModel
        fields = '__all__'
