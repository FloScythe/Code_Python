#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:38:44 2024

@author: flos
"""

import pandas as pd
#-------------------------------------

#Liste des actions détenue
action = ['PE500.PA','PANX.PA','LQQ.PA','EWLD.PA']

# Date de recherche
date = '2023-06-25'
#-------------------------------------

# Lire le fichier CSV
data = pd.read_csv('Data/Data.csv', delimiter=';')

# Convertir la colonne "Date" en datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

for i in action :
    # Filtrer les données par date et par ticker
    filtered_data = data[(data['Date'] < date) & (data['Tickers'] == ticker)]

# Calculer la somme de la colonne "Quantite"
total_quantity = filtered_data['Quantite'].sum()

if total_quantity != 0:
    
    # Afficher la somme de la colonne "Quantite"
    valeur_action = recuperation_prix(date, ticker)
    valeur_total = calcul_valeur(total_quantity, valeur_action)
    """
    print(f"\nLe nombre d'action de {ticker} était de : {total_quantity}")
    print(f"Une valeur à la cloture de : {valeur_action} €")
    print(f"Une valeur total dans le portefeuille de : {valeur_total} €")
    print('\n######################################################################\n')
    """