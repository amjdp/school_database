# Generated by Django 4.1.2 on 2022-10-21 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeacherLogin',
        ),
    ]