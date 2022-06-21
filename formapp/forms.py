from tkinter import Widget
from django import forms
from .models import Registration
from django.forms import DateInput, ModelForm
from django.forms.widgets import DateInput


class RegForm(ModelForm):
    class Meta:
        model=Registration
        fields="__all__"
        widgets = {
            'dob': DateInput(attrs={'type': 'date'}),
        }
        # {
        #     'country': countryselectwidget
        
        # }
        