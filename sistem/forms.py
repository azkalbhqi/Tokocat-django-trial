from django import forms
from .models import Paint

class PaintForm(forms.ModelForm):
    class Meta:
        model = Paint
        fields = ['color', 'price', 'brand_name', 'stock']