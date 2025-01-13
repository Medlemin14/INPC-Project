import pandas as pd
import os
from datetime import datetime, timedelta

# Create a directory for sample import files
def create_sample_import_files():
    # Ensure the directory exists
    sample_dir = 'sample_import_files'
    os.makedirs(sample_dir, exist_ok=True)

    # 1. Product Type Import Sample
    product_types_df = pd.DataFrame([
        {'code': 'PT001', 'label': 'Alimentation'},
        {'code': 'PT002', 'label': 'Habillement'},
        {'code': 'PT003', 'label': 'Électronique'}
    ])
    product_types_df.to_excel(f'{sample_dir}/product_types_import.xlsx', index=False)

    # 2. Wilaya Import Sample
    wilayas_df = pd.DataFrame([
        {'code': 'W001', 'name': 'Nouakchott'},
        {'code': 'W002', 'name': 'Nouadhibou'},
        {'code': 'W003', 'name': 'Rosso'}
    ])
    wilayas_df.to_excel(f'{sample_dir}/wilayas_import.xlsx', index=False)

    # 3. Moughataa Import Sample
    moughataa_df = pd.DataFrame([
        {'code': 'M001', 'label': 'Capitale Nord', 'wilaya_code': 'W001'},
        {'code': 'M002', 'label': 'Capitale Sud', 'wilaya_code': 'W001'},
        {'code': 'M003', 'label': 'Port', 'wilaya_code': 'W002'}
    ])
    moughataa_df.to_excel(f'{sample_dir}/moughataa_import.xlsx', index=False)

    # 4. Commune Import Sample
    communes_df = pd.DataFrame([
        {'code': 'C001', 'name': 'Capitale Nord', 'moughataa_code': 'M001'},
        {'code': 'C002', 'name': 'Capitale Sud', 'moughataa_code': 'M002'},
        {'code': 'C003', 'name': 'Port Principal', 'moughataa_code': 'M003'}
    ])
    communes_df.to_excel(f'{sample_dir}/communes_import.xlsx', index=False)

    # 5. Products Import Sample
    products_df = pd.DataFrame([
        {
            'code': 'P001', 
            'name': 'Pain', 
            'description': 'Pain frais', 
            'unit_measure': 'kg', 
            'product_type': 'PT001'
        },
        {
            'code': 'P002', 
            'name': 'T-shirt', 
            'description': 'T-shirt en coton', 
            'unit_measure': 'unité', 
            'product_type': 'PT002'
        },
        {
            'code': 'P003', 
            'name': 'Smartphone', 
            'description': 'Smartphone Android', 
            'unit_measure': 'unité', 
            'product_type': 'PT003'
        }
    ])
    products_df.to_excel(f'{sample_dir}/products_import.xlsx', index=False)

    # 6. Points of Sale Import Sample
    points_of_sale_df = pd.DataFrame([
        {
            'code': 'POS001', 
            'type': 'Supermarché', 
            'commune_code': 'C001', 
            'gps_lat': 18.0735, 
            'gps_lon': -15.9582
        },
        {
            'code': 'POS002', 
            'type': 'Épicerie', 
            'commune_code': 'C002', 
            'gps_lat': 18.0735, 
            'gps_lon': -15.9582
        }
    ])
    points_of_sale_df.to_excel(f'{sample_dir}/points_of_sale_import.xlsx', index=False)

    # 7. Product Prices Import Sample
    today = datetime.now()
    product_prices_df = pd.DataFrame([
        {
            'product_code': 'P001', 
            'point_of_sale_code': 'POS001', 
            'value': 50.00, 
            'date_from': today.strftime('%Y-%m-%d'), 
            'date_to': (today + timedelta(days=365)).strftime('%Y-%m-%d')
        },
        {
            'product_code': 'P002', 
            'point_of_sale_code': 'POS002', 
            'value': 100.00, 
            'date_from': today.strftime('%Y-%m-%d'), 
            'date_to': (today + timedelta(days=365)).strftime('%Y-%m-%d')
        }
    ])
    product_prices_df.to_excel(f'{sample_dir}/product_prices_import.xlsx', index=False)

    # 8. Carts Import Sample
    carts_df = pd.DataFrame([
        {
            'code': 'CART001', 
            'name': 'Panier Familial', 
            'description': 'Panier standard pour famille'
        },
        {
            'code': 'CART002', 
            'name': 'Panier Étudiant', 
            'description': 'Panier économique'
        }
    ])
    carts_df.to_excel(f'{sample_dir}/carts_import.xlsx', index=False)

    # 9. Cart Products Import Sample
    cart_products_df = pd.DataFrame([
        {
            'cart_code': 'CART001', 
            'product_code': 'P001', 
            'weighting': 60.0,
            'date_from': today.strftime('%Y-%m-%d'),
            'date_to': (today + timedelta(days=365)).strftime('%Y-%m-%d')
        },
        {
            'cart_code': 'CART001', 
            'product_code': 'P002', 
            'weighting': 40.0,
            'date_from': today.strftime('%Y-%m-%d'),
            'date_to': (today + timedelta(days=365)).strftime('%Y-%m-%d')
        },
        {
            'cart_code': 'CART002', 
            'product_code': 'P001', 
            'weighting': 100.0,
            'date_from': today.strftime('%Y-%m-%d'),
            'date_to': (today + timedelta(days=365)).strftime('%Y-%m-%d')
        }
    ])
    cart_products_df.to_excel(f'{sample_dir}/cart_products_import.xlsx', index=False)

    print("Sample import files have been generated in the 'sample_import_files' directory.")

# Run the function
create_sample_import_files()