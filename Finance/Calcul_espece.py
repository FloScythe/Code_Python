import pandas as pd
import yfinance as yf
from datetime import datetime

def recuperation_prix(date, ticker):
    if ticker == 'Cash':
        return 0  # Ignorer le tickers "Cash"

    # Convertir la date en datetime
    date = pd.to_datetime(date)

    # Convertir la date en chaîne de caractères
    date_str_start = "2022-2-18"
    date_str_end = "2022-2-20"

    # Récupérer les données boursières d'une action précise
    data = yf.download(ticker, start=date_str_start)
    
    if not data.empty:
        # Récupérer la valeur de clôture de l'action
        last_value = round(data['Close'][0], 3)
        print(f"\nLa valeur de clôture de l'action {ticker} à la date {date_str_start} est de : {last_value}")
        return last_value
    else:
        print(f"\nAucune donnée disponible pour {ticker} à la date {date_str_start}.")
        return 0
    
date = "2022-2-18"
ticker = "PE500.PA"
data = recuperation_prix(date, ticker)