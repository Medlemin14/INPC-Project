import pandas as pd
import os

# Créer un dossier pour les exemples
os.makedirs('exemples_import', exist_ok=True)

# 1. Exemple de fichier pour Groupes de Produits
groupes_produits_df = pd.DataFrame({
    'nom_group': ['Alimentation', 'Transport', 'Logement', 'Santé', 'Éducation']
})
groupes_produits_df.to_excel('exemples_import/groupes_produits.xlsx', index=False)

# 2. Exemple de fichier pour Régions
regions_df = pd.DataFrame({
    'nom_region': ['Nouakchott', 'Nouadhibou', 'Rosso', 'Aioun', 'Kiffa']
})
regions_df.to_excel('exemples_import/regions.xlsx', index=False)

# 3. Exemple de fichier pour Points de Vente
points_vente_df = pd.DataFrame({
    'nom_point': ['Marché Central', 'Supermarché Carrefour', 'Épicerie du Coin', 'Marché de Nouadhibou'],
    'region': ['Nouakchott', 'Nouakchott', 'Rosso', 'Nouadhibou'],
    'longitude': [-15.9582, -15.9582, -15.8667, -16.0341],
    'latitude': [18.0735, 18.0735, 16.4307, 16.5166]
})
points_vente_df.to_excel('exemples_import/points_vente.xlsx', index=False)

# 4. Exemple de fichier pour Produits
produits_df = pd.DataFrame({
    'nom_produit': ['Pain', 'Riz', 'Poulet', 'Taxi', 'Location appartement'],
    'groupe_produit': ['Alimentation', 'Alimentation', 'Alimentation', 'Transport', 'Logement'],
    'ponderation': [0.2, 0.15, 0.25, 0.1, 0.3]
})
produits_df.to_excel('exemples_import/produits.xlsx', index=False)

# 5. Exemple de fichier pour Prix
prix_df = pd.DataFrame({
    'produit': ['Pain', 'Riz', 'Poulet', 'Taxi', 'Location appartement'],
    'prix': [2.5, 3.0, 5.0, 10.0, 50000],
    'annee': [2024, 2024, 2024, 2024, 2024],
    'mois': [1, 1, 1, 1, 1],
    'points_de_vente': [
        'Marché Central,Supermarché Carrefour', 
        'Marché Central,Épicerie du Coin', 
        'Marché Central', 
        'Marché de Nouadhibou', 
        'Marché Central'
    ]
})
prix_df.to_excel('exemples_import/prix.xlsx', index=False)

print("Fichiers d'exemple générés dans le dossier 'exemples_import'")