import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from ttkthemes import ThemedTk

class MonApplication(ThemedTk):
    def __init__(self):
        super().__init__()

        self.set_theme("arc")  # Choisissez le thème ici (exemple: "arc", "clearlooks")

        self.title("Application de Portefeuille")
        self.geometry("800x600")

        self.file_path = tk.StringVar()

        # Interface utilisateur
        self.label = ttk.Label(self, text="Choisir un fichier CSV:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self, textvariable=self.file_path, width=50)
        self.entry.pack(pady=10)

        self.bouton_choisir_fichier = ttk.Button(self, text="Parcourir", command=self.choisir_fichier)
        self.bouton_choisir_fichier.pack(pady=10)

        self.bouton_executer = ttk.Button(self, text="Exécuter", command=self.executer_application)
        self.bouton_executer.pack(pady=10)

    def choisir_fichier(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
        self.file_path.set(file_path)

    def executer_application(self):
        file_path = self.file_path.get()

        if file_path:
            self.analyser_donnees(file_path)
            self.generer_graphiques()

    def analyser_donnees(self, file_path):
        df = pd.read_csv(file_path, delimiter=';')
        df['Date'] = pd.to_datetime(df['Date'])

        date_specifiee = datetime.today()
        premiere_date = df['Date'].min()

        tickers = df['Tickers'].unique().tolist()
        tickers.remove('Cash')
        data = yf.download(tickers, start=df['Date'].min(), end=date_specifiee)['Close'].round(3)

        resultats = []

        for date in pd.date_range(start=premiere_date, end=date_specifiee - pd.Timedelta(days=1), freq='D'):
            df_date = df[df['Date'] <= date]
            df_cash = df_date[df_date['Tickers'] == 'Cash']
            cash = df_cash['Quantite'].sum()

            somme_journalier = []
            for ticker in tickers:
                somme_action = df_date[df_date['Tickers'] == ticker]['Quantite'].sum()

                try:
                    valeur_actions_date = data.loc[date, ticker]
                except KeyError:
                    valeur_actions_date = data.loc[date, ticker] if date in data.index else data[ticker].shift(-1).loc[:date].dropna().iloc[-1]

                valeur_ticker = round(valeur_actions_date * somme_action, 3)
                somme_journalier.append(valeur_ticker)

            somme_depot = df_date[df_date['Action'] == 'Depot']['Montant'].sum()
            somme_achat = df_date[df_date['Action'] == 'Achat']['Montant'].sum()
            somme_vente = df_date[df_date['Action'] == 'Vente']['Montant'].sum()
            restant_cash = somme_depot - somme_achat - somme_vente

            valeur_portefeuille = round(sum(somme_journalier, restant_cash), 3)

            resultats.append({
                'Date': date,
                'Valeur du portefeuille': valeur_portefeuille,
                'Valeur investie': cash
            })

        self.df_resultats = pd.DataFrame(resultats)
        self.df_resultats.to_csv('Rendement.csv', index=False, sep=";")

    def generer_graphiques(self):
        plt.figure(figsize=(10, 6))
        plt.fill_between(self.df_resultats['Date'], self.df_resultats['Valeur du portefeuille'], color='skyblue', alpha=0.4, label='Valeur du portefeuille')
        plt.fill_between(self.df_resultats['Date'], self.df_resultats['Valeur investie'], color='salmon', alpha=0.4, label='Valeur investie')
        plt.xlabel('Date')
        plt.ylabel('Montant')
        plt.title('Évolution de la Valeur du Portefeuille comparé à la valeur investie')
        plt.ylim(20000, None)
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    app = MonApplication()
    app.mainloop()
