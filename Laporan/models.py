from django.db import models
from Transaksi.models import Transaksi

# Model for Mutasi
class Mutasi(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.DateTimeField(auto_now_add=True)  # Tanggal mutasi dibuat
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)

    def __str__(self):
        # Mengambil informasi dari transaksi terkait
        tanggal_transaksi = self.transaksi.tanggal.strftime('%Y-%m-%d')
        jenis = self.transaksi.jenis_transaksi
        # kategori = f"{self.transaksi.kat} - {self.transaksi.kategori_pemasukan}"
        jumlah = self.transaksi.jumlah

        # Mengembalikan string yang berisi detail mutasi dari transaksi
        return f"Mutasi pada {tanggal_transaksi} - {jenis} - Jenis Pemasukan Sebagai {self.transaksi.kategori_pemasukan} - Jenis Keluaran Sebagai {self.transaksi.kategori_pengeluaran}- Rp {jumlah}"


