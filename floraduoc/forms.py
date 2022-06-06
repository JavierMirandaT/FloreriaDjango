from django import forms
from .models import Flora


class FloraForm(forms.ModelForm):
    class Meta:
        model = Flora
        fields = '__all__'