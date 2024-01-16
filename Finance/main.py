import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

def calcul_quantite(date, ticker):
    # Lire le fichier CSV
    data = pd.read_csv('Data/Data.csv', delimiter=';')

    # Convertir la colonne "Date" en datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

    # Filtrer les données par date et par ticker
    filtered_data = data[(data['Date'] < date) & (data['Tickers'] == ticker)]

    # Calculer la somme de la colonne "Quantite"
    total_quantity = filtered_data['Quantite'].sum()
    if total_quantity != 0 :
        # Afficher la somme de la colonne "Quantite"
        print(f"\nAu {date}, le nombre d'action de {ticker} était de : {total_quantity}")
    else :
        pass


def dernier_jour_ouvre_avant_ou_veille(date):
    # Convertir la date en datetime
    date = pd.to_datetime(date)

    # Trouver la date de la veille
    veille = date - timedelta(days=1)

    while veille.weekday() >= 5 or veille.strftime('%Y-%m-%d') in holidays:
        veille -= pd.Timedelta(days=1)

    return veille


def recuperation_prix(date, ticker):
    # Convertir la date en datetime
    date = pd.to_datetime(date)

    # Trouver le dernier jour ouvré avant ou incluant la date
    last_business_day = dernier_jour_ouvre_avant_ou_veille(date)

    # Convertir la date en chaîne de caractères
    date_str_start = last_business_day.strftime('%Y-%m-%d')
    date_str_end = date.strftime('%Y-%m-%d')


    # Récupérer les données boursières d'une action précise
    data = yf.download(ticker, start=date_str_start, end=date_str_end)

    if not data.empty:
        # Récupérer la valeur de clôture de l'action
        last_value = round(data['Close'][0],2)
        print(f"\nLa valeur de clôture de l'action {ticker} à la date {date_str_end} est de : {last_value}")
    else:
        print(f"\nAucune donnée disponible pour {ticker} à la date {date_str_end}.")



# Liste des jours fériés
holidays = ['2022-01-01', '2022-12-25']

#Liste des actions détenue
action = ['PE500.PA','PANX.PA','LQQ.PA','EWLD.PA']

date = '2022-01-15'
# Afficher la valeur de clôture de l'action
for i in range(len(action)):
    calcul_quantite(date, action[i])
    recuperation_prix(date, action[i])
    print('\n######################################################################\n')

