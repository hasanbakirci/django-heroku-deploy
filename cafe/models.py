from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Urun(models.Model):
    isim = models.CharField(max_length=150)
    resim = models.TextField(blank=True, null=True)
    boy = models.PositiveIntegerField(
        validators = [MinValueValidator(1),MaxValueValidator(3)],
    )
    aciklama = models.TextField(blank=True, null=True)
    fiyat = models.FloatField()

    def __str__(self):
        return f'{self.isim} - {self.boy} - {self.fiyat}'

class Siparis(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE, related_name='siparisler')
    adet = models.IntegerField()
    toplam_fiyat = models.FloatField()
    olusturma_tarihi = models.DateField(auto_now_add=True)
    guncellenme_tarihi = models.DateField(auto_now=True)

    def __str__(self):
        return f'{str(self.adet)} - {str(self.toplam_fiyat)}'



