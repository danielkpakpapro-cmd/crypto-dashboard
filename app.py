import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from scraper.coingecko import get_prix_bitcoin, get_historique_bitcoin, sauvegarder_donnees
from model.prediction import charger_donnees, entrainer_modeles, predire_prix

st.set_page_config(
    page_title="Crypto Dashboard",
    page_icon="₿",
    layout="wide"
)

@st.cache_data(ttl=300)
def charger_prix_bitcoin():
    return get_prix_bitcoin()

@st.cache_data(ttl=300)
def charger_historique():
    historique = get_historique_bitcoin()
    if historique:
        sauvegarder_donnees(historique)
    return historique

st.title("₿ Crypto Dashboard - Bitcoin")
st.markdown("Analyse de tendances et prédiction du prix du Bitcoin")

# ---- SIDEBAR ----
st.sidebar.title("Paramètres")
jours_prediction = st.sidebar.slider("Jours de prédiction", 3, 30, 7)
rafraichir = st.sidebar.button("Rafraîchir les données")

# ---- RÉCUPÉRATION DES DONNÉES ----
if rafraichir:
    st.cache_data.clear()
    with st.spinner("Récupération des données..."):
        historique = get_historique_bitcoin()
        if historique:
            sauvegarder_donnees(historique)
            st.success("Données mises à jour ")
        else:
            st.warning(" Limite API atteinte, données existantes conservées.")

# ---- PRIX EN TEMPS RÉEL ----
st.subheader("Prix en temps réel")

prix_actuel = charger_prix_bitcoin()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Prix Bitcoin",
    value=f"{prix_actuel['Prix (€)']:,.0f} €"
)
col2.metric(
    label="Variation 24h",
    value=f"{prix_actuel['Variation 24h']:.2f} %",
    delta=f"{prix_actuel['Variation 24h']:.2f} %"
)
col3.metric(
    label="Volume 24h",
    value=f"{prix_actuel['Volume 24h']:,.0f} €"
)
col4.metric(
    label="Market Cap",
    value=f"{prix_actuel['Market Cap']:,.0f} €"
)

# ---- HISTORIQUE ----
st.subheader("Historique des 30 derniers jours")

df = charger_donnees()

fig_historique = go.Figure()
fig_historique.add_trace(go.Scatter(
    x=df["Date"],
    y=df["Prix (€)"],
    mode="lines+markers",
    name="Prix réel",
    line=dict(color="#F7931A", width=2)
))
fig_historique.update_layout(
    xaxis_title="Date",
    yaxis_title="Prix (€)",
    hovermode="x unified"
)
st.plotly_chart(fig_historique, use_container_width=True)

# ---- PRÉDICTIONS ----
st.subheader(f"Prédictions sur {jours_prediction} jours")

with st.spinner("Entraînement des modèles..."):
    resultats_modeles = entrainer_modeles(df)
    df_predictions = predire_prix(resultats_modeles, df, jours_prediction)

fig_pred = go.Figure()

couleurs = {
    "Linear Regression": "#3498db",
    "Random Forest"    : "#2ecc71",
    "SVR"              : "#e74c3c"
}

for modele in ["Linear Regression", "Random Forest", "SVR"]:
    fig_pred.add_trace(go.Scatter(
        x=df_predictions["Jour"],
        y=df_predictions[modele],
        mode="lines+markers",
        name=modele,
        line=dict(color=couleurs[modele], width=2)
    ))

fig_pred.update_layout(
    xaxis_title="Jour",
    yaxis_title="Prix prédit (€)",
    hovermode="x unified"
)
st.plotly_chart(fig_pred, use_container_width=True)

# ---- TABLEAU COMPARATIF ----
st.subheader("Comparaison des modèles")

col1, col2, col3 = st.columns(3)

for col, (nom, res) in zip([col1, col2, col3], resultats_modeles.items()):
    col.metric(
        label=f"MAE - {nom}",
        value=f"{res['mae']:,.0f} €"
    )

st.dataframe(df_predictions, use_container_width=True)