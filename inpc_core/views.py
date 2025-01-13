from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import GroupsProduits, Regions, PointsDeVentes, Produits, Prix
from .forms import (GroupsProduitsForm, RegionsForm, PointsDeVentesForm, 
                    ProduitsForm, PrixForm)
import pandas as pd
import numpy as np
from django.contrib import messages
from django.views.generic import FormView
from .forms import ExcelImportForm

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Vues pour GroupsProduits
class GroupsProduitsCreateView(CreateView):
    model = GroupsProduits
    form_class = GroupsProduitsForm
    template_name = 'inpc_core/groupesproduits_form.html'
    success_url = reverse_lazy('groupesproduits_list')

class GroupsProduitsUpdateView(UpdateView):
    model = GroupsProduits
    form_class = GroupsProduitsForm
    template_name = 'inpc_core/groupesproduits_form.html'
    success_url = reverse_lazy('groupesproduits_list')

class GroupsProduitsDeleteView(DeleteView):
    model = GroupsProduits
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('groupesproduits_list')

# Vues pour Regions
class RegionsCreateView(CreateView):
    model = Regions
    form_class = RegionsForm
    template_name = 'inpc_core/regions_form.html'
    success_url = reverse_lazy('regions_list')

class RegionsUpdateView(UpdateView):
    model = Regions
    form_class = RegionsForm
    template_name = 'inpc_core/regions_form.html'
    success_url = reverse_lazy('regions_list')

class RegionsDeleteView(DeleteView):
    model = Regions
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('regions_list')

# Vues pour PointsDeVentes
class PointsDeVentesCreateView(CreateView):
    model = PointsDeVentes
    form_class = PointsDeVentesForm
    template_name = 'inpc_core/pointsdeventes_form.html'
    success_url = reverse_lazy('pointsdeventes_list')

class PointsDeVentesUpdateView(UpdateView):
    model = PointsDeVentes
    form_class = PointsDeVentesForm
    template_name = 'inpc_core/pointsdeventes_form.html'
    success_url = reverse_lazy('pointsdeventes_list')

class PointsDeVentesDeleteView(DeleteView):
    model = PointsDeVentes
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('pointsdeventes_list')

# Vues pour Produits
class ProduitsCreateView(CreateView):
    model = Produits
    form_class = ProduitsForm
    template_name = 'inpc_core/produits_form.html'
    success_url = reverse_lazy('produits_list')

class ProduitsUpdateView(UpdateView):
    model = Produits
    form_class = ProduitsForm
    template_name = 'inpc_core/produits_form.html'
    success_url = reverse_lazy('produits_list')

class ProduitsDeleteView(DeleteView):
    model = Produits
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('produits_list')

# Vues pour Prix
class PrixCreateView(CreateView):
    model = Prix
    form_class = PrixForm
    template_name = 'inpc_core/prix_form.html'
    success_url = reverse_lazy('prix_list')

class PrixUpdateView(UpdateView):
    model = Prix
    form_class = PrixForm
    template_name = 'inpc_core/prix_form.html'
    success_url = reverse_lazy('prix_list')

class PrixDeleteView(DeleteView):
    model = Prix
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('prix_list')

    
# Vues génériques pour chaque modèle
class GroupsProduitsListView(ListView):
    model = GroupsProduits
    template_name = 'inpc_core/groupesproduits_list.html'

class GroupsProduitsCreateView(CreateView):
    model = GroupsProduits
    form_class = GroupsProduitsForm
    template_name = 'inpc_core/groupesproduits_form.html'
    success_url = reverse_lazy('groupesproduits_list')

class RegionsListView(ListView):
    model = Regions
    template_name = 'inpc_core/regions_list.html'

class PointsDeVentesListView(ListView):
    model = PointsDeVentes
    template_name = 'inpc_core/pointsdeventes_list.html'

class ProduitsListView(ListView):
    model = Produits
    template_name = 'inpc_core/produits_list.html'

class PrixListView(ListView):
    model = Prix
    template_name = 'inpc_core/prix_list.html'


