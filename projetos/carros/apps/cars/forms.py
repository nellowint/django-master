
from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Car
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            self.add_error('price', 'Valor não pode ser menor que zero')

        return price