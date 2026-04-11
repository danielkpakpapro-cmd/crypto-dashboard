# ₿ Crypto Dashboard - Analyse et Prédiction Bitcoin

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange)

## Description
Dashboard interactif de suivi et de prédiction du prix du Bitcoin.  
Les données sont récupérées en temps réel via l'API CoinGecko et analysées 
par 3 modèles de Machine Learning différents.

## Fonctionnalités
- Prix Bitcoin en temps réel (cours, variation 24h, volume, market cap)
- Historique des 30 derniers jours avec graphique interactif
- Comparaison de 3 modèles de prédiction :
  - Linear Regression
  - Random Forest
  - SVR (Support Vector Regression)
- Export des données en CSV et Excel
- Prédiction ajustable de 3 à 30 jours

## Technologies utilisées
- Python 3.10+
- Streamlit — interface web interactive
- Scikit-learn — modèles de Machine Learning
- Plotly — graphiques interactifs
- Pandas — manipulation des données
- CoinGecko API — données crypto en temps réel

## Installation

### 1. Cloner le projet
```bash
git clone https://github.com/VOTRE_USERNAME/crypto-dashboard.git
cd crypto-dashboard
```

### 2. Créer et activer l'environnement virtuel
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer le dashboard
```bash
streamlit run app.py
```

## Structure du projet

## Interprétation des résultats

### Métriques temps réel
- **Prix Bitcoin** : cours actuel en euros
- **Variation 24h** : positif = hausse, négatif = baisse
- **Volume 24h** : montant total échangé — plus c'est élevé, plus le marché est actif
- **Market Cap** : valeur totale de tous les Bitcoins en circulation

### Historique 30 jours
La courbe orange montre l'évolution réelle du prix :
- Les pics correspondent aux moments de forte hausse
- Les creux correspondent aux périodes de baisse
- La tendance générale indique la direction du marché

### MAE (Mean Absolute Error)
Le MAE mesure l'erreur moyenne de prédiction par jour :
- MAE < 1 000 € → excellent
- MAE entre 1 000 € et 3 000 € → acceptable pour la crypto
- MAE > 5 000 € → modèle trop imprécis

### Limitations
Aucun modèle ne peut prédire la crypto à 100%.  
Ces prédictions sont des tendances indicatives, pas des conseils financiers.