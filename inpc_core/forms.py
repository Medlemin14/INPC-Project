from django import forms
from .models import GroupsProduits, Regions, PointsDeVentes, Produits, Prix

class GroupsProduitsForm(forms.ModelForm):
    class Meta:
        model = GroupsProduits
        fields = ['nom_group']

class RegionsForm(forms.ModelForm):
    class Meta:
        model = Regions
        fields = ['nom_region']

class PointsDeVentesForm(forms.ModelForm):
    class Meta:
        model = PointsDeVentes
        fields = ['nom_point', 'region', 'longitude', 'latitude']

class ProduitsForm(forms.ModelForm):
    class Meta:
        model = Produits
        fields = ['nom_produit', 'groupe_produit', 'ponderation']

class PrixForm(forms.ModelForm):
    class Meta:
        model = Prix
        fields = ['produit', 'prix', 'annee', 'mois', 'points_de_vente']





class ExcelImportForm(forms.Form):
    FILE_TYPE_CHOICES = [
        ('groupes_produits', 'Groupes de Produits'),
        ('regions', 'Régions'),
        ('points_vente', 'Points de Vente'),
        ('produits', 'Produits'),
        ('prix', 'Prix')
    ]

    excel_file = forms.FileField(label='Fichier Excel')
    file_type = forms.ChoiceField(
        label='Type de Données', 
        choices=FILE_TYPE_CHOICES
    )