from django.db import models

class Transaksi(models.Model):
    TRANSAKSI_CHOICES = [
        ('PEMASUKAN', 'Pemasukan'),
        ('PENGELUARAN', 'Pengeluaran')
    ]

    PEMASUKAN_CHOICES = [
        ('SPP', 'Pembayaran SPP'),
        ('UANG_PANGKAL', 'Pembayaran Uang Pangkal'),
        ('HIBAH', 'Hibah'),
        ('LAINNYA', 'Pemasukan Lainnya')
    ]

    PENGELUARAN_CHOICES = [
        ('OPERASIONAL', 'Biaya Operasional'),
        ('ADMINISTRASI', 'Biaya Administrasi'),
        ('GAJI_KARYAWAN', 'Gaji Karyawan'),
        ('LAINNYA', 'Pengeluaran Lainnya')
    ]

    id = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    jenis_transaksi = models.CharField(max_length=20, choices=TRANSAKSI_CHOICES)
    kategori_pemasukan = models.CharField(max_length=20, choices=PEMASUKAN_CHOICES, blank=True, null=True)
    kategori_pengeluaran = models.CharField(max_length=20, choices=PENGELUARAN_CHOICES, blank=True, null=True)
    jumlah = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        if self.jenis_transaksi == 'PEMASUKAN':
            return f"Pemasukan - {self.kategori_pemasukan} - {self.jumlah}"
        else:
            return f"Pengeluaran - {self.kategori_pengeluaran} - {self.jumlah}"