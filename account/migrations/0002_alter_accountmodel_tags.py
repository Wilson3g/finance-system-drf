# Generated by Django 4.0.5 on 2022-06-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tagmodel_user'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Reference of the tag model', related_name='account_tag', to='tags.tagmodel'),
        ),
    ]