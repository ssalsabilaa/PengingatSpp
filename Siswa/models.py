from django.db import models

class Siswa(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    nis = models.CharField(max_length=20, unique=True)
    kelas = models.CharField(max_length=10)
    nomor_orangtua = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nama} ({self.nis})"
