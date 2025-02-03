from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
)
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import ProtectedError, Q  # Added Q here
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import (
    ProductType, Product, Wilaya, Moughataa, Commune, 
    PointOfSale, ProductPrice, Cart, CartProduct 
)
from .forms import (
    ProductTypeForm, ProductForm, WilayaForm, MoughataaForm, 
    CommuneForm, PointOfSaleForm, ProductPriceForm, 
    CartForm, CartProductForm, ExcelImportForm, ExcelExportForm
)
from .filters import ProductFilter

import logging
logger = logging.getLogger(__name__)

class SafeDeleteView(LoginRequiredMixin, DeleteView):
    def get_related_objects(self):
        """
        Retourne un dictionnaire des objets liés qui seront supprimés en cascade
        À surcharger dans les classes enfants si nécessaire
        """
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_objects = self.get_related_objects()
        context['related_objects'] = related_objects
        context['has_related_objects'] = any(objects for objects in related_objects.values())
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        related_objects = self.get_related_objects()
        logger.info(f"Tentative de suppression de {self.object} - Objets liés: {related_objects}")
        
        try:
            logger.info(f"Suppression de {self.object} et de ses objets liés")
            response = super().delete(request, *args, **kwargs)
            message = "Élément supprimé avec succès"
            if related_objects:
                message += ", ainsi que tous les éléments qui y étaient liés"
            messages.success(request, message)
            return response
        except Exception as e:
            logger.error(f"Erreur lors de la suppression de {self.object}: {str(e)}")
            messages.error(request, "Une erreur s'est produite lors de la suppression.")
            return redirect(self.get_success_url())

# Product Type Views
class ProductTypeListView(LoginRequiredMixin,ListView):
    model = ProductType
    template_name = 'inpc_core/product_type_list.html'
    context_object_name = 'product_types'

