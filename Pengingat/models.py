from django.db import models
from Siswa.models import Siswa
# Create your models here.
class Pengingat(models.Model):
    id = models.AutoField(primary_key=True)
    id_siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    tanggal = models.DateField()

    def __str__(self):
        return f"Pengingat untuk {self.id_siswa.nama} pada {self.tanggal}"