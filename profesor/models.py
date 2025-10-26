from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=100)
    apellido_pat=models.CharField(max_length=100)
    apellido_mat=models.CharField(max_length=100)
    email=models.EmailField()
    telefono=models.CharField(max_length=12)

    def __str__ (self):
        return self.nombre