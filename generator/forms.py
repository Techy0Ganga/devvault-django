from django import forms
from .models import Presets, Stack


class presetForm(forms.ModelForm):
    
    class Meta:
        model = Presets
        fields = "__all__"

        widgets = {
            'created_at' : forms.DateInput(attrs = {'type' : 'date'})
        }

class stackForm(forms.ModelForm):
    
    class Meta:
        model = Stack
        fields = "__all__"
        exclude = ['preset']