from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model=Profesor
        fields=['nombre', 'apellido_pat', 'apellido_mat', 'email', 'telefono']
        labels={
            'nombre':'Nombre',
            'apellido_pat':'Apellido Paterno',
            'apellido_mat':'Apellido Materno',
            'email':'Email',
            'telefono':'Telefono',
        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_pat':forms.TextInput(attrs={'class':'form-control'}),
            'apellido_mat':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
        }