# restaurante/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Reserva

class LoginForm(forms.Form):
    correo = forms.EmailField(max_length=100)
    contraseña = forms.CharField(widget=forms.PasswordInput)

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha', 'hora', 'mesa']

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'password1', 'password2']