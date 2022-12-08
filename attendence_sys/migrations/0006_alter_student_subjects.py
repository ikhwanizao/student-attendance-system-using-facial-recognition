# Generated by Django 3.2.10 on 2022-06-08 08:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('attendence_sys', '0005_attendence_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Pengurusan Projek', 'Pengurusan Projek'), ('Pengurusan Perhubungan Pelanggan', 'Pengurusan Perhubungan Pelanggan'), ('Sistem Bantuan Keputusan', 'Sistem Bantuan Keputusan'), ('English for Higher Education', 'English for Higher Education'), ('Pengajian Islam', 'Pengajian Islam'), ('Pengajian Moral', 'Pengajian Moral'), ('Kenegaraan dan Pembangunan Mutakhir Malaysia', 'Kenegaraan dan Pembangunan Mutakhir Malaysia'), ('Prinsip Teknologi Maklumat', 'Prinsip Teknologi Maklumat'), ('Pengaturcaraan Komputer', 'Pengaturcaraan Komputer'), ('Struktur Diskrit', 'Struktur Diskrit'), ('Senibina Komputer', 'Senibina Komputer')], max_length=267, null=True),
        ),
    ]
