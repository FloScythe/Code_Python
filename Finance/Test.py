import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import logging

# Fonction pour télécharger les données boursières
def download_stock_data(tickers, start_date, end_date):
    try:
        data = yf.download(tickers, start=start_date, end=end_date)['Close']
        return data
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des données : {e}")
        return pd.DataFrame()

# Fonction pour calculer la valeur du portefeuille
def calculate_portfolio_value(file_path, date):
    df = pd.read_csv(file_path, delimiter=';')

    df['Date'] = pd.to_datetime(df['Date'])

    df_filter = df[df['Date'] <= date]
    tickers = df_filter['Tickers'].unique().tolist()

    data = download_stock_data(tickers, df_filter['Date'].min(), date)['Close']

    buy_df = df_filter[df_filter['Action'] == 'Achat']
    buy_amounts_per_stock = buy_df.groupby('Tickers')['Montant'].sum()
#--------------------------------------------
    deposit_sum = df_filter[df_filter['Action'] == 'Depot']['Montant'].sum()
    buy_sum = buy_amounts_per_stock.sum()
    sell_sum = df_filter[df_filter['Action'] == 'Vente']['Montant'].sum()
    cash_sum = deposit_sum - buy_sum - sell_sum

    stock_product = data.iloc[-1].mul(df_filter.groupby('Tickers')['Quantite'].sum(), fill_value=0)
    portfolio_value = stock_product.sum() + cash_sum
    
    return portfolio_value,buy_amounts_per_stock

# Configurer le module de journalisation
logging.basicConfig(filename='logfile.log', level=logging.ERROR)

file_path = 'Data/Data.csv'
start_date = datetime(2024, 1, 15)
today_date = datetime.today()

df = pd.read_csv(file_path, delimiter=';')

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

df_filter = df[df['Date'] <= start_date]

# Utilisation de yf.download pour récupérer les données en une seule requête
tickers = df_filter['Tickers'].unique().tolist()

try:
    data = download_stock_data(tickers, df_filter['Date'].min(), start_date)
except Exception as e:
    logging.error(f"Erreur lors de la récupération des données : {e}")
    data = pd.DataFrame()

# Calculer la somme des espèces restantes
deposit_sum = df_filter[df_filter['Action'] == 'Depot']['Montant'].sum()
# Appeler la fonction pour calculer la valeur du portefeuille et obtenir buy_amounts_per_stock
portfolio_value, buy_amounts_per_stock = calculate_portfolio_value(file_path, start_date)

buy_sum = buy_amounts_per_stock.sum()
sell_sum = df_filter[df_filter['Action'] == 'Vente']['Montant'].sum()
cash_sum = deposit_sum - buy_sum - sell_sum

# Initialiser le DataFrame pour stocker les rendements
returns_df = pd.DataFrame(columns=['Date', 'Valeur du portefeuille', 'Total Depose', 'Difference', 'HP'])

# Boucle pour chaque jour entre la date de début et la date de fin
current_date = start_date

while current_date <= today_date:
    # Filtrer les transactions jusqu'à la date actuelle
    transactions_day = df_filter[df_filter['Date'] == current_date]

    # Calculer la somme des dépôts jusqu'à la date actuelle
    total_deposit = df_filter[df_filter['Date'] <= current_date][df_filter['Action'] == 'Depot']['Montant'].sum()
    
    # Récupérer la valeur du portefeuille pour la date actuelle
    portfolio_value = calculate_portfolio_value(file_path, current_date)
        
    if not returns_df.empty:
        difference = total_deposit - returns_df['Total Depose'].shift(1).loc[returns_df['Date'] == current_date - timedelta(days=1)].values[0]
    else:
        difference = 0    
      
    # Calculer le HP (Holding Period Return) avec la formule spécifiée
    hp = 1 + (portfolio_value - (returns_df['Valeur du portefeuille'].shift(1) + difference)) / (returns_df['Valeur du portefeuille'].shift(1) + difference)

    # Ajouter les résultats au DataFrame
    returns_df = pd.concat([returns_df, pd.DataFrame({
        'Date': [current_date],
        'Valeur du portefeuille': [portfolio_value],
        'Total Depose': [total_deposit],
        'Difference': [difference],
        'HP': [hp]
    })], ignore_index=True)
    
    # Passer à la date suivante
    current_date += timedelta(days=1)

# Sauvegarder le DataFrame dans un fichier Excel
returns_df.to_excel('Rendement.xlsx', index=False)
