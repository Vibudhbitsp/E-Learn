# Generated by Django 3.2 on 2021-05-07 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('udemy', '0003_auto_20210507_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='modules',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udemy.courses'),
        ),
    ]
