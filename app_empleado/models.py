from django.db import models

# Definición de opciones para el campo 'sexo'
SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
)

class Empleado(models.Model):
    # CLAVE PRIMARIA (CRÍTICA)
    id_empleado = models.AutoField(primary_key=True)
    
    # Campos de la tabla 'empleado' (con defaults)
    nombre = models.CharField(max_length=100, default='N/A')
    edad = models.IntegerField(default=18)
    puestoAsignado = models.CharField(max_length=50, default='Asistente')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='O')
    horario = models.CharField(max_length=50, default='9:00 - 17:00')
    telefono = models.CharField(max_length=15, default='000-000-0000')
    tipoProducto = models.CharField(max_length=100, default='General')
    cantidad = models.IntegerField(default=0)
    id_ventas = models.IntegerField(default=1)

    # Método para representación legible en el Admin
    def __str__(self):
        return f"Empleado: {self.nombre} ({self.puestoAsignado})"