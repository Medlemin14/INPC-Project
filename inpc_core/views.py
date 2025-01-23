from django.db import models
from django.shortcuts import render
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from django.urls import reverse_lazy
from .models import (
    ProductType, Product, Wilaya, Moughataa, Commune, 
    PointOfSale, ProductPrice, Cart, CartProduct 
)
from .forms import (
    ProductTypeForm, ProductForm, WilayaForm, MoughataaForm, 
    CommuneForm, PointOfSaleForm, ProductPriceForm, 
    CartForm, CartProductForm
)
from .filters import ProductFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

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

class ProductTypeDeleteView(LoginRequiredMixin,DeleteView):
    model = ProductType
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_type_list')

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

class ProductDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_list')

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

class WilayaDeleteView(LoginRequiredMixin,DeleteView):
    model = Wilaya
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('wilaya_list')

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

class MoughataaDeleteView(LoginRequiredMixin,DeleteView):
    model = Moughataa
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('moughataa_list')

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

class CommuneDeleteView(LoginRequiredMixin,DeleteView):
    model = Commune
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('commune_list')

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

class PointOfSaleDeleteView(LoginRequiredMixin,DeleteView):
    model = PointOfSale
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('point_of_sale_list')

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

class ProductPriceDeleteView(LoginRequiredMixin,DeleteView):
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

class CartDeleteView(LoginRequiredMixin, DeleteView):
    model = Cart
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('cart_list')

    def form_valid(self, form):
        # Supprimer d'abord tous les CartProduct liés à ce Cart
        CartProduct.objects.filter(cart=self.object).delete()
        return super().form_valid(form)

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
            
            # Récupérer le poids du produit dans les paniers
            cart_products = CartProduct.objects.filter(
                product=produit,
                date_from__year__lte=annee_courante,
                date_to__year__gte=annee_courante
            )
            
            # Vérifier que tous les éléments nécessaires sont présents
            if prix_base and prix_courant and cart_products:
                poids_moyen = cart_products.aggregate(
                    models.Avg('weighting')
                )['weighting__avg'] or 0
                
                # Ajouter au total uniquement si le poids est significatif
                if poids_moyen > 0:
                    prix_total_base += prix_base.value * poids_moyen
                    prix_total_courant += prix_courant.value * poids_moyen
                    poids_total += poids_moyen
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
        return redirect('login')  # Redirige vers la page de connexion
    
    # Récupérer les données INPC des derniers mois
    from datetime import datetime, timedelta
    from django.db.models import Avg, F, Q
    
    # Année de base
    ANNEE_BASE = 2019
    
    # Obtenir la date actuelle
    current_date = datetime.now()
    
    # Calculer les INPC pour les 6 derniers mois
    inpc_data = []
    for i in range(6):
        # Calculer la date du mois précédent
        month_date = current_date - timedelta(days=30 * i)
        annee_courante = month_date.year
        mois_courant = month_date.month
        
        # Récupérer tous les types de produits (catégories COICOP)
        types_produits = ProductType.objects.all()
        
        # Calculer l'INPC global pour ce mois
        inpc_total = 0
        groupes_calcules = 0
        
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
                
                # Récupérer le poids du produit dans les paniers
                cart_products = CartProduct.objects.filter(
                    product=produit,
                    date_from__year__lte=annee_courante,
                    date_to__year__gte=annee_courante
                )
                
                # Vérifier que tous les éléments nécessaires sont présents
                if prix_base and prix_courant and cart_products:
                    poids_moyen = cart_products.aggregate(
                        models.Avg('weighting')
                    )['weighting__avg'] or 0
                    
                    # Ajouter au total uniquement si le poids est significatif
                    if poids_moyen > 0:
                        prix_total_base += prix_base.value * poids_moyen
                        prix_total_courant += prix_courant.value * poids_moyen
                        poids_total += poids_moyen
                        produits_calcules += 1
            
            # Calculer l'INPC pour ce groupe de produits
            # INPC = (Prix courant / Prix base) * 100
            if prix_total_base > 0 and produits_calcules > 0:
                inpc_groupe = (prix_total_courant / prix_total_base * 100)
                inpc_total += inpc_groupe
                groupes_calcules += 1
        
        # Calculer l'INPC global
        inpc_global = inpc_total / groupes_calcules if groupes_calcules > 0 else 0
        
        # Ajouter les résultats à la liste
        inpc_data.append({
            'year': annee_courante,
            'month': mois_courant,
            'inpc': inpc_global
        })
    
    return render(request, 'inpc_core/home.html', {'inpc_data': inpc_data})

