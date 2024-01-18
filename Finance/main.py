import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

def calcul_valeur_portefeuille(date, ticker):
    # Lire le fichier CSV
    data = pd.read_csv('Data/Data.csv', delimiter=';')

    # Convertir la colonne "Date" en datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

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
        # Retourner la valeur totale pour permettre à la fonction appelante de l'utiliser
        return round(valeur_total,3)
    else:
        # Si la quantité est zéro, retourner 0 (ou une autre valeur par défaut)
        return 0


def dernier_jour_ouvre_avant_ou_veille(date):
    # Convertir la date en datetime
    date = pd.to_datetime(date)

    # Trouver la date de la veille
    veille = date - timedelta(days=1)

    while veille.weekday() >= 5 or veille.strftime('%Y-%m-%d') in holidays:
        veille -= pd.Timedelta(days=1)
        
    return veille


def recuperation_prix(date, ticker):
    # Convertir la date en datetime
    date = pd.to_datetime(date)

    # Trouver le dernier jour ouvré avant ou incluant la date
    last_business_day = dernier_jour_ouvre_avant_ou_veille(date)

    # Convertir la date en chaîne de caractères
    date_str_start = last_business_day.strftime('%Y-%m-%d')
    date_str_end = date.strftime('%Y-%m-%d')


    # Récupérer les données boursières d'une action précise
    data = yf.download(ticker, start=date_str_start, end=date_str_end)

    if not data.empty:
        # Récupérer la valeur de clôture de l'action
        last_value = round(data['Close'][0],3)
        return last_value
    else:
        # print(f"\nAucune donnée disponible pour {ticker} à la date {date_str_end}.")
        return 0


def calcul_valeur(quantite, prix):
    valeur = round(quantite * prix,3)
    return valeur


# Définir les dates
date_debut_str = "2022-01-10"
date_fin = datetime.now().date()
date_fin_str =  "2022-01-20" #date_fin.strftime('%Y-%m-%d')

# Convertir les chaînes de caractères en objets datetime
date_debut = datetime.strptime(date_debut_str, "%Y-%m-%d")
date_fin = datetime.strptime(date_fin_str, "%Y-%m-%d")

# Calculer la différence entre les deux dates
difference = date_fin - date_debut

# Extraire le nombre de jours à partir de la différence
nombre_de_jours = difference.days
# Afficher le résultat
# print(f"Il y a {nombre_de_jours} jours entre {date_debut_str} et {date_fin_str}.")

# Liste des jours fériés
holidays = ['2022-01-01', '2022-12-25']

#Liste des actions détenue
action = ['PE500.PA','PANX.PA','LQQ.PA','EWLD.PA']

# Date de recherche
date = '2023-06-25'

#-------------------------------Affichage et recherche du prix de l'action à un jour J--------------------------------------------
#------------------------------- Creation du fichier csv --------------------------------------------

try:
    df_valeur_portfolio = pd.read_csv('Valeur_portfolio.csv')
except FileNotFoundError:
    # Si le fichier n'existe pas encore, créer un DataFrame vide
    df_valeur_portfolio = pd.DataFrame(columns=['Date', 'Somme_valeur_total'])

#------------------------------- Debut de la vérification --------------------------------------------

#------------------------------- Creation de liste --------------------------------------------

# Initialiser les listes des dates et sommes
dates_portfolio = df_valeur_portfolio['Date'].tolist()
sommes_portfolio = df_valeur_portfolio['Somme_valeur_total'].tolist()

#------------------------------- Boucle a travers la liste --------------------------------------------
# Boucle à travers chaque jour
for i in range(nombre_de_jours + 1):  # +1 pour inclure également la date de début
    date_courante = (date_debut + timedelta(days=i)).strftime('%Y-%m-%d')

    # Vérifier si la date_courante est déjà présente dans "Valeur_portfolio"
    if date_courante in dates_portfolio:
        print(f"\nLa date {date_courante} est déjà présente dans 'Valeur_portfolio'. Passer à la date suivante.")
        continue
    
    # Si la date_courante n'est pas présente dans "Valeur_portfolio", effectuer la recherche de valeur
    somme_valeur_total_jour = 0  # Initialiser la somme pour la journée

    # Vérifier si la somme_valeur_total_jour est différente de 0
    if somme_valeur_total_jour == 0:
        print(f"La somme_valeur_total_jour pour la date {date_courante} est 0. Effectuer une nouvelle recherche de valeur.")
        
        # Répéter la recherche de valeur pour vérifier ce que la somme_valeur_total_jour soit différente de 0
        for action_ticker in action:
            valeur_total = calcul_valeur_portefeuille(date_courante, action_ticker)
            somme_valeur_total_jour += valeur_total
        print(f"Nouvelle somme_valeur_total_jour pour la date {date_courante} : {somme_valeur_total_jour}")
    
    # Ajouter la somme de la journée à la liste
    sommes_portfolio.append(somme_valeur_total_jour)
    dates_portfolio.append(date_courante)

# Mettre à jour le DataFrame avec les nouvelles données
df_valeur_portfolio = pd.DataFrame({
    'Date': dates_portfolio,
    'Somme_valeur_total': sommes_portfolio
})

# Écrire dans le fichier "Valeur_portfolio"
df_valeur_portfolio.to_csv('Valeur_portfolio.csv', index=False)

#--------------------------------------------------------------------------------------------------------------------------------
"""
date_limite = "20/01/2022"
soustraction_resultat = calcul_soustraction('Data/Data.csv', date_limite)

print(f"Le résultat de la soustraction jusqu'à la date {date_limite} est : {soustraction_resultat}")
"""