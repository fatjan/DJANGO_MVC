from django.db import models

from django.db.models import CharField
from django.db.models import TextField

from django.db import models as models

from django.utils import timezone

# Create your models here.
class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=255) 
    no_telepon = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=255)
    nomor_absen = models.CharField(max_length=25)
    nilai_rata_rata = models.IntegerField(max_length=255)
    def __str__(self):
        return self.nama_lengkap

class MataPelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=255)
    jadwal_dimulai = models.DateTimeField(default=timezone.now)
    jadwal_berakhir = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=255)
    no_telepon = models.CharField(max_length=255)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE) 
    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=255)
    banyak_soal = models.IntegerField(max_length=25)
    bobot_nilai = models.IntegerField(max_length=25)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_challenge

class LiveCode(models.Model):
    nama_live_code = models.CharField(max_length=255)
    banyak_soal = models.IntegerField(max_length=25)
    bobot_nilai = models.IntegerField(max_length=25)
    tanggal_pelaksanaan = models.DateTimeField(default=timezone.now)
    mata_pelajaran = models.ForeignKey(MataPelajaran, on_delete=models.CASCADE)
    def __str__(self):
        return self.nama_live_code
