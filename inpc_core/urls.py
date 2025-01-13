from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # URLs pour GroupsProduits
    path('groupesproduits/', views.GroupsProduitsListView.as_view(), name='groupesproduits_list'),
    path('groupesproduits/new/', views.GroupsProduitsCreateView.as_view(), name='groupesproduits_new'),
    path('groupesproduits/edit/<int:pk>/', views.GroupsProduitsUpdateView.as_view(), name='groupesproduits_edit'),
    path('groupesproduits/delete/<int:pk>/', views.GroupsProduitsDeleteView.as_view(), name='groupesproduits_delete'),
    
    # URLs pour Régions
    path('regions/', views.RegionsListView.as_view(), name='regions_list'),
    path('regions/new/', views.RegionsCreateView.as_view(), name='regions_new'),
    path('regions/edit/<int:pk>/', views.RegionsUpdateView.as_view(), name='regions_edit'),
    path('regions/delete/<int:pk>/', views.RegionsDeleteView.as_view(), name='regions_delete'),
    
    # URLs pour Points de Ventes
    path('pointsdeventes/', views.PointsDeVentesListView.as_view(), name='pointsdeventes_list'),
    path('pointsdeventes/new/', views.PointsDeVentesCreateView.as_view(), name='pointsdeventes_new'),
    path('pointsdeventes/edit/<int:pk>/', views.PointsDeVentesUpdateView.as_view(), name='pointsdeventes_edit'),
    path('pointsdeventes/delete/<int:pk>/', views.PointsDeVentesDeleteView.as_view(), name='pointsdeventes_delete'),
    
    # URLs pour Produits
    path('produits/', views.ProduitsListView.as_view(), name='produits_list'),
    path('produits/new/', views.ProduitsCreateView.as_view(), name='produits_new'),
    path('produits/edit/<int:pk>/', views.ProduitsUpdateView.as_view(), name='produits_edit'),
    path('produits/delete/<int:pk>/', views.ProduitsDeleteView.as_view(), name='produits_delete'),
    
    # URLs pour Prix
    path('prix/', views.PrixListView.as_view(), name='prix_list'),
    path('prix/new/', views.PrixCreateView.as_view(), name='prix_new'),
    path('prix/edit/<int:pk>/', views.PrixUpdateView.as_view(), name='prix_edit'),
    path('prix/delete/<int:pk>/', views.PrixDeleteView.as_view(), name='prix_delete'),
    
    # URL pour le calcul de l'INPC
    path('calculer-inpc/', views.calculer_inpc, name='calculer_inpc'),

    # URL pour l'importation Excel
    path('import/', views.ExcelImportView.as_view(), name='excel_import'),
]