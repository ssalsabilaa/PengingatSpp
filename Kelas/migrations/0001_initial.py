# Generated by Django 5.1.1 on 2024-11-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_kelas', models.CharField(max_length=20, unique=True)),
                ('wali_kelas', models.CharField(max_length=100)),
            ],
        ),
    ]
