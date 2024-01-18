#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:20:52 2024

@author: flos
"""
import pandas as pd

def calcul_espece(file_path, date_limite):
    # Lire le fichier CSV en spécifiant le séparateur et le format de date
    data = pd.read_csv(file_path, delimiter=';', parse_dates=['Date'], dayfirst=True)

    # Convertir les dates au format 'YYYY-MM-DD'
    date_limite_str = pd.to_datetime(date_limite, format='%Y-%m-%d').strftime('%Y-%m-%d')
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')

    # Filtrer les données par date limite
    data_filtre = data[data['Date'] <= date_limite_str]

    # Filtrer les données par type d'action
    montant_depot = data_filtre[data_filtre['Action'] == 'Depot']['Montant'].sum()
    montant_achat = data_filtre[data_filtre['Action'] == 'Achat']['Montant'].sum()
    montant_vente = data_filtre[data_filtre['Action'] == 'Vente']['Montant'].sum()

    # Calculer le restant en espèces
    restant_espece = round(montant_depot - montant_achat - montant_vente, 2)

    return restant_espece

# Exemple d'utilisation
date_limite = '2024-01-18'
file_path = 'Data/Data.csv'  # Assurez-vous de mettre le bon chemin vers votre fichier CSV
resultat_espece = calcul_espece(file_path, date_limite)
print(f"Le restant en espèces jusqu'à la date {date_limite} est de : {resultat_espece}")
