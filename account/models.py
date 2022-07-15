from utils.base_model import BaseModel
from django.db import models

class AccountModel(BaseModel):
    """
    Stores a single account register entry, related to :model:`user.UserModel` and :model:`tags.TagModel`.

    """

    TO_PAY = 'PAY'
    TO_RECEIVE = 'REC'
    YEAR_IN_SCHOOL_CHOICES = [
        (TO_PAY, 'to_pay'),
        (TO_RECEIVE, 'to_receive')
    ]

    description = models.CharField(max_length=150, help_text='Description of the account')
    value = models.FloatField(max_length=10, help_text='Total value of the account')
    status = models.BooleanField(default=False, help_text='Currently account status (paid=True or not paid=False)')
    user = models.ForeignKey('user.UserModel', related_name='user_account', on_delete=models.CASCADE, help_text='Reference of the user model')
    tags = models.ManyToManyField('tags.TagModel', related_name='account_tag', help_text='Reference of the tag model', blank=True)
    type = models.CharField(
        max_length=3,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=TO_PAY,
        help_text='Type of the account'
    )

    class Meta:
        db_table = 'account'
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

    def __str__(self) -> str:
        """
        Show the description of the account in the class instance

        """
        return self.description
