from django import forms
from .models import Cliente, Mascota

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono', 'email', 'direccion']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['cliente', 'nombre', 'especie', 'raza', 'fecha_nac', 'foto_mascota']
        widgets = {
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}), # Esto hace que el campo de fecha sea un selector de fecha HTML5
        }