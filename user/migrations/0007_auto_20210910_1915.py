# Generated by Django 3.1.5 on 2021-09-10 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_photos_quota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photos_quota',
            field=models.SmallIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='userphoto',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avatar_photos', to=settings.AUTH_USER_MODEL),
        ),
    ]
