from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True) # Usamos AutoField para id_cliente
    nombre = models.CharField(max_length=100, help_text="Nombre del cliente")
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True) # Usamos AutoField para id_mascota
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100, help_text="Nombre de la mascota")
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, blank=True, null=True)
    fecha_nac = models.DateField(blank=True, null=True)
    foto_mascota = models.ImageField(upload_to='img_mascotas/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Dueño: {self.cliente.nombre}"

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"