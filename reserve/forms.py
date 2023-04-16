from django import forms
from .models import ReserveModel


class ReserveForm(forms.ModelForm):
    class Meta:
        model=ReserveModel
        fields='__all__'

