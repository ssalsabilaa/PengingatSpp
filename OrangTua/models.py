from django.db import models

# Create your models here.
class OrangTua(models.Model):
    id = models.AutoField(primary_key=True)
    nama_orangtua = models.CharField(max_length=100)
    pekerjaan = models.CharField(max_length=100, blank=True)
    alamat = models.TextField(blank=True)
    nomor_hp = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nama_orangtua} - {self.nomor_hp}"