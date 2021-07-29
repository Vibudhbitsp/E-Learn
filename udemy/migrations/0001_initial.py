# Generated by Django 3.2 on 2021-05-05 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('Course_Tag', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdudemy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('index', models.IntegerField(default=1)),
                ('link', models.URLField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allmodules', to='udemy.courses')),
            ],
        ),
    ]
