# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def display_mentor(request):
    return render(request, 'Mentor/mentor.html', {})
