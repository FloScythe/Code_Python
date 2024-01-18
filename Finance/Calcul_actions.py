#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:38:44 2024

@author: flos
"""

import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

#-------------------------------------
ticker = 'PE500.PA'
date_limite = '2022-01-25'
#-------------------------------------

#--------------Calcul du nombres d'action -----------------------

# Lire le fichier CSV
data = pd.read_csv('Data/Data.csv', delimiter=';')

# Convertir la colonne "Date" en datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Obtenir toutes les valeurs uniques de la colonne "Tickers"
valeurs_tickers = data['Tickers'].unique()
# Exclure la valeur "Cash" de la liste
filtered_tickers = [ticker for ticker in valeurs_tickers if ticker != 'Cash']

print(filtered_tickers)

for i in filtered_tickers:
    # Filtrer les données par date et par ticker
    filtered_data = data[(data['Date'] < date_limite) & (data['Tickers'] == i)]
    
    # Calculer la somme de la colonne "Quantite"
    nombre_action = filtered_data['Quantite'].sum()
    

    
    print(f"\nLe nombre d'action de {i} à la date du {date_limite} était de : {nombre_action}")
#-------------------------------------

#--------------Calcul de la valeur de l'action -----------------------
# Convertir la date en datetime
date = pd.to_datetime(date_limite)
# Trouver la date de la veille
veille = date - timedelta(days=1)

# Trouver le dernier jour ouvré avant ou incluant la date
while veille.weekday() >= 5 :
    veille -= pd.Timedelta(days=1)
last_business_day = veille

# Convertir la date en chaîne de caractères
date_str_start = last_business_day.strftime('%Y-%m-%d')
date_str_end = date.strftime('%Y-%m-%d')

# Récupérer les données boursières d'une action précise
data = yf.download(ticker, start=date_str_start, end=date_str_end)

if not data.empty:
    # Récupérer la valeur de clôture de l'action
    last_value = round(data['Close'][0],3)
    print(last_value)
else:
    print(f"\nAucune donnée disponible pour {ticker} à la date {date_str_end}.")
#-------------------------------------
