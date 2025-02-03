import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random
import xlsxwriter

# Créer le dossier pour stocker les fichiers Excel s'il n'existe pas
output_dir = os.path.join(os.path.dirname(__file__), 'sample_import_files')
os.makedirs(output_dir, exist_ok=True)

# Définir les vrais noms des wilayas de Mauritanie
def generate_wilayas():
    wilayas = []
    # Sélectionner seulement 4 wilayas importantes
    wilaya_data = [
        {'code': 'NKC', 'name': 'Nouakchott'},
        {'code': 'NDB', 'name': 'Nouadhibou'},
        {'code': 'ATR', 'name': 'Atar'},
        {'code': 'KED', 'name': 'Kaédi'}
    ]
    for wilaya in wilaya_data:
        wilayas.append(wilaya)
    return wilayas

# Définir des listes de données pour la génération
def generate_products(num_products=20):  # Réduit à 20 produits
    products = []
    product_types = [
        {'code': 'ALIM', 'label': 'Alimentation'},
        {'code': 'HAB', 'label': 'Habillement'},
        {'code': 'LOG', 'label': 'Logement'},
        {'code': 'TRANS', 'label': 'Transport'}
    ]
    
    products_per_type = num_products // len(product_types)
    
    for type_data in product_types:
        for i in range(products_per_type):
            products.append({
                'code': f"{type_data['code']}_{i+1:02d}",
                'name': f"Produit {type_data['code']} {i+1}",
                'description': f"Description du produit {type_data['code']} {i+1}",
                'unit_measure': 'unité',
                'product_type': type_data['code']  
            })
    return products

def generate_moughataa(wilayas, num_moughataa_per_wilaya=2):  # Réduit à 2 moughataa par wilaya
    moughataa = []
    for wilaya in wilayas:
        for i in range(num_moughataa_per_wilaya):
            moughataa.append({
                'code': f"{wilaya['code']}_M{i+1}",
                'label': f"Moughataa {i+1} de {wilaya['name']}",
                'wilaya_code': wilaya['code']
            })
    return moughataa

def generate_communes(moughataa, num_communes_per_moughataa=1):  # Réduit à 1 commune par moughataa
    communes = []
    for m in moughataa:
        for i in range(num_communes_per_moughataa):
            communes.append({
                'code': f"{m['code']}_C{i+1}",
                'name': f"Commune {i+1} de {m['label']}",
                'moughataa_code': m['code']
            })
    return communes

def generate_points_of_sale(communes, num_points_per_commune=2):  # Maintenu à 2 points de vente par commune
    points_of_sale = []
    for commune in communes:
        for i in range(num_points_per_commune):
            points_of_sale.append({
                'code': f"{commune['code']}_POS{i+1}",
                'type': random.choice(['supermarket', 'market', 'shop']),
                'commune_code': commune['code'],
                'gps_lat': round(18.0735 + np.random.uniform(-1, 1), 4),
                'gps_lon': round(-15.9582 + np.random.uniform(-1, 1), 4)
            })
    return points_of_sale

def generate_product_prices(products, points_of_sale):
    """Générer des échantillons de prix de produits optimisés"""
    product_prices = []
    current_date = datetime.now()
    
    # Calculer les dates importantes
    retention_limit = current_date - timedelta(days=396)  # 13 mois
    
    # Générer les prix pour 2019 (année de base)
    base_year_start = datetime(2019, 1, 1)
    base_year_end = datetime(2019, 12, 31)
    
    # Générer les prix pour 2019 (année de base) - un prix par mois
    for month in range(1, 13):
        date_from = datetime(2019, month, 1)
        date_to = (datetime(2019, month + 1, 1) if month < 12 else datetime(2020, 1, 1)) - timedelta(days=1)
        
        for product in products:
            # Choisir aléatoirement 3 points de vente par produit au lieu de tous
            selected_pos = random.sample(points_of_sale, min(3, len(points_of_sale)))
            for pos in selected_pos:
                product_prices.append({
                    'product_code': product['code'],
                    'point_of_sale_code': pos['code'],
                    'value': round(random.uniform(100, 1000), 2),
                    'date_from': date_from,
                    'date_to': date_to
                })
    
    # Générer les prix pour les 13 derniers mois - un prix par mois
    current_month = current_date.replace(day=1)
    for _ in range(13):
        date_from = current_month.replace(day=1)
        date_to = (current_month.replace(month=current_month.month + 1) if current_month.month < 12 
                  else current_month.replace(year=current_month.year + 1, month=1)) - timedelta(days=1)
        
        for product in products:
            # Choisir aléatoirement 3 points de vente par produit
            selected_pos = random.sample(points_of_sale, min(3, len(points_of_sale)))
            for pos in selected_pos:
                product_prices.append({
                    'product_code': product['code'],
                    'point_of_sale_code': pos['code'],
                    'value': round(random.uniform(100, 1000), 2),
                    'date_from': date_from,
                    'date_to': date_to
                })
        
        current_month = (current_month - timedelta(days=1)).replace(day=1)
    
    return product_prices

