# Generated by Django 3.2 on 2021-05-07 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0002_courses_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='content',
            new_name='course_content',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='Title',
            new_name='course_name',
        ),
    ]