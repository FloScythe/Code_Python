#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:35:19 2024

@author: flos

Sert à ajouter des transaction au fichier
"""

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFormLayout

class AjoutTransactionFenetre(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Ajouter une transaction')
        self.setGeometry(200, 200, 400, 300)

        # Widgets
        self.date_edit = QLineEdit(self)
        self.action_edit = QLineEdit(self)
        self.tickers_edit = QLineEdit(self)
        self.quantite_edit = QLineEdit(self)
        self.cours_edit = QLineEdit(self)
        self.gestion_edit = QLineEdit(self)

        # Bouton Ajouter
        btn_ajouter = QPushButton('Ajouter', self)
        btn_ajouter.clicked.connect(self.ajouterTransaction)

        # Layout
        layout = QFormLayout()
        layout.addRow('Date (YYYY-MM-DD):', self.date_edit)
        layout.addRow('Action:', self.action_edit)
        layout.addRow('Tickers:', self.tickers_edit)
        layout.addRow('Quantité:', self.quantite_edit)
        layout.addRow('Cours:', self.cours_edit)
        layout.addRow('Gestion (%):', self.gestion_edit)
        layout.addRow(btn_ajouter)

        self.setLayout(layout)

    def ajouterTransaction(self):
        # Récupérer les valeurs des champs
        date = self.date_edit.text()
        action = self.action_edit.text()
        tickers = self.tickers_edit.text()
        quantite = self.quantite_edit.text()
        cours = self.cours_edit.text()
        gestion = self.gestion_edit.text()

        # Effectuer des opérations avec ces valeurs (par exemple, les imprimer)
        print(f'Date: {date}, Action: {action}, Tickers: {tickers}, Quantité: {quantite}, Cours: {cours}, Gestion: {gestion}')

        # Fermer la fenêtre après l'ajout
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    fenetre = AjoutTransactionFenetre()
    fenetre.show()
    app.exec_()
