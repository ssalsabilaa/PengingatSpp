# Generated by Django 5.1.1 on 2024-10-23 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaksi', '0005_alter_transaksi_jenis_transaksi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='jenis_transaksi',
            field=models.CharField(choices=[('PEMASUKAN', 'Pemasukan'), ('PENGELUARAN', 'Pengeluaran')], max_length=20),
        ),
    ]
