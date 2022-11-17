from django.db import models

# Create your models here.
class Bandas(models.Model):
    nombre_banda = models.CharField(max_length= 50)
    productora = models.CharField(max_length= 50)

class Comprador(models.Model):
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email =models.EmailField()


class Lugar(models.Model):
    estadio = models.CharField(max_length= 50)
