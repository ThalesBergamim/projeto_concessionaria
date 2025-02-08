from django import forms
from ecom.models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ("__all__")

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("O preço não pode ser negativo")
        return price

    def clean_year_fabrication(self):
        year_fabrication = self.cleaned_data['year_fabrication']
        if year_fabrication < 1900:
            raise forms.ValidationError("O ano de fabricação não pode ser menor que 1900")
        return year_fabrication

    def clean_year_model(self):
        year_model = self.cleaned_data['year_model']
        if year_model < 1900:
            raise forms.ValidationError("O ano de fabricação não pode ser menor que 1900")
        return year_model

    def clean_plate(self):
        plate = self.cleaned_data['plate']
        if len(plate) != 7:
            raise forms.ValidationError("A placa deve ter 7 caracteres")
        return plate
