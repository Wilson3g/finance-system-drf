from django.db import models
from utils.base_model import BaseModel


class TagModel(BaseModel):
    """
    Stores a single tag entry, related to :model:`user.UserModel`.

    """
    description = models.CharField(max_length=100)
    user = models.ForeignKey('user.UserModel', related_name='user_tags', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self) -> str:
        """
        Show the name of tag in the class instance

        """
        return self.description