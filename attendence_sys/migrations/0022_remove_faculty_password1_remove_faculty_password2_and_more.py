# Generated by Django 4.0.5 on 2022-06-28 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0021_alter_faculty_password1_alter_faculty_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='username',
        ),
    ]
