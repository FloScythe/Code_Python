#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:25:51 2024

Calcul de la valeur du portefeuille
"""

import pandas as pd
import yfinance as yf
from datetime import datetime

file_path = 'Data/Data.csv'
df = pd.read_csv(file_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])
# Récupérer la première date présente dans le fichier "Data.CSV"
premiere_date = datetime(2024,1,10) #df['Date'].min()
#Date du jour
date_specifiee = datetime.today()
#--------------------------------------------------------------------------------
# Utilisation de yf.download pour récupérer les données en une seule requête
tickers = df['Tickers'].unique().tolist()
tickers.remove('Cash')
data = yf.download(tickers, start=premiere_date, end=date_specifiee)['Close'].round(3)
#--------------------------------------------------------------------------------
# Créer une liste pour stocker les données
resultats = []
for date in  pd.date_range(start=premiere_date, end=date_specifiee - pd.Timedelta(days=1), freq='D'):
    # Filtrer le DataFrame pour la date actuelle
    df_date = df[df['Date'] <= date]
    df_cash = df_date[df_date['Tickers']=='Cash']
    cash = df_cash['Quantite'].sum()
    somme_journalier = []
    for ticker in tickers :
        somme_action = df_date[df_date['Tickers'] == ticker]['Quantite'].sum()
        try :
            #Trouver la valeur de l'action à une date précise
            valeur_actions_date = data.loc[date, ticker]
        except KeyError :
            # Si une erreur KeyError est levée, sélectionner la valeur précédente dans le tableau "data" en utilisant shift(-1)
            valeur_actions_date = data.loc[date, ticker] if date in data.index else data[ticker].shift(-1).loc[:date].dropna().iloc[-1]            
        valeur_ticker = round(valeur_actions_date*somme_action,3)
        somme_journalier.append(valeur_ticker)

    # Calculer la somme des espèces restantes
    somme_depot = df_date[df_date['Action'] == 'Depot']['Montant'].sum()
    somme_achat = df_date[df_date['Action'] == 'Achat']['Montant'].sum()
    somme_vente = df_date[df_date['Action'] == 'Vente']['Montant'].sum()
    restant_cash = somme_depot - somme_achat - somme_vente
    valeur_portefeuille = round(sum(somme_journalier,restant_cash),3)
    #--------------------------------------------------------------------------------

    # Ajouter les résultats à la liste
    resultats.append({
        'Date': date, 
        'Valeur du portefeuille': valeur_portefeuille, 
        'Valeur investie': cash
        })
print(resultats)
