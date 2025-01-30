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
WILAYAS = [
    {'code': 'NDB', 'name': 'Nouadhibou'},
    {'code': 'NKC', 'name': 'Nouakchott'},
    {'code': 'TRZ', 'name': 'Trarza'},
    {'code': 'BRK', 'name': 'Brakna'},
    {'code': 'GRG', 'name': 'Gorgol'},
    {'code': 'ADR', 'name': 'Adrar'},
    {'code': 'ASB', 'name': 'Assaba'},
    {'code': 'GDM', 'name': 'Guidimaka'},
    {'code': 'HEC', 'name': 'Hodh Ech Chargui'},
    {'code': 'HEG', 'name': 'Hodh El Gharbi'},
    {'code': 'INC', 'name': 'Inchiri'},
    {'code': 'TGN', 'name': 'Tagant'},
    {'code': 'TRS', 'name': 'Tiris Zemmour'}
]

# Définir des listes de données pour la génération
PRODUCT_TYPES = [
    {'code': 'ALIM', 'label': 'Alimentation', 'description': 'Produits alimentaires et boissons'},
    {'code': 'HABIL', 'label': 'Habillement', 'description': 'Vêtements et chaussures'},
    {'code': 'LOGEM', 'label': 'Logement', 'description': 'Logement, eau, électricité, gaz'},
    {'code': 'MEUBLE', 'label': 'Ameublement', 'description': 'Meubles, articles de ménage'},
    {'code': 'SANTE', 'label': 'Santé', 'description': 'Produits et services de santé'}
]

def generate_products(num_products=50):  # Réduit à 50 produits
    products = []
    for i in range(num_products):
        product_type = random.choice(PRODUCT_TYPES)
        products.append({
            'code': f'P{i+1:03d}',
            'name': f'Produit {product_type["label"]} {i+1}',
            'description': f'Description du produit {i+1}',
            'unit_measure': random.choice(['kg', 'litre', 'pièce']),
            'product_type': product_type['code']
        })
    return products

def generate_wilayas():
    return WILAYAS

def generate_moughataa(wilayas, num_moughataa_per_wilaya=2):  # Réduit à 2 moughataa par wilaya
    moughataa = []
    for wilaya in wilayas:
        for i in range(num_moughataa_per_wilaya):
            moughataa.append({
                'code': f'{wilaya["code"]}_M{i+1}',
                'label': f'Moughataa {i+1} de {wilaya["name"]}',
                'wilaya_code': wilaya['code']  # Déjà correct
            })
    return moughataa

def generate_communes(moughataa, num_communes_per_moughataa=2):  # Réduit à 2 communes par moughataa
    communes = []
    for m in moughataa:
        for i in range(num_communes_per_moughataa):
            communes.append({
                'code': f'{m["code"]}_C{i+1}',
                'name': f'Commune {i+1} de {m["label"]}',
                'moughataa_code': m['code']
            })
    return communes

def generate_points_of_sale(communes, num_points_per_commune=2):  # Réduit à 2 points de vente par commune
    points_of_sale = []
    for commune in communes:
        for i in range(num_points_per_commune):
            points_of_sale.append({
                'code': f'{commune["code"]}_POS{i+1}',
                'type': random.choice(['supermarket', 'market', 'shop']),
                'commune_code': commune['code'],
                'gps_lat': round(18.0735 + np.random.uniform(-1, 1), 4),
                'gps_lon': round(-15.9582 + np.random.uniform(-1, 1), 4)
            })
    return points_of_sale

def generate_product_prices(products, points_of_sale, start_year=2019, end_year=2025):
    product_prices = []
    end_month = 1 if end_year == 2025 else 12  # Pour 2025, on ne prend que janvier
    
    # Réduire le nombre de combinaisons
    sample_products = random.sample(products, min(20, len(products)))
    sample_points = random.sample(points_of_sale, min(10, len(points_of_sale)))
    
    for year in range(start_year, end_year + 1):
        for month in range(1, end_month + 1):
            # Calculer le dernier jour du mois
            last_day = (datetime(year, month, 1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            
            for product in sample_products:
                for point in sample_points:
                    base_price = round(np.random.uniform(10, 500), 2)
                    inflation_factor = 1 + (year - start_year) * 0.02  # 2% d'inflation par an
                    price = round(base_price * inflation_factor * (1 + np.random.uniform(-0.1, 0.1)), 2)
                    
                    product_prices.append({
                        'product_code': product['code'],
                        'point_of_sale_code': point['code'],
                        'value': price,
                        'date_from': f'{year}-{month:02d}-01',
                        'date_to': f'{year}-{month:02d}-{last_day.day:02d}'
                    })
    return product_prices

def generate_carts(num_carts=5):  # Réduit à 5 paniers
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
        # Sélectionner un sous-ensemble de produits pour chaque panier
        selected_products = random.sample(products, min(5, len(products)))
        total_weight = 100
        weights = [round(total_weight / len(selected_products), 2)] * len(selected_products)
        
        for product, weight in zip(selected_products, weights):
            for year in range(start_year, end_year + 1):
                cart_products.append({
                    'cart_code': cart['code'],
                    'product_code': product['code'],
                    'weighting': weight,
                    'date_from': f'{year}-01-01',
                    'date_to': f'{year}-12-31'
                })
    return cart_products

def save_to_excel(df, filepath, sheet_name='Sheet1'):
    with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Générer les données
wilayas = generate_wilayas()
moughataa = generate_moughataa(wilayas)
communes = generate_communes(moughataa)
products = generate_products()
points_of_sale = generate_points_of_sale(communes)
product_prices = generate_product_prices(products, points_of_sale)
carts = generate_carts()
cart_products = generate_cart_products(products, carts)

# Créer les DataFrames
df_wilayas = pd.DataFrame(wilayas)
df_moughataa = pd.DataFrame(moughataa)
df_communes = pd.DataFrame(communes)
df_product_types = pd.DataFrame(PRODUCT_TYPES)
df_products = pd.DataFrame(products)
df_points_of_sale = pd.DataFrame(points_of_sale)
df_product_prices = pd.DataFrame(product_prices)
df_carts = pd.DataFrame(carts)
df_cart_products = pd.DataFrame(cart_products)

# Sauvegarder les fichiers
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