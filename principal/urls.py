from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos, name='videos'),
    path('videos/', views.videos, name='videos'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('creditos/', views.creditos, name='creditos'),
    path('agregar-video/', views.agregar_video, name='agregar_video'),
    path('agregar-usuario/', views.agregar_usuario, name='agregar_usuario'),
]