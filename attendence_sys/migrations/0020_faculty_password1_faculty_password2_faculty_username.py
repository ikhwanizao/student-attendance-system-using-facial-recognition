# Generated by Django 4.0.5 on 2022-06-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0019_auto_20220608_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='password1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='password2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
