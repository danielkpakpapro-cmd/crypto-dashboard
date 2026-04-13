# ₿ Crypto Dashboard - Analyse et Prédiction Bitcoin

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange)
![CoinGecko](https://img.shields.io/badge/API-CoinGecko-green)

## Description
Dashboard interactif de suivi et de prédiction du prix du Bitcoin.
Les données sont récupérées en temps réel via l'API CoinGecko (gratuite, sans clé API)
et analysées par 3 modèles de Machine Learning différents.

## Fonctionnalités
- Prix Bitcoin en temps réel (cours, variation 24h, volume, market cap)
- Historique des 30 derniers jours avec graphique interactif
- Comparaison de 3 modèles de prédiction :
  - Linear Regression
  - Random Forest
  - SVR (Support Vector Regression)
- Export automatique des données en CSV et Excel
- Prédiction ajustable de 3 à 30 jours via un slider
- Génération automatique des données au premier lancement

## Prérequis
Avant de commencer, assurez-vous d'avoir installé :
- [Python 3.10+](https://www.python.org/downloads/) — cochez "Add Python to PATH" lors de l'installation
- [Git](https://git-scm.com/downloads)

## Installation et lancement

### 1. Cloner le projet
```bash
git clone https://github.com/danielkpakpapro-cmd/crypto-dashboard.git
cd crypto-dashboard
```

### 2. Créer l'environnement virtuel
```bash
# Windows (PowerShell)
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

### 3. Activer l'environnement virtuel
```bash
# Windows (PowerShell)
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

> **Problème sur Windows ?** Si PowerShell bloque l'activation, exécutez d'abord :
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Puis relancez l'activation.

### 4. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 5. Lancer le dashboard
```bash
streamlit run app.py
```

Le dashboard s'ouvre automatiquement dans votre navigateur.  
**Les données sont récupérées automatiquement au premier lancement.**

> **Note** : une connexion internet est nécessaire pour récupérer
> les données via l'API CoinGecko.

## Structure du projet

## Comment ça marche

### 1. Récupération des données
Le fichier `scraper/coingecko.py` interroge l'API CoinGecko pour récupérer :
- Le prix actuel du Bitcoin en euros
- L'historique des 30 derniers jours
- La variation 24h, le volume et la market cap

Les données sont automatiquement sauvegardées en **CSV** et **Excel**
dans le dossier `data/`.

### 2. Modèles de prédiction
Le fichier `model/prediction.py` entraîne 3 modèles sur l'historique :

| Modèle | Comportement | Points forts |
|---|---|---|
| Linear Regression | Tendance en ligne droite | Simple, rapide, interprétable |
| Random Forest | Moyenne de plusieurs arbres de décision | Stable, robuste |
| SVR | Détecte des courbes complexes | Plus précis sur données non linéaires |

Les données sont normalisées avec un **StandardScaler** pour que les modèles
gèrent correctement l'extrapolation au-delà des données connues.

### 3. Dashboard Streamlit
Le fichier `app.py` affiche :
- Les métriques temps réel
- Le graphique historique interactif
- Les prédictions des 3 modèles sur N jours (ajustable via le slider)
- Le tableau comparatif des MAE

## Interprétation des résultats

### Métriques temps réel
- **Prix Bitcoin** : cours actuel en euros
- **Variation 24h** : positif = hausse, négatif = baisse
- **Volume 24h** : montant total échangé — plus c'est élevé, plus le marché est actif
- **Market Cap** : valeur totale de tous les Bitcoins en circulation

### Historique 30 jours
La courbe orange montre l'évolution réelle du prix :
- Les **pics** correspondent aux moments de forte hausse
- Les **creux** correspondent aux périodes de baisse
- La **tendance générale** indique la direction du marché

### MAE (Mean Absolute Error)
Le MAE mesure l'erreur moyenne de prédiction par jour :
- MAE < 1 000 € → excellent
- MAE entre 1 000 € et 3 000 € → acceptable pour la crypto
- MAE > 5 000 € → modèle trop imprécis

## Limitations
- Les prédictions sont **indicatives** et non des conseils financiers
- L'API CoinGecko gratuite est limitée à **10-30 appels par minute**
  (un cache de 5 minutes est mis en place pour éviter les blocages)
- Les prédictions au-delà de **7 jours** sont moins fiables car les modèles
  sont entraînés sur seulement 31 jours de données
- Les modèles simples ne capturent pas les événements imprévisibles du marché
  (actualités, régulations, tweets influents...)

## Pistes d'amélioration
- Ajouter d'autres cryptomonnaies (Ethereum, BNB, Solana...)
- Intégrer un graphique en chandelier (candlestick)
- Utiliser un modèle LSTM (réseau neuronal) pour de meilleures prédictions
- Déployer sur Streamlit Cloud pour un accès en ligne gratuit

## Auteurs
- **Daniel** — [danielkpakpapro-cmd](https://github.com/danielkpakpapro-cmd)
- **Binôme** — [GitHub](https://github.com/BINOME_USERNAME)

## Contexte
Projet réalisé dans le cadre du cours de Python — 2026