def home(request):
    return render(request, 'inpc_core/home.html')

    
# Fonction de calcul de l'INPC
def calculer_inpc(request):
    # Récupérer tous les prix
    prix_queryset = Prix.objects.all()
    
    # Convertir le queryset en DataFrame pandas
    prix_data = list(prix_queryset.values(
        'produit__nom_produit', 
        'produit__groupe_produit__nom_group',
        'produit__ponderation', 
        'prix', 
        'annee', 
        'mois'
    ))
    
    df = pd.DataFrame(prix_data)
    
    # Convertir les colonnes prix et ponderation en float
    df['prix'] = df['prix'].astype(float)
    df['produit__ponderation'] = df['produit__ponderation'].astype(float)
    
    # Grouper par année, mois et groupe de produits
    grouped = df.groupby(['annee', 'mois', 'produit__groupe_produit__nom_group'])
    
    # Calculer l'INPC par groupe de produits
    inpc_par_groupe = grouped.apply(lambda x: np.average(
        x['prix'], 
        weights=x['produit__ponderation']
    )).reset_index()
    
    # Renommer les colonnes pour plus de clarté
    inpc_par_groupe.columns = ['Année', 'Mois', 'Groupe', 'INPC']
    
    # Calculer l'INPC global
    inpc_global = inpc_par_groupe.groupby(['Année', 'Mois'])['INPC'].mean()
    
    context = {
        'inpc_par_groupe': inpc_par_groupe.to_dict('records'),
        'inpc_global': inpc_global.to_dict()
    }
    
    return render(request, 'inpc_core/calculer_inpc.html', context)




class ExcelImportView(FormView):
    template_name = 'inpc_core/excel_import.html'
    form_class = ExcelImportForm
    success_url = '/import/'

    def form_valid(self, form):
        excel_file = form.cleaned_data['excel_file']
        
        try:
            # Lire le fichier Excel
            df = pd.read_excel(excel_file)
            
            # Importer les données selon le type de fichier
            file_type = form.cleaned_data['file_type']
            
            if file_type == 'groupes_produits':
                self.import_groupes_produits(df)
            elif file_type == 'regions':
                self.import_regions(df)
            elif file_type == 'points_vente':
                self.import_points_vente(df)
            elif file_type == 'produits':
                self.import_produits(df)
            elif file_type == 'prix':
                self.import_prix(df)
            
            messages.success(self.request, 'Importation réussie !')
        except Exception as e:
            messages.error(self.request, f'Erreur lors de l\'importation : {str(e)}')
        
        return super().form_valid(form)

    def import_groupes_produits(self, df):
        for _, row in df.iterrows():
            GroupsProduits.objects.get_or_create(
                nom_group=row['nom_group']
            )

    def import_regions(self, df):
        for _, row in df.iterrows():
            Regions.objects.get_or_create(
                nom_region=row['nom_region']
            )

    def import_points_vente(self, df):
        for _, row in df.iterrows():
            region = Regions.objects.get(nom_region=row['region'])
            PointsDeVentes.objects.get_or_create(
                nom_point=row['nom_point'],
                region=region,
                longitude=row.get('longitude'),
                latitude=row.get('latitude')
            )

    def import_produits(self, df):
        for _, row in df.iterrows():
            groupe = GroupsProduits.objects.get(nom_group=row['groupe_produit'])
            Produits.objects.get_or_create(
                nom_produit=row['nom_produit'],
                groupe_produit=groupe,
                ponderation=row['ponderation']
            )

    def import_prix(self, df):
        for _, row in df.iterrows():
            produit = Produits.objects.get(nom_produit=row['produit'])
            points_vente = PointsDeVentes.objects.filter(
                nom_point__in=row['points_de_vente'].split(',')
            )
            
            prix = Prix.objects.create(
                produit=produit,
                prix=row['prix'],
                annee=row['annee'],
                mois=row['mois']
            )
            prix.points_de_vente.set(points_vente)