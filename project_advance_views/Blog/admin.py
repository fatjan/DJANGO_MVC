# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Blog
from django.contrib import admin

# Register your models here.
my_model = [Blog]
admin.site.register(my_model)
