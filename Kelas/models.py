from django.db import models

# Create your models here.
class Kelas(models.Model):
    id = models.AutoField(primary_key=True)
    nama_kelas = models.CharField(max_length=20, unique=True)
    wali_kelas = models.CharField(max_length=100)

    def __str__(self):
        return f"Kelas: {self.nama_kelas} - Wali Kelas: {self.wali_kelas}"