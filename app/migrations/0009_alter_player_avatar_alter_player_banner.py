# Generated by Django 4.1.2 on 2022-12-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_player_avatar_alter_player_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='banner',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
