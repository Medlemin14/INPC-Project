import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
import random
import xlsxwriter

# Créer le dossier pour stocker les fichiers Excel s'il n'existe pas
output_dir = os.path.join(os.path.dirname(__file__), 'large_sample_import_files')
os.makedirs(output_dir, exist_ok=True)

# Définir des listes de données pour la génération
PRODUCT_TYPES = [
    {'code': 'ALIM', 'label': 'Alimentation', 'description': 'Produits alimentaires et boissons'},
    {'code': 'HABIL', 'label': 'Habillement', 'description': 'Vêtements et chaussures'},
    {'code': 'LOGEM', 'label': 'Logement', 'description': 'Logement, eau, électricité, gaz'},
    {'code': 'MEUBLE', 'label': 'Ameublement', 'description': 'Meubles, articles de ménage'},
    {'code': 'SANTE', 'label': 'Santé', 'description': 'Produits et services de santé'},
    {'code': 'TRANSP', 'label': 'Transports', 'description': 'Services de transport'},
    {'code': 'COMM', 'label': 'Communication', 'description': 'Services de communication'},
    {'code': 'LOISIR', 'label': 'Loisirs', 'description': 'Loisirs et culture'},
    {'code': 'EDUC', 'label': 'Éducation', 'description': 'Services éducatifs'},
    {'code': 'REST', 'label': 'Restauration', 'description': 'Restaurants et hôtels'}
]

def generate_products(num_products=500):
    products = []
    for i in range(num_products):
        product_type = random.choice(PRODUCT_TYPES)
        products.append({
            'code': f'P{i+1:04d}',
            'name': f'Produit {product_type["label"]} {i+1}',
            'description': f'Description détaillée du produit {i+1}',
            'unit_measure': random.choice(['kg', 'litre', 'pièce', 'm²', 'unité']),
            'product_type': product_type['code']
        })
    return products

def generate_points_of_sale(num_points=50):
    points_of_sale = []
    for i in range(num_points):
        points_of_sale.append({
            'code': f'POS{i+1:03d}',
            'type': random.choice(['Supermarché', 'Épicerie', 'Marché', 'Boutique']),
            'commune_code': f'COMM{i+1:03d}',
            'gps_lat': round(18.0735 + np.random.uniform(-1, 1), 4),
            'gps_lon': round(-15.9582 + np.random.uniform(-1, 1), 4)
        })
    return points_of_sale

def generate_product_prices(products, points_of_sale, start_year=2019, end_year=2024):
    product_prices = []
    # Réduire le nombre de combinaisons
    sample_products = random.sample(products, min(100, len(products)))
    sample_points = random.sample(points_of_sale, min(20, len(points_of_sale)))
    
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
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

def generate_carts(num_carts=20):
    carts = []
    for i in range(num_carts):
        carts.append({
            'code': f'CART{i+1:03d}',
            'name': f'Panier {i+1}',
            'description': f'Description du panier {i+1}'
        })
    return carts

def generate_cart_products(products, carts, start_year=2019, end_year=2024):
    cart_products = []
    for cart in carts:
        # Sélectionner un sous-ensemble de produits pour chaque panier
        selected_products = random.sample(products, random.randint(5, 20))
        total_weight = 100
        
        for product in selected_products:
            weight = round(total_weight / len(selected_products), 2)
            
            for year in range(start_year, end_year + 1):
                cart_products.append({
                    'cart_code': cart['code'],
                    'product_code': product['code'],
                    'weighting': weight,
                    'date_from': f'{year}-01-01',
                    'date_to': f'{year}-12-31'
                })
    
    return cart_products