def generate_carts(num_carts=4):  # Réduit à 4 paniers
    carts = []
    for i in range(num_carts):
        carts.append({
            'code': f'CART{i+1:02d}',
            'name': f'Panier {i+1}',
            'description': f'Description du panier {i+1}'
        })
    return carts

def generate_cart_products(products, carts, start_year=2019, end_year=2025):
    cart_products = []
    end_month = 1 if end_year == 2025 else 12
    
    for cart in carts:
        # Sélectionner tous les produits pour chaque panier
        selected_products = products
        total_weight = 100
        weights = [round(total_weight / len(selected_products), 2)] * len(selected_products)
        
        for product, weight in zip(selected_products, weights):
            for year in range(start_year, end_year + 1):
                for month in range(1, end_month + 1):
                    # Calculer le dernier jour du mois
                    last_day = (datetime(year, month, 1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
                    
                    cart_products.append({
                        'cart_code': cart['code'],
                        'product_code': product['code'],
                        'weighting': weight,
                        'date_from': f'{year}-{month:02d}-01',
                        'date_to': f'{year}-{month:02d}-{last_day.day:02d}'
                    })
    return cart_products

def generate_product_types():
    return [
        {'code': 'ALIM', 'label': 'Alimentation', 'description': 'Produits alimentaires'},
        {'code': 'HAB', 'label': 'Habillement', 'description': 'Vêtements et chaussures'},
        {'code': 'LOG', 'label': 'Logement', 'description': 'Logement et services'},
        {'code': 'TRANS', 'label': 'Transport', 'description': 'Transport et communication'}
    ]

def save_to_excel(df, filepath, sheet_name='Sheet1'):
    with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Générer les données
wilayas = generate_wilayas()
moughataa = generate_moughataa(wilayas)
communes = generate_communes(moughataa)
points_of_sale = generate_points_of_sale(communes)
product_types = generate_product_types()
products = generate_products()
product_prices = generate_product_prices(products, points_of_sale)
carts = generate_carts()
cart_products = generate_cart_products(products, carts)

# Créer les DataFrames
df_wilayas = pd.DataFrame(wilayas)
df_moughataa = pd.DataFrame(moughataa)
df_communes = pd.DataFrame(communes)
df_product_types = pd.DataFrame(product_types)
df_products = pd.DataFrame(products)
df_points_of_sale = pd.DataFrame(points_of_sale)
df_product_prices = pd.DataFrame(product_prices)
df_carts = pd.DataFrame(carts)
df_cart_products = pd.DataFrame(cart_products)

# Sauvegarder les fichiers Excel
save_to_excel(df_wilayas, os.path.join(output_dir, 'wilayas.xlsx'))
save_to_excel(df_moughataa, os.path.join(output_dir, 'moughataa.xlsx'))
save_to_excel(df_communes, os.path.join(output_dir, 'communes.xlsx'))
save_to_excel(df_product_types, os.path.join(output_dir, 'product_types.xlsx'))
save_to_excel(df_products, os.path.join(output_dir, 'products.xlsx'))
save_to_excel(df_points_of_sale, os.path.join(output_dir, 'points_of_sale.xlsx'))
save_to_excel(df_product_prices, os.path.join(output_dir, 'product_prices.xlsx'))
save_to_excel(df_carts, os.path.join(output_dir, 'carts.xlsx'))
save_to_excel(df_cart_products, os.path.join(output_dir, 'cart_products.xlsx'))

print("Fichiers d'exemple générés avec succès dans le dossier 'sample_import_files'")