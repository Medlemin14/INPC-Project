from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    ProductTypeListView, ProductTypeCreateView, ProductTypeUpdateView, ProductTypeDeleteView,
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    WilayaListView, WilayaCreateView, WilayaUpdateView, WilayaDeleteView,
    MoughataaListView, MoughataaCreateView, MoughataaUpdateView, MoughataaDeleteView,
    CommuneListView, CommuneCreateView, CommuneUpdateView, CommuneDeleteView,
    PointOfSaleListView, PointOfSaleCreateView, PointOfSaleUpdateView, PointOfSaleDeleteView,
    ProductPriceListView, ProductPriceCreateView, ProductPriceUpdateView, ProductPriceDeleteView,
    CartListView, CartCreateView, CartUpdateView, CartDeleteView,
    CartProductListView, CartProductCreateView, CartProductUpdateView, CartProductDeleteView,
    ExcelImportView
)

urlpatterns = [
    # Product Type URLs
    path('product-type/', views.ProductTypeListView.as_view(), name='product_type_list'),
    path('product-type/create/', views.ProductTypeCreateView.as_view(), name='product_type_create'),
    path('product-type/<int:pk>/update/', views.ProductTypeUpdateView.as_view(), name='product_type_update'),
    path('product-type/<int:pk>/delete/', views.ProductTypeDeleteView.as_view(), name='product_type_delete'),

    # Product URLs
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # Wilaya URLs
    path('wilaya/', views.WilayaListView.as_view(), name='wilaya_list'),
    path('wilaya/create/', views.WilayaCreateView.as_view(), name='wilaya_create'),
    path('wilaya/<int:pk>/update/', views.WilayaUpdateView.as_view(), name='wilaya_update'),
    path('wilaya/<int:pk>/delete/', views.WilayaDeleteView.as_view(), name='wilaya_delete'),

    # Moughataa URLs
    path('moughataa/', views.MoughataaListView.as_view(), name='moughataa_list'),
    path('moughataa/create/', views.MoughataaCreateView.as_view(), name='moughataa_create'),
    path('moughataa/<int:pk>/update/', views.MoughataaUpdateView.as_view(), name='moughataa_update'),
    path('moughataa/<int:pk>/delete/', views.MoughataaDeleteView.as_view(), name='moughataa_delete'),

    # Commune URLs
    path('commune/', views.CommuneListView.as_view(), name='commune_list'),
    path('commune/create/', views.CommuneCreateView.as_view(), name='commune_create'),
    path('commune/<int:pk>/update/', views.CommuneUpdateView.as_view(), name='commune_update'),
    path('commune/<int:pk>/delete/', views.CommuneDeleteView.as_view(), name='commune_delete'),

    # Point of Sale URLs
    path('point-of-sale/', views.PointOfSaleListView.as_view(), name='point_of_sale_list'),
    path('point-of-sale/create/', views.PointOfSaleCreateView.as_view(), name='point_of_sale_create'),
    path('point-of-sale/<int:pk>/update/', views.PointOfSaleUpdateView.as_view(), name='point_of_sale_update'),
    path('point-of-sale/<int:pk>/delete/', views.PointOfSaleDeleteView.as_view(), name='point_of_sale_delete'),

    # Product Price URLs
    path('product-price/', views.ProductPriceListView.as_view(), name='product_price_list'),
    path('product-price/create/', views.ProductPriceCreateView.as_view(), name='product_price_create'),
    path('product-price/<int:pk>/update/', views.ProductPriceUpdateView.as_view(), name='product_price_update'),
    path('product-price/<int:pk>/delete/', views.ProductPriceDeleteView.as_view(), name='product_price_delete'),

    # Cart URLs
    path('cart/', views.CartListView.as_view(), name='cart_list'),
    path('cart/create/', views.CartCreateView.as_view(), name='cart_create'),
    path('cart/<int:pk>/update/', views.CartUpdateView.as_view(), name='cart_update'),
    path('cart/<int:pk>/delete/', views.CartDeleteView.as_view(), name='cart_delete'),

    # Cart Product URLs
    path('cart-product/', views.CartProductListView.as_view(), name='cart_product_list'),
    path('cart-product/create/', views.CartProductCreateView.as_view(), name='cart_product_create'),
    path('cart-product/<int:pk>/detail/', views.CartProductDetailView.as_view(), name='cart_product_detail'),
    path('cart-product/<int:pk>/update/', views.CartProductUpdateView.as_view(), name='cart_product_update'),
    path('cart-product/<int:pk>/delete/', views.CartProductDeleteView.as_view(), name='cart_product_delete'),
    # URL pour le calcul de l'INPC
    path('calculer-inpc/', views.calculer_inpc, name='calculer_inpc'),

    # URL pour l'importation Excel
    path('import/', views.ExcelImportView.as_view(), name='excel_import'),
    path('login/', auth_views.LoginView.as_view(template_name='inpc_core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inpc_core/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='inpc_core/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='inpc_core/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='inpc_core/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='inpc_core/password_reset_complete.html'), name='password_reset_complete'),
]