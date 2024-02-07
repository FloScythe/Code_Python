"""
Code de création du tableau de portefeuille

#################################################################################
#                               Les Grands Chiffres                             #
#################################################################################

#################################               #################################       
#       Valeur portfeuille      #               #     Performance Annualisée    #
#################################               #################################

#################################               ################################# 
#     Montant total investi     #               #Jours depuis la création du PEA#
#################################               #################################

#################################               #################################       
#   Plus / Moins Value latente  #               #Patrimoine le plus haut atteint#
#################################               #################################

#################################               #################################       
#     Plus Value réalisée       #               #   Cash restant à investir     #
#################################               #################################

"""

from PyQt5.QtWidgets import QWidget, QLabel,QVBoxLayout,QApplication,QHBoxLayout
import sys
from main import valeur_portefeuille,investi,cash
class PortfolioInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Portfolio')
        self.setGeometry(200, 200, 400, 300)
        
        # Labels pour afficher les informations du Portfolio
        label_grands_chiffres = QLabel('Les grands chiffres', self)
        label_valeurs_portfolio = QLabel(f'Valeurs du portefeuille : {valeur_portefeuille} €', self)  
        label_montant_investi = QLabel(f'Montant total investi : {investi} €', self)  
        #label_plus_value = QLabel(f'Plus-value : {plus_value} €', self)  
        
        #label_performance_annualisee = QLabel(f'Performance annualisée : {performance_annualisee} %', self)  
        #label_jours_depuis_creation = QLabel(f'Jours depuis la création : {jours_depuis_creation} jours', self)  
        #label_patrimoine_le_plus_haut = QLabel(f'Patrimoine le plus haut : {patrimoine_le_plus_haut} €', self)  
        label_cash = QLabel(f'Cash restant : {cash} €', self)  

        # Layout genral
        layout_genral = QHBoxLayout()
        
        # Layout1
        layout1 = QVBoxLayout()
        layout1.addWidget(label_grands_chiffres)
        layout1.addWidget(label_valeurs_portfolio)
        layout1.addWidget(label_montant_investi)
        
        # Layout2
        layout2 = QVBoxLayout()
        #layout2.addWidget(label_Performance Annualisée)
        layout2.addWidget(label_valeurs_portfolio)
        layout2.addWidget(label_montant_investi)
        
        layout_genral.addLayout(layout1)
        layout_genral.addLayout(layout2)


        self.setLayout(layout_genral)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = PortfolioInterface()
    fenetre.show()
    sys.exit(app.exec_())