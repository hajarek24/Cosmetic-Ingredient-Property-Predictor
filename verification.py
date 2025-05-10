## Pour vérifier si on a correctement fait les colonnes Alcohol-Free, Fungal Acne Safe et Acne-Safe
import pandas as pd

# Charger le fichier final
df = pd.read_csv("final_cosmetics.csv", sep=";")

# Définir les règles simples
alcohols = ["Alcohol Denat.", "Ethanol", "Isopropyl Alcohol"]
not_safe_fungal = ["coconut oil", "lauric acid", "oleic acid"]
safe_acne = ["niacinamide", "green tea", "zinc"]

print("=== Vérification Alcohol-Free ===")
df_false = df[df["Alcohol-Free"] == False]
for i, row in df_false.iterrows():
    if not any(x.lower() in row["Ingredients"].lower() for x in alcohols):
        print(f" Incohérence possible à la ligne {i} : marqué 'non alcohol-free' mais aucun alcool trouvé.")

print("\n=== Vérification Fungal Acne Safe ===")
df_fungal_unsafe = df[df["Fungal Acne Safe"] == False]
for i, row in df_fungal_unsafe.iterrows():
    if all(x.lower() not in row["Ingredients"].lower() for x in not_safe_fungal):
        print(f" Incohérence possible à la ligne {i} : marqué 'non sûr pour acné fongique' mais ingrédients risqués absents.")

print("\n=== Vérification Acne-Prone Safe ===")
df_acne_safe = df[df["Acne-Prone Safe"] == True]
for i, row in df_acne_safe.iterrows():
    if all(x.lower() not in row["Ingredients"].lower() for x in safe_acne):
        print(f" Doute à la ligne {i} : marqué 'sûr pour peau acnéique' mais aucun ingrédient bénéfique trouvé.")

print("\n Vérification terminée.")
