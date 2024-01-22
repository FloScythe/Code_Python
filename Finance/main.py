import pandas as pd
import yfinance as yf
from datetime import datetime
import logging

# Configurer le module de journalisation
logging.basicConfig(filename='logfile.log', level=logging.ERROR)

file_path = 'Data/Data.csv'
date_specifiee = datetime(2024, 1, 21)

df = pd.read_csv(file_path, delimiter=';')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

df_filtre = df[df['Date'] <= date_specifiee]

# Utilisation de yf.download pour récupérer les données en une seule requête
tickers = df_filtre['Tickers'].unique().tolist()

try:
    data = yf.download(tickers, start=df_filtre['Date'].min(), end=date_specifiee)['Close']
except Exception as e:
    logging.error(f"Erreur lors de la récupération des données : {str(e)}")
    data = pd.DataFrame()

# Filtrer uniquement les lignes d'achat pour le calcul du PRU
achats_df = df_filtre[df_filtre['Action'] == 'Achat']

# Calculer la somme des montants par action pour les achats
montants_achats_par_action = achats_df.groupby('Tickers')['Montant'].sum()

# Calculer la somme des quantités par action pour les achats
quantites_achats_par_action = achats_df.groupby('Tickers')['Quantite'].sum()

# Calculer le PRU en excluant les transactions de vente
pru_par_action_achats = montants_achats_par_action / quantites_achats_par_action
# Utiliser reset_index pour afficher les tickers et les valeurs de PRU sans l'index "Tickers"
pru_par_action_achats_reset = pru_par_action_achats.reset_index()
# Renommer les colonnes du DataFrame résultant
pru_par_action_achats_reset.columns = ['Tickers', 'PRU']

# Calculer la somme des espèces restantes
somme_depot = df_filtre[df_filtre['Action'] == 'Depot']['Montant'].sum()
somme_achat = montants_achats_par_action.sum()
somme_vente = df_filtre[df_filtre['Action'] == 'Vente']['Montant'].sum()
somme_especes = somme_depot - somme_achat - somme_vente

# Calculer la valeur totale du portefeuille
if not data.empty:
    produit_par_action = data.iloc[-1].mul(df_filtre.groupby('Tickers')['Quantite'].sum(), fill_value=0)
    valeur_portefeuille = produit_par_action.sum() + somme_especes
    print(f"Il reste : {somme_especes} euros en espèces")
    print(f"La valeur totale du portefeuille à la date {date_specifiee} est de {valeur_portefeuille} euros.")
    print(pru_par_action_achats_reset.to_string(header=True, index=False))
else:
    print("Erreur dans la récupération des données. Consultez le fichier journal.")
