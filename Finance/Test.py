import pandas as pd
import yfinance as yf
from datetime import datetime

file_path = 'Data/Data.csv'

#Date pour les tests
date_specifiee = datetime(2024,1,24)

df = pd.read_csv(file_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])

#--------------------------------------------------------------------------------
# Utilisation de yf.download pour récupérer les données en une seule requête
tickers = df['Tickers'].unique().tolist()
tickers.remove('Cash')
#print(tickers)
data = yf.download(tickers, start=df['Date'].min(), end=date_specifiee)['Close'].round(3)
print(data)
#--------------------------------------------------------------------------------
"""
# Récupérer la première date présente dans le fichier "Data.CSV"
premiere_date = df['Date'].min()
"""
#Date pour les tests
premiere_date = datetime(2024,1,20)

# Créer une liste pour stocker les données
resultats = []

for date in  pd.date_range(start=premiere_date, end=date_specifiee - pd.Timedelta(days=1), freq='D'):
    print("\n",date)
    # Filtrer le DataFrame pour la date actuelle
    df_date = df[df['Date'] <= date]
    
    df_cash = df_date[df_date['Tickers']=='Cash']
    cash = df_cash['Quantite'].sum()
    #print(f"Le total investi a la date {date} : {cash}")
    
    somme_journalier = []
    for ticker in tickers :
        somme_action = df_date[df_date['Tickers'] == ticker]['Quantite'].sum()
        print(f"Le nombre d'action {ticker} est de : {somme_action}")
        try :
            #Trouver la valeur de l'action à une date précise
            valeur_actions_date = data.loc[date, ticker]
            print(f"La valeur de l'action {ticker} est de : {valeur_actions_date}")
        except KeyError :
            # Si une erreur KeyError est levée, sélectionner la valeur précédente dans le tableau "data" en utilisant shift(-1)
            valeur_actions_date = data.loc[date, ticker] if date in data.index else data[ticker].shift(-1).loc[:date].dropna().iloc[-1]
            print(f"La valeur de l'action {ticker} est de : {valeur_actions_date}")
            
        
        valeur_ticker = round(valeur_actions_date*somme_action,3)
        somme_journalier.append(valeur_ticker)
        print(somme_journalier)

    # Calculer la somme des espèces restantes
    somme_depot = df_date[df_date['Action'] == 'Depot']['Montant'].sum()
    somme_achat = df_date[df_date['Action'] == 'Achat']['Montant'].sum()
    somme_vente = df_date[df_date['Action'] == 'Vente']['Montant'].sum()
    restant_cash = somme_depot - somme_achat - somme_vente
    #print("Le total restant :",restant_cash)
    
    valeur_portefeuille = round(sum(somme_journalier,restant_cash),3)
    print("La valeur du portefeuille est de : ",valeur_portefeuille)
    
for i, ticker in enumerate(tickers):
    somme_ticker = somme_journalier[i]
    repartition = round(somme_ticker / valeur_portefeuille * 100, 2)
    print(f"La part de {ticker} est de : {repartition}%")

    #--------------------------------------------------------------------------------