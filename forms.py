from django import forms
from .models import Empmodel

class Empforms(forms.ModelForm):
    class Meta:
        model=Empmodel
        fields=["idno","name",'salary']