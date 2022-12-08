# Generated by Django 3.2.10 on 2022-06-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0002_alter_student_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Sunday', 'Sunday')], default='Monday', max_length=15),
        ),
        migrations.AlterField(
            model_name='time',
            name='end',
            field=models.CharField(choices=[('08:00 am', '08:00 am'), ('09:00 am', '09:00 am'), ('10:00 am', '10:00 am'), ('11:00 am', '11:00 am'), ('12:00 pm', '12:00 pm'), ('01:00 pm', '01:00 pm'), ('02:00 pm', '02:00 pm'), ('03:00 pm', '03:00 pm'), ('04:00 pm', '04:00 pm'), ('05:00 pm', '05:00 pm'), ('06:00 pm', '06:00 pm')], default='10:00 pm', max_length=50),
        ),
        migrations.AlterField(
            model_name='time',
            name='start',
            field=models.CharField(choices=[('08:00 am', '08:00 am'), ('09:00 am', '09:00 am'), ('10:00 am', '10:00 am'), ('11:00 am', '11:00 am'), ('12:00 pm', '12:00 pm'), ('01:00 pm', '01:00 pm'), ('02:00 pm', '02:00 pm'), ('03:00 pm', '03:00 pm'), ('04:00 pm', '04:00 pm'), ('05:00 pm', '05:00 pm'), ('06:00 pm', '06:00 pm')], default='08:00 am', max_length=50),
        ),
    ]
