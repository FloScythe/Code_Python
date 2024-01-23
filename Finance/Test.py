import pandas as pd
import yfinance as yf
from datetime import datetime
import logging
import os

#------------------------------------------------------------------------------

file_path = 'Performance.csv'

df = pd.read_csv(file_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])

# Date pour les tests
date_specifiee = datetime(2022, 1, 20)
# date_debut = datetime(2022, 1, 15)

# Filtrer le DataFrame pour les dates spécifiées
df_filtre = df[(df['Date'] <= date_specifiee)]
print(df_filtre)

# hp = 1 + (vp-(vp-1 + diff))/(vp-1 + diff)
valeur_portefeuille = df_filtre['Valeur du portefeuille']
valeur_portefeuille_veille = df_filtre['Valeur du portefeuille']
difference = df_filtre['Difference_Valeur_Investie']
print(valeur_portefeuille,difference)
# Calculer la différence de valeur investie entre date_specifiee et date_debut
df_filtre['HP'] = 1 + (valeur_portefeuille-(difference))/difference
df_filtre['HP'].iloc[0] = 1  # Remplacer la première valeur par 1
#------------------------------------------------------------------------------

# Enregistrer le DataFrame filtré dans un fichier CSV
csv_path = 'Test.csv'
df_filtre.to_csv(csv_path, index=False)
print(f"Le fichier Performance.csv a été créé et enregistré.")