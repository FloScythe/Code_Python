import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import Qt  # Ajoutez cette ligne pour importer Qt
from Ajouter_Transaction import AjoutTransactionFenetre

class MaFenetre(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Interface avec Navigation et Affichage')
        self.setGeometry(100, 100, 800, 600)

        # Layouts
        layout_general = QVBoxLayout()
        layout_navigation = QVBoxLayout()
        layout_affichage = QVBoxLayout()

        # Bouton pour sélectionner un fichier CSV
        btn_selectionner = QPushButton('Sélectionner CSV', self)
        btn_selectionner.clicked.connect(self.selectionnerFichierCSV)
        
        # Bouton pour ouvrir la fenêtre d'ajout de transaction
        btn_ajout_transaction = QPushButton('Ajouter Transaction', self)
        btn_ajout_transaction.clicked.connect(self.ajouter_Transaction)

        # Boutons de navigation
        btn_portfolio = QPushButton('Portfolio', self)
        btn_rendement = QPushButton('Performance', self)

        # Bouton pour quitter l'application
        btn_quitter = QPushButton('Quitter', self)
        btn_quitter.clicked.connect(self.close)

        # Widgets pour affichage des données
        label_affichage = QLabel('Zone d\'affichage')
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(3)
        self.table_widget.setRowCount(5)
        self.table_widget.setHorizontalHeaderLabels(['Colonne 1', 'Colonne 2', 'Colonne 3'])

        # Connecter le bouton Rendement à la fonction correspondante
        btn_rendement.clicked.connect(self.executerMainEtChargerRendement)

        # Ajout des boutons de navigation et de sélection au layout_navigation
        layout_navigation.addWidget(btn_selectionner)
        layout_navigation.addWidget(btn_portfolio)
        layout_navigation.addWidget(btn_rendement)
        layout_navigation.addWidget(btn_ajout_transaction)  # Nouveau bouton pour ajouter manuellement des transactions


        # Ajout des widgets d'affichage au layout_affichage
        layout_affichage.addWidget(label_affichage)
        layout_affichage.addWidget(self.table_widget)  # Initialisation avec le tableau

        # Ajout des layouts de navigation et d'affichage au layout_general
        layout_general.addLayout(layout_navigation)
        layout_general.addLayout(layout_affichage)
        layout_general.addWidget(btn_quitter, alignment=Qt.AlignBottom | Qt.AlignRight)  # Bouton Quitter en bas à droite

        # Définir le layout principal de la fenêtre
        self.setLayout(layout_general)

    def selectionnerFichierCSV(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # Ouvrir le dialogue de sélection de fichier
        fichier, _ = QFileDialog.getOpenFileName(self, "Sélectionner un fichier CSV", "", "Fichiers CSV (*.csv);;Tous les fichiers (*)", options=options)

        # Vérifier si un fichier a été sélectionné
        if fichier:
            # Charger le contenu du fichier CSV dans le QTableWidget
            self.chargerContenuCSV(fichier)

    def chargerContenuCSV(self, fichier):
        try:
            with open(fichier, 'r') as file:
                lines = file.readlines()

                # Supprimer les anciennes données du QTableWidget
                self.table_widget.setRowCount(0)

                # Utiliser le séparateur ";" pour diviser la première ligne et déterminer le nombre de colonnes
                if lines:
                    header_items = lines[0].strip().split(';')
                    num_columns = len(header_items)

                    # Ajuster le nombre de colonnes du QTableWidget
                    self.table_widget.setColumnCount(num_columns)
                    self.table_widget.setHorizontalHeaderLabels(header_items)

                    # Ajouter les nouvelles données du fichier CSV avec le séparateur ";"
                    for line in lines[1:]:
                        items = line.strip().split(';')
                        rowPosition = self.table_widget.rowCount()
                        self.table_widget.insertRow(rowPosition)

                        for column, item in enumerate(items):
                            self.table_widget.setItem(rowPosition, column, QTableWidgetItem(item))

        except Exception as e:
            print(f"Erreur lors du chargement du fichier CSV : {e}")

    def executerMainEtChargerRendement(self):
        # Exécuter main.py
        subprocess.run(["python", "main.py"])

        # Après l'exécution, charger le fichier "Rendement.csv" dans le QTableWidget
        self.chargerContenuCSV("Rendement.csv")
    
    """
    Liée l'interface Ajouter_transaction a la fenetre principale'
    """
    def ajouter_Transaction(self):
        # Créer et afficher la fenêtre d'ajout de transaction
        ajout_transaction_fenetre = AjoutTransactionFenetre(self)
        ajout_transaction_fenetre.show()
        
        # Cacher la fenêtre principale
        self.hide()


    def reafficher(self):
        # Réafficher la fenêtre principale lorsque la fenêtre "Ajouter transaction" est fermée
        self.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec_())
