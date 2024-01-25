#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:30:21 2024

@author: flos
"""

import pandas as pd
import yfinance as yf
from datetime import datetime
import os
import matplotlib.pyplot as plt

def charger_donnees_csv(file_path):
    df = pd.read_csv(file_path, delimiter=';')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def recuperer_donnees_yfinance(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Close'].round(3)
    return data

def calculer_valeur_journaliere(df, tickers, data, start_date, end_date):
    resultats = []
    somme_journalier = []  # Ajout de cette ligne
    for date in pd.date_range(start=start_date, end=end_date - pd.Timedelta(days=1), freq='D'):
        df_date = df[df['Date'] <= date]
        df_cash = df_date[df_date['Tickers']=='Cash']
        cash = df_cash['Quantite'].sum()
        somme_journalier = []
        for ticker in tickers:
            somme_action = df_date[df_date['Tickers'] == ticker]['Quantite'].sum()
            try:
                valeur_actions_date = data.loc[date, ticker]
            except KeyError:
                valeur_actions_date = data.loc[date, ticker] if date in data.index else data[ticker].shift(-1).loc[:date].dropna().iloc[-1]
            valeur_ticker = round(valeur_actions_date * somme_action, 3)
            somme_journalier.append(valeur_ticker)

        somme_depot = df_date[df_date['Action'] == 'Depot']['Montant'].sum()
        somme_achat = df_date[df_date['Action'] == 'Achat']['Montant'].sum()
        somme_vente = df_date[df_date['Action'] == 'Vente']['Montant'].sum()
        restant_cash = somme_depot - somme_achat - somme_vente
        valeur_portefeuille = round(sum(somme_journalier, restant_cash), 3)

        resultats.append({
            'Date': date,
            'Valeur du portefeuille': valeur_portefeuille,
            'Valeur investie': cash
        })

    return resultats, somme_journalier

def sauvegarder_resultats(resultats, csv_path):
    df_resultats = pd.DataFrame(resultats)
    df_resultats.to_csv(csv_path, index=False, sep=";")
    print(f"Les résultats ont été enregistrés dans {csv_path}")

def calculer_repartition_ticker(tickers, somme_journalier, valeur_portefeuille):
    repartitions = []
    for i, ticker in enumerate(tickers):
        somme_ticker = somme_journalier[i]
        repartition = round(somme_ticker / valeur_portefeuille * 100, 2)
        repartitions.append((ticker, repartition))
        print(f"La part de {ticker} est de : {repartition}%")
    return repartitions

def calculer_performance(df, date_specifiee):
    df['Date'] = pd.to_datetime(df['Date'])
    df_filtre = df[df['Date'] <= date_specifiee]
    df_filtre['Difference_Valeur_Investie'] = df_filtre['Valeur investie'].diff().round(3)
    df_filtre.loc[df_filtre.index[0], 'Difference_Valeur_Investie'] = 0
    df_filtre['HP'] = round(1 + (df_filtre['Valeur du portefeuille'] - (df_filtre['Valeur du portefeuille'].shift(1) + df_filtre['Difference_Valeur_Investie'])) / (df_filtre['Valeur du portefeuille'].shift(1) + df_filtre['Difference_Valeur_Investie']), 3)
    df_filtre.loc[df_filtre.index[0], 'HP'] = 1
    df_filtre.to_csv(csv_path, index=False, sep=";")

    df = pd.read_csv(csv_path, delimiter=';')
    df['Date'] = pd.to_datetime(df['Date'])

    df_annee = df['Date'].dt.year.unique()

    for date in df_annee:
        df_filtre = df[df['Date'].dt.year == date]
        performance = (df_filtre['HP'].prod() - 1)
        performance_percent = round(performance * 100, 2)
        print(f"la performance de l'année {date} : {performance_percent}%")

    performance = round((df_filtre['Valeur du portefeuille'].iloc[-1] / df_filtre['Valeur investie'].iloc[0] - 1) * 100, 2)
    print(f"la performance toutes années confondues : {performance}%")


# Utilisation des fonctions
file_path = 'Data/Data.csv'
csv_path = 'Rendement.csv'
start_date = charger_donnees_csv(file_path)['Date'].min()
end_date = datetime.today()
tickers = charger_donnees_csv(file_path)['Tickers'].unique().tolist()
tickers.remove('Cash')

df = charger_donnees_csv(file_path)
data = recuperer_donnees_yfinance(tickers, start_date, end_date)
resultats, somme_journalier = calculer_valeur_journaliere(df, tickers, data, start_date, end_date)
sauvegarder_resultats(resultats, csv_path)
repartitions = calculer_repartition_ticker(tickers, somme_journalier, resultats[-1]['Valeur du portefeuille'])
calculer_performance(pd.read_csv(csv_path, delimiter=';'), end_date)


