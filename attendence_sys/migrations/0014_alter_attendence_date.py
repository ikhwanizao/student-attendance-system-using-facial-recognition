# Generated by Django 3.2.10 on 2022-06-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0013_alter_attendence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
