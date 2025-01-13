from django import forms
from .models import (
    ProductType, Product, Wilaya, Moughataa, Commune, 
    PointOfSale, ProductPrice, Cart, CartProduct
)



class ExcelImportForm(forms.Form):
    MODEL_CHOICES = [
        ('product_type', 'Types de Produits'),
        ('product', 'Produits'),
        ('wilaya', 'Wilayas'),
        ('moughataa', 'Moughataa'),
        ('commune', 'Communes'),
        ('point_of_sale', 'Points de Vente'),
        ('product_price', 'Prix des Produits'),
        ('cart', 'Paniers'),
        ('cart_product', 'Produits des Paniers'),
    ]
    
    file = forms.FileField(
        label='Sélectionner un fichier Excel',
        help_text='Formats acceptés: .xlsx, .xls',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )
    
    model_type = forms.ChoiceField(
        label='Type de Données',
        choices=MODEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['code', 'label', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'unit_measure', 'product_type']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class WilayaForm(forms.ModelForm):
    class Meta:
        model = Wilaya
        fields = ['code', 'name']

class MoughataaForm(forms.ModelForm):
    class Meta:
        model = Moughataa
        fields = ['code', 'label', 'wilaya']

class CommuneForm(forms.ModelForm):
    class Meta:
        model = Commune
        fields = ['code', 'name', 'moughataa']

class PointOfSaleForm(forms.ModelForm):
    class Meta:
        model = PointOfSale
        fields = ['code', 'type', 'gps_lat', 'gps_lon', 'commune']
        widgets = {
            'gps_lat': forms.NumberInput(attrs={'step': '0.000001'}),
            'gps_lon': forms.NumberInput(attrs={'step': '0.000001'}),
        }

class ProductPriceForm(forms.ModelForm):
    class Meta:
        model = ProductPrice
        fields = ['value', 'date_from', 'date_to', 'product', 'point_of_sale']
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['code', 'name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class CartProductForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = ['cart', 'product', 'weighting', 'date_from', 'date_to']
        widgets = {
            'date_from': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
            'weighting': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '100'})
        }