import streamlit as st
import pickle
import os

st.title("Cosmetic Ingredient Property Analyzer")
st.write("Cette application prédit les propriétés d'un produit cosmétique en fonction de ses ingrédients.")
# Chemins vers les fichiers
model_path = "cosmetics_model.pkl"
vectorizer_path = "vectorizer.pkl"

# Vérifier que les fichiers existent
if not os.path.exists(model_path):
    st.error(f"Fichier introuvable : {model_path}")
    st.stop()
if not os.path.exists(vectorizer_path):
    st.error(f"Fichier introuvable : {vectorizer_path}")
    st.stop()

# Charger les fichiers
with open(model_path, "rb") as f:
    model = pickle.load(f)
with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# Zone de saisie
ingredients_input = st.text_area("Entrez les ingrédients :", height=150)

if st.button("Prédire les propriétés"):
    if ingredients_input.strip():
        try:
            input_data = vectorizer.transform([ingredients_input])
            prediction = model.predict(input_data)[0]

            categories = ["Oily", "Dry", "Sensitive", "Combination", "Normal",
                          "Alcohol-Free", "Acne-Prone Safe", "Fungal Acne Safe"]

            result = {cat: pred for cat, pred in zip(categories, prediction) if pred == 1}

            st.subheader("Propriétés prédites :")
            if result:
                st.success(f"Ce produit est adapté pour : {', '.join(result.keys())}")
            else:
                st.warning("Aucune propriété spécifique détectée.")
        except Exception as e:
            st.error(f"Erreur lors de la prédiction : {e}")
    else:
        st.error("Veuillez entrer des ingrédients.")
