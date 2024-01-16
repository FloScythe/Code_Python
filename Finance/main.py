import pandas as pd
import yfinance as yf
import numpy as np

def calcul_quantite(date, ticker):
    # Lire le fichier CSV
    data = pd.read_csv('Data/Data.csv', delimiter=';')

    # Convertir la colonne "Date" en datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

    # Filtrer les données par date et par ticker
    filtered_data = data[(data['Date'] < date) & (data['Tickers'] == ticker)]

    # Calculer la somme de la colonne "Quantite"
    total_quantity = filtered_data['Quantite'].sum()

    # Afficher la somme de la colonne "Quantite"
    print(f"\nAu {date}, le nombre d'action de {ticker} était de : {total_quantity}")


# Liste des jours fériés
holidays = ['2022-01-01', '2022-12-25']

def dernier_jour_ouvre_avant(date):
    date = pd.to_datetime(date)
    while date.weekday() > 5 or date.strftime('%Y-%m-%d') in holidays:
        date -= pd.Timedelta(days=1)
    return date


def recuperation_prix(date, ticker):
    # Convertir la date en datetime
    date = pd.to_datetime(date)

    # Trouver le dernier jour ouvré avant la date
    last_business_day = dernier_jour_ouvre_avant(date)

    # Convertir la date en chaîne de caractères
    date_str = last_business_day.strftime('%Y-%m-%d')

    # Récupérer les données boursières d'une action précise
    data = yf.download(ticker, start=date_str, end=date_str)

    if not data.empty:
        # Récupérer la valeur de clôture de l'action
        last_value = data['Close'][0]
        print(f"\nLa valeur de clôture de l'action {ticker} à la date {date_str} est de : {last_value}")
    else:
        print(f"\nAucune donnée disponible pour {ticker} à la date {date_str}.")


action = ['PE500.PA','PANX.PA','LQQ.PA','EWLD.PA']

calcul_quantite('2022-01-20', action[0])
print('\n######################################################################\n')
# Afficher la valeur de clôture de l'action
recuperation_prix('2020-01-20', action[0])
