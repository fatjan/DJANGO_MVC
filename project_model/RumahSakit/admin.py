from django.contrib import admin
from .models import Dokter, Pasien, Resep, Obat

# Register your models here.
my_rumah_sakit = [Dokter, Pasien, Resep, Obat]
admin.site.register(my_rumah_sakit)