class ProductTypeCreateView(LoginRequiredMixin,CreateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'inpc_core/product_type_form.html'
    success_url = reverse_lazy('product_type_list')

class ProductTypeUpdateView(LoginRequiredMixin,UpdateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'inpc_core/product_type_form.html'
    success_url = reverse_lazy('product_type_list')

class ProductTypeDeleteView(SafeDeleteView):
    model = ProductType
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_type_list')

    def get_related_objects(self):
        obj = self.get_object()
        products = list(obj.products.all())
        prices = []
        cart_products = []
        
        for product in products:
            prices.extend(list(product.prices.all()))
            cart_products.extend(list(product.cart_products.all()))
            
        return {
            'Produits': products,
            'Prix': prices,
            'Produits dans les paniers': cart_products
        }

# Product Views
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inpc_core/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return ProductFilter(self.request.GET, queryset=queryset).qs

class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inpc_core/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(LoginRequiredMixin,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inpc_core/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(SafeDeleteView):
    model = Product
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def get_related_objects(self):
        obj = self.get_object()
        return {
            'Prix': obj.prices.all(),
            'Produits dans les paniers': obj.cart_products.all()
        }

# Wilaya Views
class WilayaListView(LoginRequiredMixin,ListView):
    model = Wilaya
    template_name = 'inpc_core/wilaya_list.html'
    context_object_name = 'wilayas'

class WilayaCreateView(LoginRequiredMixin,CreateView):
    model = Wilaya
    form_class = WilayaForm
    template_name = 'inpc_core/wilaya_form.html'
    success_url = reverse_lazy('wilaya_list')

class WilayaUpdateView(LoginRequiredMixin,UpdateView):
    model = Wilaya
    form_class = WilayaForm
    template_name = 'inpc_core/wilaya_form.html'
    success_url = reverse_lazy('wilaya_list')

class WilayaDeleteView(SafeDeleteView):
    model = Wilaya
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('wilaya_list')

    def get_related_objects(self):
        obj = self.get_object()
        moughataa_set = list(obj.moughataa_set.all())
        communes = []
        points_of_sale = []
        product_prices = []
        
        for moughataa in moughataa_set:
            communes.extend(list(moughataa.commune_set.all()))
            
        for commune in communes:
            points_of_sale.extend(list(commune.points_of_sale.all()))
            
        for point_of_sale in points_of_sale:
            product_prices.extend(list(point_of_sale.product_prices.all()))
            
        return {
            'Moughataa': moughataa_set,
            'Communes': communes,
            'Points de vente': points_of_sale,
            'Prix des produits': product_prices
        }

    def delete(self, request, *args, **kwargs):
        """Override delete to add success message"""
        logger.info(f"Méthode delete appelée pour Wilaya")
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Wilaya supprimée avec succès.')
        return response

# Moughataa Views
class MoughataaListView(LoginRequiredMixin,ListView):
    model = Moughataa
    template_name = 'inpc_core/moughataa_list.html'
    context_object_name = 'moughataa_list'

class MoughataaCreateView(LoginRequiredMixin,CreateView):
    model = Moughataa
    form_class = MoughataaForm
    template_name = 'inpc_core/moughataa_form.html'
    success_url = reverse_lazy('moughataa_list')

class MoughataaUpdateView(LoginRequiredMixin,UpdateView):
    model = Moughataa
    form_class = MoughataaForm
    template_name = 'inpc_core/moughataa_form.html'
    success_url = reverse_lazy('moughataa_list')

class MoughataaDeleteView(SafeDeleteView):
    model = Moughataa
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('moughataa_list')

    def get_related_objects(self):
        obj = self.get_object()
        return {
            'Communes': obj.commune_set.all()
        }

# Commune Views
class CommuneListView(LoginRequiredMixin,ListView):
    model = Commune
    template_name = 'inpc_core/commune_list.html'
    context_object_name = 'communes'

class CommuneCreateView(LoginRequiredMixin,CreateView):
    model = Commune
    form_class = CommuneForm
    template_name = 'inpc_core/commune_form.html'
    success_url = reverse_lazy('commune_list')

class CommuneUpdateView(LoginRequiredMixin,UpdateView):
    model = Commune
    form_class = CommuneForm
    template_name = 'inpc_core/commune_form.html'
    success_url = reverse_lazy('commune_list')

class CommuneDeleteView(SafeDeleteView):
    model = Commune
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('commune_list')

    def get_related_objects(self):
        obj = self.get_object()
        return {
            'Points de vente': obj.points_of_sale.all()
        }

# Point of Sale Views
class PointOfSaleListView(LoginRequiredMixin,ListView):
    model = PointOfSale
    template_name = 'inpc_core/point_of_sale_list.html'
    context_object_name = 'points_of_sale'

class PointOfSaleCreateView(LoginRequiredMixin,CreateView):
    model = PointOfSale
    form_class = PointOfSaleForm
    template_name = 'inpc_core/point_of_sale_form.html'
    success_url = reverse_lazy('point_of_sale_list')

class PointOfSaleUpdateView(LoginRequiredMixin,UpdateView):
    model = PointOfSale
    form_class = PointOfSaleForm
    template_name = 'inpc_core/point_of_sale_form.html'
    success_url = reverse_lazy('point_of_sale_list')

class PointOfSaleDeleteView(SafeDeleteView):
    model = PointOfSale
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('point_of_sale_list')

    def get_related_objects(self):
        obj = self.get_object()
        return {
            'Prix des produits': obj.product_prices.all()
        }

# Product Price Views
class ProductPriceListView(LoginRequiredMixin,ListView):
    model = ProductPrice
    template_name = 'inpc_core/product_price_list.html'
    context_object_name = 'product_prices'

class ProductPriceCreateView(LoginRequiredMixin,CreateView):
    model = ProductPrice
    form_class = ProductPriceForm
    template_name = 'inpc_core/product_price_form.html'
    success_url = reverse_lazy('product_price_list')

class ProductPriceUpdateView(LoginRequiredMixin,UpdateView):
    model = ProductPrice
    form_class = ProductPriceForm
    template_name = 'inpc_core/product_price_form.html'
    success_url = reverse_lazy('product_price_list')

class ProductPriceDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductPrice
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_price_list')

# Cart Views
class CartListView(LoginRequiredMixin,ListView):
    model = Cart
    template_name = 'inpc_core/cart_list.html'
    context_object_name = 'carts'

class CartCreateView(LoginRequiredMixin,CreateView):
    model = Cart
    form_class = CartForm
    template_name = 'inpc_core/cart_form.html'
    success_url = reverse_lazy('cart_list')

class CartUpdateView(LoginRequiredMixin,UpdateView):
    model = Cart
    form_class = CartForm
    template_name = 'inpc_core/cart_form.html'
    success_url = reverse_lazy('cart_list')

class CartDeleteView(SafeDeleteView):
    model = Cart
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('cart_list')

    def get_related_objects(self):
        obj = self.get_object()
        return {
            'Produits dans le panier': obj.cart_products.all()
        }

# Cart Product Views 
class CartProductListView(LoginRequiredMixin,ListView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_list.html'
    context_object_name = 'cart_products'

class CartProductCreateView(LoginRequiredMixin,CreateView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_form.html'
    form_class = CartProductForm
    success_url = reverse_lazy('cart_product_list')

class CartProductUpdateView(LoginRequiredMixin,UpdateView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_form.html'
    form_class = CartProductForm
    success_url = reverse_lazy('cart_product_list')

class CartProductDeleteView(LoginRequiredMixin,DeleteView):
    model = CartProduct
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('cart_product_list')

class CartProductDetailView(LoginRequiredMixin,DetailView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_detail.html'
    context_object_name = 'cart_product'


# INPC Calculation View
@login_required
def calculer_inpc(request):
    """
    Calcule l'Indice National des Prix à la Consommation (INPC)
    avec possibilité de sélectionner l'année et le mois
    """
    from datetime import datetime
    from django.db.models import Avg, Count, F, Q
    
    # Année de base
    ANNEE_BASE = 2019
    
    # Récupérer l'année et le mois à partir de la requête, sinon utiliser l'année et le mois actuels
    annee_courante = request.GET.get('annee', datetime.now().year)
    mois_courant = request.GET.get('mois', datetime.now().month)
    
    try:
        annee_courante = int(annee_courante)
        mois_courant = int(mois_courant)
    except ValueError:
        # En cas de valeurs invalides, utiliser l'année et le mois actuels
        annee_courante = datetime.now().year
        mois_courant = datetime.now().month
    
    # Récupérer tous les types de produits (catégories COICOP)
    types_produits = ProductType.objects.all()
    
    # Dictionnaires pour stocker les résultats
    inpc_par_groupe = []
    inpc_global = {}
    
    # Calculer l'INPC pour chaque type de produit
    for type_produit in types_produits:
        # Récupérer les produits de ce type
        produits = Product.objects.filter(product_type=type_produit)
        
        # Variables pour stocker les totaux
        prix_total_base = 0
        prix_total_courant = 0
        poids_total = 0
        produits_calcules = 0
        
        for produit in produits:
            # Récupérer les prix pour l'année de base
            prix_base = ProductPrice.objects.filter(
                product=produit,
                date_from__year=ANNEE_BASE,
                date_from__month=mois_courant
            ).order_by('-date_from').first()
            
            # Récupérer les prix pour l'année courante
            prix_courant = ProductPrice.objects.filter(
                product=produit,
                date_from__year=annee_courante,
                date_from__month=mois_courant
            ).order_by('-date_from').first()
            
            # Poids du produit - utiliser uniquement les pondérations de 2019
            annee_base_debut = datetime(2019, 1, 1)
            annee_base_fin = datetime(2019, 12, 31)
            
            poids = CartProduct.objects.filter(
                product=produit,
                date_from__lte=annee_base_fin,
                date_to__gte=annee_base_debut
            ).aggregate(Avg('weighting'))['weighting__avg'] or 0
            
            if prix_base and prix_courant and poids > 0:
                indice_produit = (prix_courant.value / prix_base.value) * 100
                prix_total_base += prix_base.value * poids
                prix_total_courant += prix_courant.value * poids
                poids_total += poids
                produits_calcules += 1
        
        # Calculer l'INPC pour ce groupe de produits
        # INPC = (Prix courant / Prix base) * 100
        inpc_groupe = (prix_total_courant / prix_total_base * 100) if prix_total_base > 0 else 0
        
        # N'ajouter que les groupes avec des produits calculés
        if produits_calcules > 0:
            inpc_par_groupe.append({
                'Année': annee_courante,
                'Mois': mois_courant,
                'Groupe': type_produit.label,
                'INPC': inpc_groupe,
                'Produits Calculés': produits_calcules
            })
    
    # Calculer l'INPC global
    if inpc_par_groupe:
        inpc_total = sum(groupe['INPC'] for groupe in inpc_par_groupe) / len(inpc_par_groupe)
    else:
        inpc_total = 0
    
    inpc_global[(annee_courante, mois_courant)] = inpc_total
    
    # Préparer les options d'années et de mois pour le formulaire
    annees_disponibles = sorted(set(
        ProductPrice.objects.values_list('date_from__year', flat=True).distinct()
    ))
    
    context = {
        'annee_base': ANNEE_BASE,
        'annee_courante': annee_courante,
        'mois_courant': mois_courant,
        'annees_disponibles': annees_disponibles,
        'inpc_par_groupe': inpc_par_groupe,
        'inpc_global': inpc_global
    }
    
    return render(request, 'inpc_core/calculer_inpc.html', context)

# Home View
@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Récupérer les données INPC des derniers mois
    from datetime import datetime, timedelta
    from django.db.models import Avg, Count, F, Q
    
    # Année de base
    ANNEE_BASE = 2019
    
    # Obtenir la date actuelle
    current_date = datetime.now()
    
    # Calculer les INPC pour les 6 derniers mois
    inpc_data = []
    labels_mois = []
    valeurs_inpc = []
    
    # Calculer les dates des 6 derniers mois
    mois_a_calculer = []
    date_temp = current_date.replace(day=1)
    
    for i in range(6):
        mois_a_calculer.append((date_temp.year, date_temp.month))
        if date_temp.month == 1:
            date_temp = date_temp.replace(year=date_temp.year - 1, month=12)
        else:
            date_temp = date_temp.replace(month=date_temp.month - 1)
    
    # Inverser la liste pour avoir l'ordre chronologique
    mois_a_calculer.reverse()
    
    for annee_courante, mois_courant in mois_a_calculer:
        print(f"\n=== Calcul pour {mois_courant}/{annee_courante} ===")
        
        # Créer les dates de début et fin du mois courant
        date_debut_mois_courant = datetime(annee_courante, mois_courant, 1)
        if mois_courant == 12:
            date_fin_mois_courant = datetime(annee_courante + 1, 1, 1) - timedelta(days=1)
        else:
            date_fin_mois_courant = datetime(annee_courante, mois_courant + 1, 1) - timedelta(days=1)
            
        # Créer les dates de début et fin du mois de l'année de base
        date_debut_mois_base = datetime(ANNEE_BASE, mois_courant, 1)
        if mois_courant == 12:
            date_fin_mois_base = datetime(ANNEE_BASE + 1, 1, 1) - timedelta(days=1)
        else:
            date_fin_mois_base = datetime(ANNEE_BASE, mois_courant + 1, 1) - timedelta(days=1)
        
        print(f"Période base: {date_debut_mois_base.date()} à {date_fin_mois_base.date()}")
        print(f"Période courante: {date_debut_mois_courant.date()} à {date_fin_mois_courant.date()}")
        
        # Vérifier les prix disponibles
        prix_base_count = ProductPrice.objects.filter(
            date_from__lte=date_fin_mois_base,
            date_to__gte=date_debut_mois_base
        ).count()
        
        prix_courant_count = ProductPrice.objects.filter(
            date_from__lte=date_fin_mois_courant,
            date_to__gte=date_debut_mois_courant
        ).count()
        
        print(f"Nombre de prix pour la période de base: {prix_base_count}")
        print(f"Nombre de prix pour la période courante: {prix_courant_count}")
        
        # Récupérer tous les types de produits (catégories COICOP)
        types_produits = ProductType.objects.all()
        
        # Variables pour le calcul de l'INPC
        inpc_total = 0
        poids_global_total = 0
        
        for type_produit in types_produits:
            produits = Product.objects.filter(product_type=type_produit)
            somme_indices = 0
            nombre_produits_valides = 0
            poids_groupe_total = 0
            
            print(f"\nGroupe {type_produit.code}:")
            
            for produit in produits:
                # Prix moyen pour l'année de base
                prix_base = ProductPrice.objects.filter(
                    product=produit,
                    date_from__lte=date_fin_mois_base,
                    date_to__gte=date_debut_mois_base
                ).aggregate(Avg('value'))['value__avg']
                
                # Prix moyen pour la période courante
                prix_courant = ProductPrice.objects.filter(
                    product=produit,
                    date_from__lte=date_fin_mois_courant,
                    date_to__gte=date_debut_mois_courant
                ).aggregate(Avg('value'))['value__avg']
                
                # Poids du produit - utiliser uniquement les pondérations de 2019
                annee_base_debut = datetime(2019, 1, 1)
                annee_base_fin = datetime(2019, 12, 31)
                
                poids = CartProduct.objects.filter(
                    product=produit,
                    date_from__lte=annee_base_fin,
                    date_to__gte=annee_base_debut
                ).aggregate(Avg('weighting'))['weighting__avg'] or 0
                
                if prix_base and prix_courant and poids > 0:
                    indice_produit = (prix_courant / prix_base) * 100
                    somme_indices += indice_produit * poids
                    poids_groupe_total += poids
                    nombre_produits_valides += 1
                    print(f"  Produit {produit.code}: Base={prix_base:.2f}, Courant={prix_courant:.2f}, Poids={poids:.2f}")
                else:
                    print(f"  Produit {produit.code}: INVALIDE - Base={prix_base}, Courant={prix_courant}, Poids={poids}")
            
            print(f"  Total produits valides: {nombre_produits_valides}")
            print(f"  Poids total du groupe: {poids_groupe_total}")
            
            # Calculer l'indice du groupe si des données valides existent
            if nombre_produits_valides > 0 and poids_groupe_total > 0:
                indice_groupe = somme_indices / poids_groupe_total
                inpc_total += indice_groupe * (poids_groupe_total / 100)
                poids_global_total += poids_groupe_total
                print(f"  Indice du groupe: {indice_groupe:.2f}")
            else:
                print("  Pas de données valides pour ce groupe")
        
        # Calculer l'INPC final
        inpc_global = inpc_total * (100 / poids_global_total) if poids_global_total > 0 else 0
        
        # Formater la date pour l'affichage
        month_name = date_debut_mois_courant.strftime('%B %Y')
        
        # Ajouter les résultats à la liste
        inpc_data.append({
            'year': annee_courante,
            'month': mois_courant,
            'month_name': month_name,
            'inpc': round(inpc_global, 2)
        })
        
        # Ajouter les données pour les graphiques
        labels_mois.append(month_name)
        valeurs_inpc.append(round(inpc_global, 2))
    
    # Données pour le graphique circulaire (répartition des types de produits)
    product_types_data = ProductType.objects.annotate(
        product_count=Count('products')
    ).values('label', 'product_count')
    
    pie_labels = [item['label'] for item in product_types_data]
    pie_data = [item['product_count'] for item in product_types_data]
    
    # Données pour le graphique en barres (prix moyens par wilaya)
    wilayas_data = Wilaya.objects.annotate(
        avg_price=Avg('moughataa_set__commune_set__points_of_sale__product_prices__value')
    ).values('name', 'avg_price')
    
    bar_labels = [item['name'] for item in wilayas_data]
    bar_data = [float(item['avg_price'] or 0) for item in wilayas_data]
    
    # Convertir les données en JSON pour le template
    from django.core.serializers.json import DjangoJSONEncoder
    import json
    
    context = {
        'inpc_data': inpc_data,
        # Données pour le graphique en ligne
        'labels_mois': json.dumps(labels_mois, cls=DjangoJSONEncoder),
        'valeurs_inpc': json.dumps(valeurs_inpc, cls=DjangoJSONEncoder),
        # Données pour le graphique circulaire
        'pie_labels': json.dumps(pie_labels, cls=DjangoJSONEncoder),
        'pie_data': json.dumps(pie_data, cls=DjangoJSONEncoder),
        # Données pour le graphique en barres
        'bar_labels': json.dumps(bar_labels, cls=DjangoJSONEncoder),
        'bar_data': json.dumps(bar_data, cls=DjangoJSONEncoder),
    }
    
    return render(request, 'inpc_core/home.html', context)

import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ExcelImportForm, ExcelExportForm
from .models import (
    ProductType, Product, Wilaya, Moughataa, 
    Commune, PointOfSale, ProductPrice, Cart, CartProduct 
)
from datetime import datetime
import io

def cleanup_old_prices():
    """
    Nettoie les anciennes données de prix en ne gardant que:
    - Toutes les données de 2019 (année de base)
    - Les données des 13 derniers mois pour les autres années
    """
    from datetime import datetime, timedelta
    
    # Conserver toutes les données de 2019 (année de base)
    base_year = 2019
    
    # Calculer la date limite pour les données récentes (13 derniers mois)
    current_date = datetime.now()
    retention_limit = current_date - timedelta(days=396)  # ~13 months
    
    # Supprimer les prix anciens sauf ceux de 2019
    ProductPrice.objects.filter(
        ~Q(date_from__year=base_year),  # Exclure l'année de base
        date_from__lt=retention_limit,   # Garder seulement les 13 derniers mois
    ).delete()

class ExcelImportView(LoginRequiredMixin, FormView):
    template_name = 'inpc_core/excel_import.html'
    form_class = ExcelImportForm
    success_url = '/inpc/import/'

    def form_valid(self, form):
        operation = form.cleaned_data['operation']
        model_type = form.cleaned_data['model_type']
        uploaded_file = form.cleaned_data['file']

        try:
            if operation == 'import':
                # Import based on model type
                import_methods = {
                    'product_type': self.import_product_types,
                    'product': self.import_products,
                    'wilaya': self.import_wilayas,
                    'moughataa': self.import_moughataa,
                    'commune': self.import_communes,
                    'point_of_sale': self.import_points_of_sale,
                    'product_price': self.import_product_prices,
                    'cart': self.import_carts,
                    'cart_product': self.import_cart_products
                }

                import_method = import_methods.get(model_type)
                if import_method:
                    df = pd.read_excel(uploaded_file)
                    
                    # Validate DataFrame columns
                    expected_columns = self.get_expected_columns(model_type)
                    missing_columns = set(expected_columns) - set(df.columns)
                    
                    if missing_columns:
                        raise ValueError(f"Colonnes manquantes: {', '.join(missing_columns)}")
                    
                    # Perform import with additional validation
                    result = import_method(df)
                    
                    if result.get('errors'):
                        messages.warning(self.request, f"Importation partielle. Erreurs: {result['errors']}")
                    else:
                        messages.success(self.request, f'Importation de {model_type} réussie!')
                else:
                    messages.error(self.request, 'Type de modèle non reconnu')

            elif operation == 'export':
                # Export based on model type
                export_methods = {
                    'product_type': self.export_product_types,
                    'product': self.export_products,
                    'wilaya': self.export_wilayas,
                    'moughataa': self.export_moughataa,
                    'commune': self.export_communes,
                    'point_of_sale': self.export_points_of_sale,
                    'product_price': self.export_product_prices,
                    'cart': self.export_carts,
                    'cart_product': self.export_cart_products
                }

                export_method = export_methods.get(model_type)
                if export_method:
                    df = export_method()
                    
                    # Create an in-memory bytes buffer
                    buffer = io.BytesIO()
                    
                    # Write DataFrame to Excel
                    df.to_excel(buffer, index=False, engine='openpyxl')
                    
                    # Prepare HTTP response
                    buffer.seek(0)
                    response = HttpResponse(
                        buffer.getvalue(), 
                        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                    )
                    response['Content-Disposition'] = f'attachment; filename={model_type}_export.xlsx'
                    
                    messages.success(self.request, f'Exportation de {model_type} réussie!')
                    return response
                else:
                    messages.error(self.request, 'Type de modèle non reconnu')

        except Exception as e:
            messages.error(self.request, f'Erreur lors de l\'opération: {str(e)}')

        return super().form_valid(form)

    def get_expected_columns(self, model_type):
        """Return expected columns for each model type"""
        column_map = {
            'product_type': ['code', 'label', 'description'],
            'product': ['code', 'name', 'description', 'unit_measure', 'product_type'],
            'wilaya': ['code', 'name'],
            'moughataa': ['code', 'label', 'wilaya_code'],
            'commune': ['code', 'name', 'moughataa_code'],
            'point_of_sale': ['code', 'type', 'gps_lat', 'gps_lon', 'commune_code'],
            'product_price': ['product_code', 'point_of_sale_code', 'value', 'date_from', 'date_to'],
            'cart': ['code', 'name', 'description'],
            'cart_product': ['cart_code', 'product_code', 'weighting', 'date_from', 'date_to']
        }
        return column_map.get(model_type, [])

    def import_product_types(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                ProductType.objects.create(
                    code=row['code'],
                    label=row['label'],
                    description=row.get('description', '')
                )
            except Exception as e:
                errors.append(f"Erreur pour {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_wilayas(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                Wilaya.objects.create(
                    code=row['code'],
                    name=row['name']
                )
            except Exception as e:
                errors.append(f"Erreur pour {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_moughataa(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                wilaya = Wilaya.objects.get(code=row['wilaya_code'])
                Moughataa.objects.create(
                    code=row['code'],
                    label=row['label'],
                    wilaya=wilaya
                )
            except Wilaya.DoesNotExist:
                errors.append(f"Erreur pour {row['code']}: Wilaya {row['wilaya_code']} non trouvée")
            except Exception as e:
                errors.append(f"Erreur pour {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_communes(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                moughataa = Moughataa.objects.get(code=row['moughataa_code'])
                Commune.objects.create(
                    code=row['code'],
                    name=row['name'],
                    moughataa=moughataa
                )
            except Moughataa.DoesNotExist:
                errors.append(f"Erreur pour {row['code']}: Moughataa {row['moughataa_code']} non trouvée")
            except Exception as e:
                errors.append(f"Erreur pour {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_points_of_sale(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                commune = Commune.objects.get(code=row['commune_code'])
                PointOfSale.objects.create(
                    code=row['code'],
                    type=row['type'],
                    gps_lat=row['gps_lat'],
                    gps_lon=row['gps_lon'],
                    commune=commune
                )
            except Commune.DoesNotExist:
                errors.append(f"Erreur pour {row['code']}: Commune {row['commune_code']} non trouvée")
            except Exception as e:
                errors.append(f"Erreur pour {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_product_prices(self, df):
        try:
            # Nettoyer les anciennes données avant l'import
            cleanup_old_prices()
            
            # Continuer avec l'import normal
            errors = []
            for _, row in df.iterrows():
                try:
                    product = Product.objects.get(code=row['product_code'])
                    point_of_sale = PointOfSale.objects.get(code=row['point_of_sale_code'])
                    ProductPrice.objects.create(
                        value=row['value'],
                        date_from=row['date_from'],
                        date_to=row['date_to'],
                        product=product,
                        point_of_sale=point_of_sale
                    )
                except Product.DoesNotExist:
                    errors.append(f"Erreur: Produit {row['product_code']} non trouvé")
                except PointOfSale.DoesNotExist:
                    errors.append(f"Erreur: Point de vente {row['point_of_sale_code']} non trouvé")
                except Exception as e:
                    errors.append(f"Erreur: {str(e)}")
            return {'errors': errors}
        except Exception as e:
            messages.error(self.request, f"Erreur lors de l'import des prix: {str(e)}")

    def import_carts(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                Cart.objects.create(
                    code=row['code'],
                    name=row['name'],
                    description=row.get('description', '')
                )
            except Exception as e:
                errors.append(f"Erreur pour {row['code']}: {str(e)}")
        return {'errors': errors}

    def import_cart_products(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                cart = Cart.objects.get(code=row['cart_code'])
                product = Product.objects.get(code=row['product_code'])
                CartProduct.objects.create(
                    cart=cart,
                    product=product,
                    weighting=row['weighting'],
                    date_from=row['date_from'],
                    date_to=row['date_to']
                )
            except Cart.DoesNotExist:
                errors.append(f"Erreur: Panier {row['cart_code']} non trouvé")
            except Product.DoesNotExist:
                errors.append(f"Erreur: Produit {row['product_code']} non trouvé")
            except Exception as e:
                errors.append(f"Erreur: {str(e)}")
        return {'errors': errors}

    def import_products(self, df):
        errors = []
        for _, row in df.iterrows():
            try:
                product_type = ProductType.objects.get(code=row['product_type'])
                Product.objects.create(
                    code=row['code'],
                    name=row['name'],
                    description=row.get('description', ''),
                    unit_measure=row['unit_measure'],
                    product_type=product_type
                )
            except ProductType.DoesNotExist:
                errors.append(f"Erreur pour {row['code']}: Type de produit {row['product_type']} non trouvé")
            except Exception as e:
                errors.append(f"Erreur pour {row['code']}: {str(e)}")
        return {'errors': errors}

    def export_product_types(self):
        queryset = ProductType.objects.all()
        return pd.DataFrame(list(queryset.values('code', 'label', 'description')))

    def export_products(self):
        queryset = Product.objects.select_related('product_type').all()
        return pd.DataFrame(list(queryset.values('code', 'name', 'description', 'unit_measure', 'product_type__code')))

    def export_wilayas(self):
        queryset = Wilaya.objects.all()
        return pd.DataFrame(list(queryset.values('code', 'name')))

    def export_moughataa(self):
        queryset = Moughataa.objects.select_related('wilaya').all()
        return pd.DataFrame(list(queryset.values('code', 'label', 'wilaya__code')))

    def export_communes(self):
        queryset = Commune.objects.select_related('moughataa').all()
        return pd.DataFrame(list(queryset.values('code', 'name', 'moughataa__code')))

    def export_points_of_sale(self):
        queryset = PointOfSale.objects.select_related('commune').all()
        return pd.DataFrame(list(queryset.values('code', 'type', 'gps_lat', 'gps_lon', 'commune__code')))

    def export_product_prices(self):
        queryset = ProductPrice.objects.select_related('product', 'point_of_sale').all()
        return pd.DataFrame(list(queryset.values('value', 'date_from', 'date_to', 'product__code', 'point_of_sale__code')))

    def export_carts(self):
        queryset = Cart.objects.all()
        return pd.DataFrame(list(queryset.values('code', 'name', 'description')))

    def export_cart_products(self):
        queryset = CartProduct.objects.select_related('cart', 'product').all()
        return pd.DataFrame(list(queryset.values('cart__code', 'product__code', 'weighting', 'date_from', 'date_to')))
