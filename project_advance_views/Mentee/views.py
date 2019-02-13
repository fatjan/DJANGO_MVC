# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def display_mentee(request):
    return render(request, 'Mentee/mentee.html', {})