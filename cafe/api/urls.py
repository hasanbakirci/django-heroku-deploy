from django.urls import path
from cafe.api import views as api_views

urlpatterns = [
    path('urunler/',api_views.UrunListCreateAPIView.as_view(),name='urun-listesi'),
    path('urunler/<int:pk>',api_views.UrunDetailAPIView.as_view(),name='urun-bilgileri'),

    path('siparisler/',api_views.SiparisListCreateAPIView.as_view(),name='siparis-listesi'),
    path('siparisler/<int:pk>',api_views.SiparisDetailAPIView.as_view(),name='siparis-bilgileri'),
]