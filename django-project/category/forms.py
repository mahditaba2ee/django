
from django import forms
from .models import ProductModel

class AddProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields = ('name','des','price')