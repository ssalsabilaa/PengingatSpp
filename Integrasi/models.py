from django.db import models

class WhatsApp(models.Model):
    id = models.AutoField(primary_key=True)
    nomor_hp = models.CharField(max_length=15)
    isi_pesan = models.TextField()

    def __str__(self):
        return f"Pesan ke {self.nomor_hp}"
