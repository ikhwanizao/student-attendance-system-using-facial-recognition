# Generated by Django 3.2.10 on 2022-06-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0004_alter_student_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='semester',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
