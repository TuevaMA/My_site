from django import forms

class MyForm(forms.Form):  # добавила Туева
    name = forms.CharField(label='Твое имя', max_length=50)
    age = forms.IntegerField(label='Возраст')
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'foto' )
