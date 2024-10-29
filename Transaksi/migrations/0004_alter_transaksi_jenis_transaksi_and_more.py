# Generated by Django 5.1.1 on 2024-10-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transaksi', '0003_remove_transaksi_deskripsi_remove_transaksi_kategori_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='jenis_transaksi',
            field=models.CharField(choices=[('PEMASUKAN', 'Pemasukan'), ('PENGELUARAN', 'Pengeluaran')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='kategori_pemasukan',
            field=models.CharField(blank=True, choices=[('SPP', 'Pembayaran SPP'), ('UANG_PANGKAL', 'Pembayaran Uang Pangkal'), ('HIBAH', 'Hibah'), ('LAINNYA', 'Pemasukan Lainnya')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='kategori_pengeluaran',
            field=models.CharField(blank=True, choices=[('OPERASIONAL', 'Biaya Operasional'), ('ADMINISTRASI', 'Biaya Administrasi'), ('GAJI_KARYAWAN', 'Gaji Karyawan'), ('LAINNYA', 'Pengeluaran Lainnya')], max_length=50, null=True),
        ),
    ]