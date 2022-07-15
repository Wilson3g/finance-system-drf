# Generated by Django 4.0.5 on 2022-06-27 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('description', models.CharField(help_text='Description of the account', max_length=150)),
                ('value', models.FloatField(help_text='Total value of the account', max_length=10)),
                ('status', models.BooleanField(default=False, help_text='Currently account status (paid=True or not paid=False)')),
                ('type', models.CharField(choices=[('PAY', 'to_pay'), ('REC', 'to_receive')], default='PAY', help_text='Type of the account', max_length=3)),
                ('tags', models.ManyToManyField(help_text='Reference of the tag model', related_name='account_tag', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(help_text='Reference of the user model', on_delete=django.db.models.deletion.CASCADE, related_name='user_account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'account',
                'verbose_name_plural': 'accounts',
                'db_table': 'account',
            },
        ),
    ]