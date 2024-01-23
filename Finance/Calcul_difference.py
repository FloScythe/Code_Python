import pandas as pd
import yfinance as yf
from datetime import datetime
import logging
import os

#------------------------------------------------------------------------------

file_path = 'Rendement.csv'

df = pd.read_csv(file_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])

# Date pour les tests
date_specifiee = datetime.today() - pd.Timedelta(days=1)
# date_debut = datetime(2022, 1, 15)

# Filtrer le DataFrame pour les dates spécifiées
df_filtre = df[(df['Date'] <= date_specifiee)]
#print(df_filtre)

# Calculer la différence de valeur investie entre date_specifiee et date_debut
df_filtre['Difference_Valeur_Investie'] = df_filtre['Valeur investie'].diff().round(3)
df_filtre['Difference_Valeur_Investie'].iloc[0] = 0  # Remplacer la première valeur par 0

# Calculer la colonne 'HP'
df_filtre['HP'] = round(1 + (df_filtre['Valeur du portefeuille'] - (df_filtre['Valeur du portefeuille'].shift(1) + df_filtre['Difference_Valeur_Investie'])) / (df_filtre['Valeur du portefeuille'].shift(1) + df_filtre['Difference_Valeur_Investie']),3)
df_filtre['HP'].iloc[0] = 1  # Remplacer la première valeur par 1

# Afficher le résultat
print(df_filtre[['Date', 'Valeur investie', 'Difference_Valeur_Investie']])

#------------------------------------------------------------------------------

# Enregistrer le DataFrame filtré dans un fichier CSV
csv_path = 'Performance.csv'
df_filtre.to_csv(csv_path, index=False,sep=";")
print(f"Le fichier Performance.csv a été créé et enregistré.")