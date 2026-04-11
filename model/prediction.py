import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

def charger_donnees():
    df = pd.read_csv("data/bitcoin.csv")
    df["Jour"] = range(len(df))
    return df

def entrainer_modeles(df):
    X = df[["Jour"]]
    y = df["Prix (€)"]

    scaler_X = StandardScaler()
    scaler_y = StandardScaler()

    X_scaled = scaler_X.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y.values.reshape(-1, 1)).ravel()

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_scaled, test_size=0.2, random_state=42
    )

    modeles = {
        "Linear Regression": LinearRegression(),
        "Random Forest"    : RandomForestRegressor(n_estimators=100, random_state=42),
        "SVR"              : SVR(kernel="rbf", C=100, gamma=0.1, epsilon=0.1)
    }

    resultats = {}

    for nom, modele in modeles.items():
        modele.fit(X_train, y_train)
        y_pred_scaled = modele.predict(X_test)
        y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).ravel()
        y_test_original = scaler_y.inverse_transform(y_test.reshape(-1, 1)).ravel()
        mae = mean_absolute_error(y_test_original, y_pred)

        print(f"{nom} → Erreur moyenne : {mae:.2f} €")

        resultats[nom] = {
            "modele"  : modele,
            "mae"     : mae,
            "scaler_X": scaler_X,
            "scaler_y": scaler_y
        }

    return resultats

def predire_prix(resultats, df, jours_suivants=7):
    dernier_jour = df["Jour"].max()
    jours_futurs = np.array(
        range(dernier_jour + 1, dernier_jour + 1 + jours_suivants)
    ).reshape(-1, 1)

    predictions = {"Jour": [f"J+{i+1}" for i in range(jours_suivants)]}

    for nom, res in resultats.items():
        X_futur_scaled = res["scaler_X"].transform(jours_futurs)
        y_pred_scaled = res["modele"].predict(X_futur_scaled)
        y_pred = res["scaler_y"].inverse_transform(
            y_pred_scaled.reshape(-1, 1)
        ).ravel()
        predictions[nom] = [round(p, 2) for p in y_pred]

    return pd.DataFrame(predictions)

if __name__ == "__main__":
    df = charger_donnees()
    print(f"{len(df)} jours chargés\n")

    resultats = entrainer_modeles(df)

    print("\nPrédictions sur 7 jours :")
    predictions = predire_prix(resultats, df)
    print(predictions)