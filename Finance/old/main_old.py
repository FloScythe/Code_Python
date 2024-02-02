import pandas as pd
import yfinance as yf
from datetime import datetime
import os
import matplotlib.pyplot as plt

file_path = 'Data/Data.csv'
df = pd.read_csv(file_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])
#Date du jour
date_specifiee = datetime.today()
# Récupérer la première date présente dans le fichier "Data.CSV"
premiere_date = df['Date'].min()
#--------------------------------------------------------------------------------
# Utilisation de yf.download pour récupérer les données en une seule requête
tickers = df['Tickers'].unique().tolist()
tickers.remove('Cash')
data = yf.download(tickers, start=df['Date'].min(), end=date_specifiee)['Close'].round(3)
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
somme_journalier.append(restant_cash)
    
df_resultats = pd.DataFrame(resultats)
# Enregistrer le DataFrame dans un fichier Excel
csv_path = 'Rendement.csv'
df_resultats.to_csv(csv_path, index=False,sep=";")
print(f"Les résultats ont été enregistrés dans {csv_path}")
#--------------------------------------------------------------------------------

tickers.append('Cash')
for i, ticker in enumerate(tickers):
    somme_ticker = somme_journalier[i]
    repartition = round(somme_ticker / valeur_portefeuille * 100, 2)
    print(f"La part de {ticker} est de : {repartition}%")
#--------------------------------------------------------------------------------

#Calculer la performance
df = pd.read_csv(csv_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])

# Filtrer le DataFrame pour les dates spécifiées
df_filtre = df[(df['Date'] <= date_specifiee)]

# Calculer la différence de valeur investie entre date_specifiee et date_debut
df_filtre['Difference_Valeur_Investie'] = df_filtre['Valeur investie'].diff().round(3)
df_filtre.loc[df_filtre.index[0], 'Difference_Valeur_Investie'] = 0

# Calculer la colonne 'HP'
df_filtre['HP'] = round(1 + (df_filtre['Valeur du portefeuille'] - (df_filtre['Valeur du portefeuille'].shift(1) + df_filtre['Difference_Valeur_Investie'])) / (df_filtre['Valeur du portefeuille'].shift(1) + df_filtre['Difference_Valeur_Investie']),3)
df_filtre.loc[df_filtre.index[0], 'HP'] = 1

df_filtre.to_csv(csv_path, index=False,sep=";")

df = pd.read_csv(csv_path, delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])

df_annee = df['Date'].dt.year.unique()

for date in df_annee :
    df_filtre = df[df['Date'].dt.year == date]    
    performance = (df_filtre['HP'].prod() - 1)
    performance_percent = round(performance*100,2)
    print(f"la performance de l'année {date} : {performance_percent}%")
    

performance = round((valeur_portefeuille/somme_depot-1)*100,2)
print(f"la performance toutes années confondues : {performance}%")

#--------------------------------------------------------------------------------
"""
# Créer un graphique en quartier avec la répartition du portefeuille

labels = tickers
sizes = [round(somme / valeur_portefeuille * 100, 2) for somme in somme_journalier]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops=dict(weight='bold', fontsize=10), shadow=True)

ax.axis('equal')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Open Sans, Arial, sans-serif'

plt.title("Répartition du portefeuille", fontsize=16, fontweight='bold')

plt.show()


# Charger les données depuis le fichier rendement.csv
df = pd.read_csv('rendement.csv', delimiter=';')
df['Date'] = pd.to_datetime(df['Date'])

# Créer un graphique avec des courbes en aire
plt.figure(figsize=(10, 6))

# Courbe en aire pour la "Valeur du portefeuille"
plt.fill_between(df['Date'], df['Valeur du portefeuille'], color='skyblue', alpha=0.4, label='Valeur du portefeuille')

# Courbe en aire pour la "Somme déposée"
plt.fill_between(df['Date'], df['Valeur investie'], color='salmon', alpha=0.4, label='Valeur investie')

# Configurer l'axe des x avec les dates
plt.xlabel('Date')
plt.ylabel('Montant')
plt.title('Évolution de la Valeur du Portefeuille comparé à la valeur investie')
plt.ylim(25000, None)  # Commencer à 20000, laisser la limite supérieure automatique

plt.legend()
plt.grid(True)
plt.show()
"""