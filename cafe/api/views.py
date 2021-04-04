from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import generics
from cafe.models import Urun,Siparis
from cafe.api.serializers import SiparisSerializer,UrunSerializer

class UrunListCreateAPIView(generics.ListCreateAPIView):
    queryset = Urun.objects.all()
    serializer_class = UrunSerializer
class UrunDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Urun.objects.all()
    serializer_class = UrunSerializer

class SiparisListCreateAPIView(generics.ListCreateAPIView):
    queryset = Siparis.objects.all()
    serializer_class = SiparisSerializer
class SiparisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Siparis.objects.all()
    serializer_class = SiparisSerializer