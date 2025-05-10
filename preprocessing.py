import pandas as pd

# 1. Charger le fichier brut mal formé
raw_file = "cosmetic_p.csv"
try:
    df = pd.read_csv(raw_file, sep=",", on_bad_lines='skip', engine='python')
except Exception as e:
    print(f"Erreur lors du chargement : {e}")
    exit()

# Si les colonnes ne sont pas bien séparées, on les renomme manuellement
if len(df.columns) == 1:
    print("Données mal séparées, correction des colonnes...")
    expected_columns = ["Label", "Brand", "Name", "Price", "Rank", "Ingredients", "Combination", "Dry", "Normal", "Oily", "Sensitive"]
    df = pd.read_csv(raw_file, sep=",", on_bad_lines='skip', engine='python', names=expected_columns, skiprows=1)

# Vérification et renommage forcé des colonnes pour garantir leur présence
expected_columns = ["Label", "Brand", "Name", "Price", "Rank", "Ingredients", "Combination", "Dry", "Normal", "Oily", "Sensitive"]
df.columns = expected_columns

# Affichage pour vérification
print("Colonnes après chargement :", df.columns.tolist())

# 2. Suppression des colonnes inutiles
df.drop(columns=["Price", "Rank"], inplace=True, errors='ignore')

# 3. Création des colonnes enrichies
def check_alcohol_free(ingredients):
    alcohols = ["Alcohol Denat.", "Ethanol", "Isopropyl Alcohol"]
    return all(a.lower() not in ingredients.lower() for a in alcohols)

def check_fungal_acne_safe(ingredients):
    risky = ["coconut oil", "lauric acid", "oleic acid"]
    return all(r.lower() not in ingredients.lower() for r in risky)

def check_acne_prone_safe(ingredients):
    safe = ["niacinamide", "green tea", "zinc"]
    return any(s.lower() in ingredients.lower() for s in safe)

df["Alcohol-Free"] = df["Ingredients"].fillna("").apply(check_alcohol_free)
df["Fungal Acne Safe"] = df["Ingredients"].fillna("").apply(check_fungal_acne_safe)
df["Acne-Prone Safe"] = df["Ingredients"].fillna("").apply(check_acne_prone_safe)

# 4. Conversion des indicateurs 0/1 en booléens
columns_to_convert = ["Oily", "Dry", "Sensitive", "Combination", "Normal"]
for col in columns_to_convert:
    if col in df.columns:
        df[col] = df[col].astype(bool)

# 5. Réorganisation des colonnes
column_order = ["Label", "Brand", "Name", "Ingredients", "Oily", "Dry", "Sensitive",
                "Combination", "Normal", "Alcohol-Free", "Fungal Acne Safe", "Acne-Prone Safe"]
df = df[[col for col in column_order if col in df.columns]]

# 6. Sauvegarde du fichier nettoyé
df.to_csv("final_cosmetics.csv", index=False, sep=";")
print("Fichier final_cosmetics.csv généré avec succès.")