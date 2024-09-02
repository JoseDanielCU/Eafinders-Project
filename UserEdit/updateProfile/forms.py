from django import forms
from .models import UserRecords

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UserRecords
        fields = ['username', 'description']
