from django.db import models
from utils.base_model import BaseModel


class TagModel(BaseModel):
    description = models.CharField(max_length=100)
    user = models.ForeignKey('user.UserModel', related_name='user_tags', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
