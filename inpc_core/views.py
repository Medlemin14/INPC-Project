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

# Product Type Views
class ProductTypeListView(ListView):
    model = ProductType
    template_name = 'inpc_core/product_type_list.html'
    context_object_name = 'product_types'

class ProductTypeCreateView(CreateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'inpc_core/product_type_form.html'
    success_url = reverse_lazy('product_type_list')

class ProductTypeUpdateView(UpdateView):
    model = ProductType
    form_class = ProductTypeForm
    template_name = 'inpc_core/product_type_form.html'
    success_url = reverse_lazy('product_type_list')

class ProductTypeDeleteView(DeleteView):
    model = ProductType
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_type_list')

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'inpc_core/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inpc_core/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inpc_core/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_list')

# Wilaya Views
class WilayaListView(ListView):
    model = Wilaya
    template_name = 'inpc_core/wilaya_list.html'
    context_object_name = 'wilayas'

class WilayaCreateView(CreateView):
    model = Wilaya
    form_class = WilayaForm
    template_name = 'inpc_core/wilaya_form.html'
    success_url = reverse_lazy('wilaya_list')

class WilayaUpdateView(UpdateView):
    model = Wilaya
    form_class = WilayaForm
    template_name = 'inpc_core/wilaya_form.html'
    success_url = reverse_lazy('wilaya_list')

class WilayaDeleteView(DeleteView):
    model = Wilaya
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('wilaya_list')

# Moughataa Views
class MoughataaListView(ListView):
    model = Moughataa
    template_name = 'inpc_core/moughataa_list.html'
    context_object_name = 'moughataa_list'

class MoughataaCreateView(CreateView):
    model = Moughataa
    form_class = MoughataaForm
    template_name = 'inpc_core/moughataa_form.html'
    success_url = reverse_lazy('moughataa_list')

class MoughataaUpdateView(UpdateView):
    model = Moughataa
    form_class = MoughataaForm
    template_name = 'inpc_core/moughataa_form.html'
    success_url = reverse_lazy('moughataa_list')

class MoughataaDeleteView(DeleteView):
    model = Moughataa
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('moughataa_list')

# Commune Views
class CommuneListView(ListView):
    model = Commune
    template_name = 'inpc_core/commune_list.html'
    context_object_name = 'communes'

class CommuneCreateView(CreateView):
    model = Commune
    form_class = CommuneForm
    template_name = 'inpc_core/commune_form.html'
    success_url = reverse_lazy('commune_list')

class CommuneUpdateView(UpdateView):
    model = Commune
    form_class = CommuneForm
    template_name = 'inpc_core/commune_form.html'
    success_url = reverse_lazy('commune_list')

class CommuneDeleteView(DeleteView):
    model = Commune
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('commune_list')

# Point of Sale Views
class PointOfSaleListView(ListView):
    model = PointOfSale
    template_name = 'inpc_core/point_of_sale_list.html'
    context_object_name = 'points_of_sale'

class PointOfSaleCreateView(CreateView):
    model = PointOfSale
    form_class = PointOfSaleForm
    template_name = 'inpc_core/point_of_sale_form.html'
    success_url = reverse_lazy('point_of_sale_list')

class PointOfSaleUpdateView(UpdateView):
    model = PointOfSale
    form_class = PointOfSaleForm
    template_name = 'inpc_core/point_of_sale_form.html'
    success_url = reverse_lazy('point_of_sale_list')

class PointOfSaleDeleteView(DeleteView):
    model = PointOfSale
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('point_of_sale_list')

# Product Price Views
class ProductPriceListView(ListView):
    model = ProductPrice
    template_name = 'inpc_core/product_price_list.html'
    context_object_name = 'product_prices'

class ProductPriceCreateView(CreateView):
    model = ProductPrice
    form_class = ProductPriceForm
    template_name = 'inpc_core/product_price_form.html'
    success_url = reverse_lazy('product_price_list')

class ProductPriceUpdateView(UpdateView):
    model = ProductPrice
    form_class = ProductPriceForm
    template_name = 'inpc_core/product_price_form.html'
    success_url = reverse_lazy('product_price_list')

class ProductPriceDeleteView(DeleteView):
    model = ProductPrice
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('product_price_list')

# Cart Views
class CartListView(ListView):
    model = Cart
    template_name = 'inpc_core/cart_list.html'
    context_object_name = 'carts'

class CartCreateView(CreateView):
    model = Cart
    form_class = CartForm
    template_name = 'inpc_core/cart_form.html'
    success_url = reverse_lazy('cart_list')

class CartUpdateView(UpdateView):
    model = Cart
    form_class = CartForm
    template_name = 'inpc_core/cart_form.html'
    success_url = reverse_lazy('cart_list')

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('cart_list')

# Cart Product Views
class CartProductListView(ListView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_list.html'
    context_object_name = 'cart_products'

class CartProductCreateView(CreateView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_form.html'
    form_class = CartProductForm
    success_url = reverse_lazy('cart_product_list')

class CartProductUpdateView(UpdateView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_form.html'
    form_class = CartProductForm
    success_url = reverse_lazy('cart_product_list')

class CartProductDeleteView(DeleteView):
    model = CartProduct
    template_name = 'inpc_core/confirm_delete.html'
    success_url = reverse_lazy('cart_product_list')

class CartProductDetailView(DetailView):
    model = CartProduct
    template_name = 'inpc_core/cart_product_detail.html'
    context_object_name = 'cart_product'

# INPC Calculation View
def calculer_inpc(request):
    # TODO: Implement INPC calculation logic
    return render(request, 'inpc_core/calculer_inpc.html')

# Home View
def home(request):
    return render(request, 'inpc_core/home.html')

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

class ExcelImportView(FormView):
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

