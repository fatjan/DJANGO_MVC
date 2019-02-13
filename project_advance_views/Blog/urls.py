from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_blog, name='blog'),
    path('blog_new/', views.blog_new, name='blog_new'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail')
    

]

