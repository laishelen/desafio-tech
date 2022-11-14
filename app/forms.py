from django.forms import ModelForm
from app.models import usuarios
from django import forms

# Create the form class.
class usuariosForm(ModelForm):
    class Meta:
        model = usuarios
        fields = ['login', 'password', 'dataNascimento']
