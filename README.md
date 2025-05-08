# 🧴 Cosmetics Ingredients Classifier

This project is a machine learning web application that classifies cosmetic product ingredients as **Safe**, **Risky**, or **Unknown** based on a trained model. It aims to help users quickly assess whether certain ingredients might be harmful in cosmetic products.

## 🚀 Features

- 🔍 Input cosmetic ingredients to check their safety.
- ✅ Classifies ingredients using a trained **XGBoost** model.
- 🧠 Uses **TF-IDF vectorization** to process text input.
- 🎯 Built with **Streamlit** for a fast and interactive user interface.

## 📁 Project Structure

```

cosmetics-project/
├── app.py                  # Streamlit app script
├── knoww\.ipynb             # Jupyter Notebook for model training
├── final\_cosmetics\_data.csv # Dataset used for training
├── cosmetics\_model.pkl     # Trained XGBoost model
├── vectorizer.pkl          # TF-IDF vectorizer
├── README.md               # Project description (this file)
├── .gitignore              # Files to ignore in Git

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

* This version does **not yet include QR code or barcode scanning**. That feature is planned for a future update.
* The classification is based solely on textual ingredient names and may not replace professional advice.

## 🛠️ Future Improvements

* 🔍 QR or barcode scanning to autofill ingredients.
* 🧼 Suggest safer alternatives to risky ingredients.
* 💾 User history and profiles.

```


