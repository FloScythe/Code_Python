import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV
data = pd.read_csv('Data/Data.csv', delimiter=';')

# Compter le nombre d'occurrences de chaque nom de la colonne "Tickers"
counts = data['Tickers'].value_counts()

# Retirer une valeur spécifique
counts = counts.drop('Cash')

# Afficher un graphique en barres
counts.plot(kind='bar')

"""
Différent type de grapphique :
    
Graphique en barres : df.plot(kind='bar')
Graphique en barres empilées : df.plot(kind='bar', stacked=True)
Graphique en histogramme : df.plot(kind='hist')
Graphique en boîte : df.plot(kind='box')
Graphique en nuage de points : df.plot(kind='scatter', x='x_column', y='y_column')
Graphique en secteurs : df.plot(kind='pie')
Graphique en surface : df.plot(kind='surface')
Graphique en densité : df.plot(kind='density')
"""

# Ajouter un titre et des étiquettes d'axe
plt.title('Occurrences de chaque nom de la colonne "Tickers"')
plt.xlabel('Nom de la colonne "Tickers"')
plt.ylabel('Nombre d\'occurrences')

# Afficher le graphique
plt.show()
