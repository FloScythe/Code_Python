import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget
import pandas as pd

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

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Choisir un fichier", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

        # Ajout du bouton Quitter
        btn_quitter = QPushButton('Quitter', self)
        btn_quitter.setToolTip('Cliquez ici pour quitter l\'application')
        btn_quitter.move(500, 450)
        btn_quitter.clicked.connect(self.close)

        # Ajout du bouton Selectionner
        btn_selectionner = QPushButton('Selectionner', self)
        btn_selectionner.setToolTip('Cliquez ici pour reselectionner un fichier')
        btn_selectionner.move(350, 450)
        btn_selectionner.clicked.connect(self.initUI)

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

        # Ajout d'une table pour les valeurs calculées
        table_calculs = QTableWidget(self)
        table_calculs.setGeometry(50, 50, 500, 350)
        table_calculs.setRowCount(1)
        table_calculs.setColumnCount(2)
        table_calculs.setHorizontalHeaderLabels(["Valeur", "Calcul"])

        # Ajout des valeurs calculées
        valeur_portefeuille = 10000
        calcul_portefeuille = "100 actions * 100€"
        table_calculs.setItem(0, 0, QTableWidgetItem(str(valeur_portefeuille)))
        table_calculs.setItem(0, 1, QTableWidgetItem(calcul_portefeuille))

        # Ajout de la table des valeurs calculées à l'onglet
        onglets.addTab(table_calculs, "Valeurs calculées")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
