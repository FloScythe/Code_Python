#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:47:00 2024

@author: flos
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget
import pandas as pd
import subprocess

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Choisir un fichier'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Ajout du bouton Quitter
        btn_quitter = QPushButton('Quitter', self)
        btn_quitter.setToolTip('Cliquez ici pour quitter l\'application')
        btn_quitter.move(500, 450)
        btn_quitter.clicked.connect(self.closeApplication)
        
        
        # Ajout du bouton Selectionner
        btn_selectionner = QPushButton('Selectionner', self)
        btn_selectionner.setToolTip('Cliquez ici pour reselectionner un fichier')
        btn_selectionner.move(350, 450)
        btn_selectionner.clicked.connect(self.selectFile)  # Modifié ici


        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Choisir un fichier", "", "CSV Files (*.csv)", options=options)
        if fileName:
            print(fileName)
            # Exécuter le fichier main.py
            subprocess.run(["python", "main.py"])

        # Ajout de la table
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 350)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        # Lecture du fichier CSV
        df = pd.read_csv(fileName,sep=";")

        # Ajout des colonnes à la table
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        # Ajout des lignes à la table
        self.tableWidget.setRowCount(len(df.index))
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

        # Ajout d'un second onglet
        onglets = QTabWidget(self)
        onglets.setGeometry(50, 50, 500, 350)
        onglets.addTab(self.tableWidget, "Fichier CSV")
    
        # Lecture du fichier "Rendement.csv"
        df_rendement = pd.read_csv("Rendement.csv", sep=";")
        
        # Calcul des données nécessaires
        valeur_portefeuille = df_rendement["Valeur du portefeuille"].sum()
        montant_investi = df_rendement["Valeur investie"].sum()
        # Calcul des autres données selon vos besoins

        # Ajout d'une table pour les valeurs calculées
        table_calculs = QTableWidget(self)
        table_calculs.setGeometry(50, 50, 500, 350)
        
        # Mise à jour de la table dans le deuxième onglet
        table_calculs.setRowCount(len(df_rendement.index))
        table_calculs.setColumnCount(len(df_rendement.columns))
        table_calculs.setHorizontalHeaderLabels(df_rendement.columns)

        
        for i in range(len(df_rendement.index)):
            for j in range(len(df_rendement.columns)):
                table_calculs.setItem(i, j, QTableWidgetItem(str(df_rendement.iloc[i, j])))

        # Ajout de la table des valeurs calculées à l'onglet
        onglets.addTab(table_calculs, "Rendement")

    def resetUI(self):
        # Réinitialisez les éléments graphiques et les données au besoin
        self.tableWidget.clear()  # Effacez la table existante
        
    def closeApplication(self):
        QApplication.closeAllWindows()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
        
    sys.exit(app.exec_())

