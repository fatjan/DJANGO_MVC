# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db.models import CharField, TextField
from django.db import models as models

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=255, default='')
    deskripsi = models.TextField(max_length=10000, default='')
    images = models.ImageField(upload_to="Media/img")
    komentar = models.IntegerField(default=0)
    waktu_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.judul 
