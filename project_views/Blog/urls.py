from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_blog, name='blog')
    path('blog_temp', views.blog_temp)
]

