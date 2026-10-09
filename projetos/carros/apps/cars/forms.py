
from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

"""
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            return self.add_error('price', 'Valor não pode ser menor que zero')
        return price
"""