import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ExcelImportForm
from .models import (
    ProductType, Product, Wilaya, Moughataa, 
    Commune, PointOfSale, ProductPrice, Cart, CartProduct 
)
from datetime import datetime

class ExcelImportView(LoginRequiredMixin,FormView):
    template_name = 'inpc_core/excel_import.html'
    form_class = ExcelImportForm
    success_url = '/inpc/import/'

    def form_valid(self, form):
        uploaded_file = form.cleaned_data['file']
        model_type = form.cleaned_data['model_type']

        try:
            # Read Excel file
            df = pd.read_excel(uploaded_file)
            
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
                import_method(df)
                messages.success(self.request, f'Importation de {model_type} réussie!')
            else:
                messages.error(self.request, 'Type de modèle non reconnu')

        except Exception as e:
            messages.error(self.request, f'Erreur lors de l\'importation: {str(e)}')

        return super().form_valid(form)

    def import_product_types(self, df):
        for _, row in df.iterrows():
            ProductType.objects.create(
                code=row['code'],
                label=row['label']
            )

    def import_products(self, df):
        for _, row in df.iterrows():
            product_type = ProductType.objects.get(code=row['product_type'])
            Product.objects.create(
                code=row['code'],
                name=row['name'],
                description=row['description'],
                unit_measure=row['unit_measure'],
                product_type=product_type
            )
        

    def import_wilayas(self, df):
        for _, row in df.iterrows():
            Wilaya.objects.create(
                code=row['code'],
                name=row['name']
            )
    
    def import_moughataa(self, df):
        for _, row in df.iterrows():
            wilaya = Wilaya.objects.get(code=row['wilaya_code'])
            Moughataa.objects.create(
                code=row['code'],
                label=row['label'],
                wilaya=wilaya
            )
    
    def import_communes(self, df):
        for _, row in df.iterrows():
            moughataa = Moughataa.objects.get(code=row['moughataa_code'])
            Commune.objects.create(
                code=row['code'],
                name=row['name'],
                moughataa=moughataa
            )
    
    def import_points_of_sale(self, df):
        for _, row in df.iterrows():
            commune = Commune.objects.get(code=row['commune_code'])
            PointOfSale.objects.create(
                code=row['code'],
                type=row['type'],
                gps_lat=row.get('gps_lat', None),
                gps_lon=row.get('gps_lon', None),
                commune=commune
            )
    
    def import_product_prices(self, df):
        for _, row in df.iterrows():
            product = Product.objects.get(code=row['product_code'])
            point_of_sale = PointOfSale.objects.get(code=row['point_of_sale_code'])
            ProductPrice.objects.create(
                product=product,
                point_of_sale=point_of_sale,
                value=row['value'],
                date_from=row['date_from'],
                date_to=row.get('date_to', None)
            )
    
    def import_carts(self, df):
        for _, row in df.iterrows():
            Cart.objects.create(
                code=row['code'],
                name=row['name'],
                description=row.get('description', '')
            )
    
    def import_cart_products(self, df):
        for _, row in df.iterrows():
            cart = Cart.objects.get(code=row['cart_code'])
            product = Product.objects.get(code=row['product_code'])
            CartProduct.objects.create(
                cart=cart,
                product=product,
                weighting=row['weighting'],
                date_from=row.get('date_from', datetime.now().date()),
                date_to=row.get('date_to', None)
            )
