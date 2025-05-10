# 🧴 Cosmetic Ingredients Skin Type Classifier

This project is a machine learning web interface that analyzes a large dataset of cosmetic products and predicts, based on their ingredients, what type of skin they are suitable for. Users can input ingredients, and the system will predict if the product is suitable for a specific skin type, helping users make informed decisions about cosmetic products.

## 🚀 Features

- 🔍 Input cosmetic ingredients to check which skin type(s) are they adapted for.
- ✅ Classifies ingredients using a trained **XGBoost** model.
- 🧠 Uses **TF-IDF vectorization** to process text input.
- 🎯 Built with **Streamlit** for a fast and interactive user interface.

## 📁 Project Structure

```

cosmetics-project/
├── app.py                    # Streamlit app script
├── cosmetics_analysis.ipynb   # Jupyter Notebook for model training
├── cosmetics_analysis.html    # HTML version of the Jupyter notebook
├── preprocessing.py           # Data preprocessing script
├── display_datasets.py        # Displays the first two rows of both datasets
├── verification.py            # Verifies if the rules for new columns (e.g., alcohol-free) are correctly applied
├── cosmetics.csv              # Original raw dataset
├── final_cosmetics_data.csv   # Preprocessed dataset
├── cosmetics_model.pkl        # Trained XGBoost model
├── vectorizer.pkl             # TF-IDF vectorizer
├── README.md                  # Project description (this file)
├── .gitignore                 # Files to be ignored by Git


````

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/cosmetics-project.git
cd cosmetics-project
````

2. Install the dependencies:

```bash
pip install streamlit xgboost scikit-learn pandas
```

## 🧪 How to Use

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the link that appears (usually `http://localhost:8501`) in your browser.

## 📌 Notes

* This version does **not include QR code or barcode scanning**.
* The classification is based solely on textual ingredient names and may not replace professional advice.

## 🛠️ Perspectives and Improvements

* 🔍 QR or barcode scanning to autofill ingredients.
* 🧼 Suggest safer alternatives to risky ingredients.
* 💾 User history and profiles.

```


