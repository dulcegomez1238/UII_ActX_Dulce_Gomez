from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        # Incluir todos los campos
        fields = '__all__'
        
        # Etiquetas personalizadas
        labels = {
            'id_empleado': 'ID Empleado',
            'nombre': 'Nombre Completo',
            'edad': 'Edad',
            'puestoAsignado': 'Puesto Asignado',
            'sexo': 'Sexo',
            'horario': 'Horario',
            'telefono': 'Teléfono',
            'tipoProducto': 'Tipo de Producto',
            'cantidad': 'Cantidad',
            'id_ventas': 'ID Ventas',
        }
        
        # Aplicar estilos de Bootstrap 
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'min': 18}),
            'puestoAsignado': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoProducto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'id_ventas': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }