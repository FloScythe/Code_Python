import pandas as pd
import yfinance as yf
from datetime import datetime
import logging
import os

# Configurer le module de journalisation
logging.basicConfig(filename='logfile.log', level=logging.ERROR)

file_path = 'Rendement.csv'
df = pd.read_csv(file_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])

#Date du jour
#date_specifiee = datetime.today()

#Date pour les tests
#date_specifiee = datetime(2022,1,21)

#--------------------------------------------------------------------------------

