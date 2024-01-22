import pandas as pd
import yfinance as yf
from datetime import datetime
import logging
import os

# Configurer le module de journalisation
logging.basicConfig(filename='logfile.log', level=logging.ERROR)

file_path = 'Data/Data.csv'
date_specifiee = datetime.today()

df = pd.read_csv(file_path, delimiter=';')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

#--------------------------------------------------------------------------------
# Utilisation de yf.download pour récupérer les données en une seule requête
tickers = df['Tickers'].unique().tolist()
tickers.remove('Cash')
print(tickers)
try:
    data = yf.download(tickers, start=df['Date'].min(), end=date_specifiee)['Close']
except Exception as e:
    logging.error(f"Erreur lors de la récupération des données : {str(e)}")
    data = pd.DataFrame()

#--------------------------------------------------------------------------------
# Créer une liste pour stocker les résultats de chaque jour
resultats_liste = []

# Récupérer la première date présente dans le fichier "Data.CSV"
premiere_date = df['Date'].min()

# Boucle à travers les jours pour calculer les valeurs
for date in pd.date_range(start=premiere_date, end=date_specifiee, freq='D'):
    # Filtrer le DataFrame pour la date actuelle
    df_date = df[df['Date'] <= date]

    # Filtrer uniquement les lignes d'achat
    achats_df = df_date[df_date['Action'] == 'Achat']

    # Calculer la somme des espèces restantes
    somme_depot = df_date[df_date['Action'] == 'Depot']['Montant'].sum()
    somme_achat = df_date[df_date['Action'] == 'Achat']['Montant'].sum()
    somme_vente = df_date[df_date['Action'] == 'Vente']['Montant'].sum()
    somme_especes = somme_depot - somme_achat - somme_vente
    
    # Calculer les valeurs pour la date actuelle (similaire à votre code existant)
    valeur_portefeuille = 0  # Initialiser à une valeur par défaut
    
    if not data.empty:
        # Obtenez la valeur de l'action pour la date spécifiée
        for ticker in tickers:
            try:
                valeur_actions_date = data.loc[date, ticker]
                # Calculer le produit du nombre d'actions par la valeur de l'action à la date spécifiée
                print(date)
                print(f"{ticker} : {achats_df[achats_df['Tickers'] == ticker]['Quantite'].sum()} à la valeur : {valeur_actions_date}")

                produit_par_action = achats_df[achats_df['Tickers'] == ticker]['Quantite'].sum() * valeur_actions_date
                valeur_portefeuille += produit_par_action
                print(f"La valeur du portefeuille : {valeur_portefeuille}")
            except KeyError:
                # Gérer l'absence de la date dans l'index de data
                pass
    
    # Ajouter les valeurs à la liste des résultats
    resultats_liste.append({
        'Date': date,
        'Valeur du portefeuille': valeur_portefeuille + somme_especes,
        'Somme des dépôts': somme_depot
    })

# Créer un DataFrame à partir de la liste des résultats
resultats_df = pd.DataFrame(resultats_liste)

# Enregistrer le DataFrame dans un fichier Excel
fichier_excel = 'resultats_portefeuille.xlsx'
resultats_df.to_excel(fichier_excel, index=False)

print(f"Données enregistrées dans {fichier_excel}")
