from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
import uuid


class UserManagerModel(BaseUserManager):
    ...


class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    name = models.CharField(max_length=60, null=False, help_text='nome')
    phone = models.CharField(max_length=60, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    objects = UserManagerModel()

    def __str__(self):
        return self.email


class UserRecoveryModel(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_recovery"
