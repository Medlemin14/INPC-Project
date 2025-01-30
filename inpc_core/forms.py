from django import forms
from .models import (
    ProductType, Product, Wilaya, Moughataa, Commune, 
    PointOfSale, ProductPrice, Cart, CartProduct
)



class ExcelImportForm(forms.Form):
    OPERATION_CHOICES = [
        ('import', 'Importer'),
        ('export', 'Exporter'),
    ]

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
    
    operation = forms.ChoiceField(
        label='Type d\'Opération',
        choices=OPERATION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_operation'})
    )
    
    file = forms.FileField(
        label='Sélectionner un fichier Excel',
        help_text='Formats acceptés: .xlsx, .xls',
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )
    
    model_type = forms.ChoiceField(
        label='Type de Données',
        choices=MODEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        operation = cleaned_data.get('operation')
        file = cleaned_data.get('file')
        
        if operation == 'import' and not file:
            raise forms.ValidationError('Un fichier est requis pour l\'importation')
        
        return cleaned_data

class ExcelExportForm(forms.Form):
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
    
    model_type = forms.ChoiceField(
        label='Type de Données à Exporter',
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
        fields = ['value', 'product', 'point_of_sale']

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
        fields = ['cart', 'product', 'weighting']
        widgets = {
            'weighting': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '100'})
        }