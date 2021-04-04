from rest_framework import serializers
from cafe.models import Urun,Siparis

class UrunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urun
        fields = '__all__'

class SiparisSerializer(serializers.ModelSerializer):
    urun = Urun.isim
    class Meta:
        model = Siparis
        fields = '__all__'
        #exclude = ['toplam_fiyat']