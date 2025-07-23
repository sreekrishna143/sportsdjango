# forms.py
from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'image', 'description', 'country']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
