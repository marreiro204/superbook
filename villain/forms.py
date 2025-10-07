from django import forms
from .models import Villains

class VillainForm(forms.ModelForm):
    class Meta:
        model = Villains
        fields = ['codinome',  'poder_principal', 'cidade', 'historia', 'foto']
