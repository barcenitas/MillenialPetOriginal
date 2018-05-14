from django.db import models
from django.utils import timezone
# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=150)
    user=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=50)
    correo=models.EmailField(max_length=50)
    def __str__(self):
        return self.user

class Cita(models.Model):
    #NUM_PAQUETE_CHOICES=('1','2','3')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    hora_inicio= models.DateTimeField(default=timezone.now)
    hora_fin=models.DateTimeField()
    #num_paquete=models.CharField(max_length=3, choices=NUM_PAQUETE_CHOICES)
    num_paquete=models.SmallIntegerField()
class Producto(models.Model):
    nombre= models.CharField(max_length=100)
    precio= models.DecimalField(max_digits=10,decimal_places=4)
    cantidad= models.IntegerField()
    imagen= models.ImageField(verbose_name="Imagen",upload_to="ImgPlanes")
    descripcion=models.TextField()


class Lista(models.Model):
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad= models.PositiveIntegerField()
    subtotal= models.DecimalField(max_digits=15,decimal_places=4)

class Lista_cliente(models.Model):
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    lista= models.ForeignKey(Lista,on_delete=models.CASCADE)
    total= models.DecimalField(max_digits=15,decimal_places=4)

