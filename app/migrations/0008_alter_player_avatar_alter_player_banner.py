# Generated by Django 4.1.2 on 2022-12-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_player_banner_player_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='banner',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
