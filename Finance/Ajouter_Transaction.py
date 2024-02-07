from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFormLayout, QComboBox, QDateEdit
from PyQt5.QtCore import Qt, pyqtSignal
import csv,sys

class AjoutTransactionFenetre(QWidget):
    # Définir un signal personnalisé pour indiquer la fermeture de la fenêtre
    fermeture = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Ajouter une transaction')
        self.setGeometry(200, 200, 400, 300)

        # Widgets
        self.date_edit = QDateEdit(self)  # Utilisation de QDateEdit pour la sélection de la date
        self.date_edit.setCalendarPopup(True)  # Afficher le calendrier lorsque l'utilisateur clique sur la zone de texte
        
        self.action_combo = QComboBox(self)
        self.action_combo.addItems(["Dépôt", "Achat", "Vente"])
        
        self.tickers_combo = QComboBox(self)
        self.tickers_combo.addItems(["PE500.PA", "PANX.PA", "EWLD.PA","LQQ.PA"])
        
        self.quantite_edit = QLineEdit(self)
        self.cours_edit = QLineEdit(self)
        self.gestion_edit = QLineEdit(self)

        #Bouton Ajouter
        btn_ajouter = QPushButton('Ajouter', self)
        btn_ajouter.clicked.connect(self.ajouterTransaction)
        
        # Bouton pour quitter l'application
        btn_quitter = QPushButton('Quitter', self)
        btn_quitter.clicked.connect(self.close)

        # Layout
        layout = QFormLayout()
        layout.addRow('Date:', self.date_edit)
        layout.addRow('Action:', self.action_combo)
        layout.addRow('Tickers:', self.tickers_combo)
        layout.addRow('Quantité:', self.quantite_edit)
        layout.addRow('Cours:', self.cours_edit)
        layout.addRow('Gestion (%):', self.gestion_edit)
        layout.addRow(btn_ajouter)
        layout.addRow(btn_quitter)

        self.setLayout(layout)

    def closeEvent(self, event):
        # Émettre le signal de fermeture de la fenêtre
        self.fermeture.emit()
        event.accept()

    def ajouterTransaction(self):
        try :
            # Récupérer les valeurs des champs
            date = self.date_edit.date().toString('yyyy-M-d')  # Convertir la date en format 'YYYY-MM-DD'
            action = self.action_combo.currentText()
            tickers = self.tickers_combo.currentText()
            quantite = self.quantite_edit.text()
            cours = self.cours_edit.text()
            gestion = self.gestion_edit.text()
            somme_ht = round((int(quantite) * float(cours)),3)
            commission = round((float(somme_ht) * float(gestion)),3)
            montant = round((float(somme_ht)+float(commission)),3)
            
            # Convertir la valeur de Gestion en pourcentage
            gestion_en_pourcentage = f"{float(gestion):.2%}"
            
            # Créer un dictionnaire avec les données de la nouvelle transaction
            nouvelle_transaction = {
                'Date': date,
                'Action': action,
                'Tickers': tickers,
                'Quantité': quantite,
                'Cours': cours,
                'Somme_HT': somme_ht,
                'Gestion': gestion_en_pourcentage,
                'Commission': commission,
                'Montant': montant
            }
    
            # Ouvrir le fichier CSV en mode append
            with open('Data/data.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=nouvelle_transaction.keys(),delimiter=';')
    
                # Si le fichier est vide, écrire l'en-tête
                if file.tell() == 0:
                    writer.writeheader()
    
                # Écrire la nouvelle transaction
                writer.writerow(nouvelle_transaction)
    
            # Fermer la fenêtre après l'ajout
            self.close()
            
        except ValueError:
            print("Erreur: Assurez-vous que les champs Quantité, Cours et Gestion sont des nombres valides.")
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = AjoutTransactionFenetre()
    fenetre.show()
    sys.exit(app.exec_())