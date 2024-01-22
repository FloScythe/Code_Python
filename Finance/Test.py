import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import logging

# Configurer le module de journalisation
logging.basicConfig(filename='logfile.log', level=logging.ERROR)

file_path = 'Data/Data.csv'
date_specifiee = datetime(2022, 1, 31)

df = pd.read_csv(file_path, delimiter=';')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

df_filtre = df[df['Date'] <= date_specifiee]

# Utilisation de yf.download pour récupérer les données en une seule requête
tickers = df_filtre['Tickers'].unique().tolist()

try:
    data = yf.download(tickers, start=df_filtre['Date'].min(), end=date_specifiee)['Close']
except Exception as e:
    logging.error(f"Erreur lors de la récupération des données : {str(e)}")
    data = pd.DataFrame()

print(data)
