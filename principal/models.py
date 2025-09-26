from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    url_video = models.URLField()
    duracion = models.CharField(max_length=10)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo