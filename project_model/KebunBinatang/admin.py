from django.contrib import admin
from .models import Hewan, Kandang, Penjaga, Pengunjung
# Register your models here.
my_kebun_binatang = [Hewan, Kandang, Penjaga, Pengunjung]
admin.site.register(my_kebun_binatang)