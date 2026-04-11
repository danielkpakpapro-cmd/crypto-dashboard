import requests
import pandas as pd
from datetime import datetime
import os

def get_prix_bitcoin():
    print("Récupération du prix Bitcoin...")
    
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "eur",
        "include_24hr_change": "true",
        "include_24hr_vol": "true",
        "include_market_cap": "true"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        if "bitcoin" not in data:
            print("API limitée, données par défaut utilisées...")
            return {
                "Date"          : datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Prix (€)"      : 0,
                "Variation 24h" : 0,
                "Volume 24h"    : 0,
                "Market Cap"    : 0
            }
        
        btc = data["bitcoin"]
        return {
            "Date"          : datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Prix (€)"      : btc["eur"],
            "Variation 24h" : btc["eur_24h_change"],
            "Volume 24h"    : btc["eur_24h_vol"],
            "Market Cap"    : btc["eur_market_cap"]
        }
    
    except Exception as e:
        print(f"Erreur : {e}")
        return {
            "Date"          : datetime.now().strftime("%d/%m/%Y %H:%M"),
            "Prix (€)"      : 0,
            "Variation 24h" : 0,
            "Volume 24h"    : 0,
            "Market Cap"    : 0
        }


def get_historique_bitcoin():
    print("Récupération de l'historique Bitcoin (30 jours)...")
    
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "eur",
        "days"       : "30",
        "interval"   : "daily"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 429:
            print("Limite API atteinte...")
            return None
        
        data = response.json()
        
        if "prices" not in data:
            print("Données indisponibles...")
            return None
        
        historique = []
        for item in data["prices"]:
            timestamp = item[0] / 1000
            date = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y")
            prix = item[1]
            historique.append({"Date": date, "Prix (€)": prix})
        
        print(f"{len(historique)} jours récupérés ✅")
        return historique
    
    except Exception as e:
        print(f"Erreur : {e}")
        return None


def sauvegarder_donnees(historique):
    os.makedirs("data", exist_ok=True)
    
    df = pd.DataFrame(historique)
    df.to_csv("data/bitcoin.csv", index=False)
    print("Fichier CSV sauvegardé ✅")
    
    df.to_excel("data/bitcoin.xlsx", index=False)
    print("Fichier Excel sauvegardé ✅")
    
    return df


if __name__ == "__main__":
    prix = get_prix_bitcoin()
    print(prix)
    
    historique = get_historique_bitcoin()
    if historique:
        df = sauvegarder_donnees(historique)
        print(df.head())