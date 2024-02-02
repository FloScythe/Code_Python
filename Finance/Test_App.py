import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QFrame, QGridLayout, QWidget, QFileDialog, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget
from main import valeur_portefeuille, investi
import subprocess
import pandas as pd


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Suivi Financier'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        # Ajout d'un second onglet
        onglets = QTabWidget(self)
        onglets.setGeometry(50, 50, 500, 350)
        onglets.addTab(self.tableWidget, "Fichier CSV")
    

        # Add widgets
        self.create_widgets()

    def create_widgets(self):
        # Create grid layout
        grid_layout = QGridLayout()

        # Add labels to grid layout
        grid_layout.addWidget(QLabel(f'Valeur du portefeuille €{portfolio_value:.2f}'), 0, 0)
        grid_layout.addWidget(QLabel(f'Montant total investi €{total_invested:.2f}'), 1, 0)
        grid_layout.addWidget(QLabel(f'Plus / Moins Value latente {latent_value:.2f}% €{latent_amount:.2f}'), 2, 0)
        grid_layout.addWidget(QLabel(f'Performance Annualisée {annualized_performance:.2f}% VS S&P 500 {sp500_performance:.2f}%'), 0, 1)
        grid_layout.addWidget(QLabel(f'{days_since_pea} Jours depuis la création du PEA {pea_age}'), 1, 1)
        grid_layout.addWidget(QLabel(f'Patrimoine le plus haut atteint {wealth_date} €{wealth_value:.2f}'), 2, 1)
        grid_layout.addWidget(QLabel(f'Cash restant à investir €{remaining_cash:.2f}'), 3, 1)

        # Set grid layout as central widget
        central_widget = QFrame(self)
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)

        # Add combo box for time frames
        time_combo = QComboBox(self)
        time_combo.setGeometry(600, 550, 100, 30)
        time_combo.addItems(['1j', '5j', '1m', 'AAJ', '1a', '5a', 'max'])

if __name__ == '__main__':
    # Define variables homonymes
    portfolio_value = valeur_portefeuille
    total_invested = investi
    latent_value = ((valeur_portefeuille/investi)-1)*100
    latent_amount = valeur_portefeuille - investi
    annualized_performance = 6.02
    sp500_performance = 0.00
    days_since_pea = 2024
    pea_age = 750
    wealth_date = '1/30/2024'
    wealth_value = 55237.09
    remaining_cash = 4.74

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
