# Generated by Django 3.2 on 2021-05-23 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('udemy', '0006_auto_20210523_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='learners',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classroommodules',
            name='learners',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classesmodules', to=settings.AUTH_USER_MODEL),
        ),
    ]