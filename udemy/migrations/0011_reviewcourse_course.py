# Generated by Django 3.2 on 2021-05-26 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0010_reviewcourse'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewcourse',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='udemy.courses'),
        ),
    ]
