# Generated by Django 5.1.1 on 2024-10-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal', models.DateField()),
                ('jenis_transaksi', models.CharField(choices=[('PEMASUKAN', 'Pemasukan'), ('PENGELUARAN', 'Pengeluaran')], max_length=20)),
                ('kategori_pemasukan', models.CharField(blank=True, choices=[('SPP', 'Pembayaran SPP'), ('UANG_PANGKAL', 'Pembayaran Uang Pangkal'), ('HIBAH', 'Hibah'), ('LAINNYA', 'Pemasukan Lainnya')], max_length=20, null=True)),
                ('kategori_pengeluaran', models.CharField(blank=True, choices=[('OPERASIONAL', 'Biaya Operasional'), ('ADMINISTRASI', 'Biaya Administrasi'), ('GAJI_KARYAWAN', 'Gaji Karyawan'), ('LAINNYA', 'Pengeluaran Lainnya')], max_length=20, null=True)),
                ('jumlah', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