# Ajout des fonctions pour Wilayas, Moughataa et Communes
def generate_wilayas(num_wilayas=15):
    wilayas = [
        {'code': 'W001', 'name': 'Nouakchott', 'description': 'Région de la capitale'},
        {'code': 'W002', 'name': 'Nouadhibou', 'description': 'Région du port'},
        {'code': 'W003', 'name': 'Dakhlet Nouadhibou', 'description': 'Région côtière nord'},
        {'code': 'W004', 'name': 'Tiris Zemmour', 'description': 'Région du nord'},
        {'code': 'W005', 'name': 'Adrar', 'description': 'Région désertique'},
        {'code': 'W006', 'name': 'Tagant', 'description': 'Région centrale'},
        {'code': 'W007', 'name': 'Brakna', 'description': 'Région sud-ouest'},
        {'code': 'W008', 'name': 'Trarza', 'description': 'Région sud-ouest'},
        {'code': 'W009', 'name': 'Gorgol', 'description': 'Région sud'},
        {'code': 'W010', 'name': 'Guidimakha', 'description': 'Région sud'},
        {'code': 'W011', 'name': 'Hodh Ech Chargui', 'description': 'Région est'},
        {'code': 'W012', 'name': 'Hodh El Gharbi', 'description': 'Région sud-est'},
        {'code': 'W013', 'name': 'Assaba', 'description': 'Région centrale'},
        {'code': 'W014', 'name': 'Inchiri', 'description': 'Région ouest'},
        {'code': 'W015', 'name': 'Sélibaby', 'description': 'Région sud'}
    ]
    return wilayas[:num_wilayas]

def generate_moughataa(wilayas, num_moughataa_per_wilaya=3):
    moughataa = []
    for wilaya in wilayas:
        for i in range(num_moughataa_per_wilaya):
            moughataa.append({
                'code': f'M{wilaya["code"][1:]}_{i+1:02d}',
                'label': f'Moughataa {wilaya["name"]} {i+1}',
                'wilaya_code': wilaya['code']
            })
    return moughataa

def generate_communes(moughataa, num_communes_per_moughataa=2):
    communes = []
    for mgh in moughataa:
        for i in range(num_communes_per_moughataa):
            communes.append({
                'code': f'C{mgh["code"][1:]}_{i+1:02d}',
                'name': f'Commune {mgh["label"]} {i+1}',
                'moughataa_code': mgh['code']
            })
    return communes

def save_large_dataframe(df, filepath, sheet_name='Sheet1'):
    # Créer un writer avec XlsxWriter
    writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    
    # Écrire le DataFrame
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Fermer le writer
    writer.close()

# Générer les données
products = generate_products()
points_of_sale = generate_points_of_sale()
product_prices = generate_product_prices(products, points_of_sale)
carts = generate_carts()
cart_products = generate_cart_products(products, carts)

# Générer les données géographiques
wilayas = generate_wilayas()
moughataa = generate_moughataa(wilayas)
communes = generate_communes(moughataa)

# Créer les DataFrames
df_product_types = pd.DataFrame(PRODUCT_TYPES)
df_products = pd.DataFrame(products)
df_points_of_sale = pd.DataFrame(points_of_sale)
df_product_prices = pd.DataFrame(product_prices)
df_carts = pd.DataFrame(carts)
df_cart_products = pd.DataFrame(cart_products)

# Créer les DataFrames supplémentaires
df_wilayas = pd.DataFrame(wilayas)
df_moughataa = pd.DataFrame(moughataa)
df_communes = pd.DataFrame(communes)

# Mettre à jour les points de vente avec des références aux communes
df_points_of_sale['commune_code'] = [random.choice(communes)['code'] for _ in range(len(df_points_of_sale))]

# Sauvegarder les fichiers Excel
save_large_dataframe(df_product_types, os.path.join(output_dir, 'product_types.xlsx'))
save_large_dataframe(df_products, os.path.join(output_dir, 'products.xlsx'))
save_large_dataframe(df_points_of_sale, os.path.join(output_dir, 'points_of_sale.xlsx'))
save_large_dataframe(df_product_prices, os.path.join(output_dir, 'product_prices.xlsx'))
save_large_dataframe(df_carts, os.path.join(output_dir, 'carts.xlsx'))
save_large_dataframe(df_cart_products, os.path.join(output_dir, 'cart_products.xlsx'))
save_large_dataframe(df_wilayas, os.path.join(output_dir, 'wilayas.xlsx'))
save_large_dataframe(df_moughataa, os.path.join(output_dir, 'moughataa.xlsx'))
save_large_dataframe(df_communes, os.path.join(output_dir, 'communes.xlsx'))

print(f"Fichiers générés dans {output_dir}")
print(f"Nombre de produits : {len(products)}")
print(f"Nombre de points de vente : {len(points_of_sale)}")
print(f"Nombre de prix de produits : {len(product_prices)}")
print(f"Nombre de paniers : {len(carts)}")
print(f"Nombre de produits dans les paniers : {len(cart_products)}")
print(f"Nombre de Wilayas : {len(wilayas)}")
print(f"Nombre de Moughataa : {len(moughataa)}")
print(f"Nombre de Communes : {len(communes)}")