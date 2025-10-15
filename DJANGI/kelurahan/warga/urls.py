from django.urls import path
from .views import WargaListView, WargaDetailView, WargaCreateView, PengaduanListView, PengaduanCreateView

urlpatterns = [
    path('warga', WargaListView.as_view(), name='warga_list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
    path('tambah/', WargaCreateView.as_view(), name='warga_tambah'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan_tambah'),
]