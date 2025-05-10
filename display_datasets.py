## Pour afficher les colonnes et les 2 premières lignes des deux datasets (l'originale et la finale)
import pandas as pd

# Pour afficher toutes les colonnes dans la sortie
pd.set_option('display.max_columns', None)

# Charger les fichiers CSV
orig = pd.read_csv('cosmetic_p.csv', sep=',')
mod  = pd.read_csv('final_cosmetics.csv', sep=';', on_bad_lines='skip')

# Affichage des colonnes
print("=== Original Dataset Columns ===")
print(orig.columns.tolist(), end='\n\n')

print("=== Modified Dataset Columns ===")
print(mod.columns.tolist(), end='\n\n')

# Affichage des 2 premières lignes
print("=== Original – first 2 rows ===")
print(orig.head(2).to_string(index=False), end='\n\n')

print("=== Modified – first 2 rows ===")
print(mod.head(2).to_string(index=False))