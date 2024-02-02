import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTableWidget, QTabWidget
#------------------------------------------------------------------------------

class Fenetre(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Choisir un fichier'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        # Ajout du bouton Selection
        btn_selection = QPushButton('Selection', self)
        btn_selection.move(400, 450)
        #btn_selection.clicked.connect()
        
        btn_quitter = QPushButton('Quitter', self)
        btn_quitter.move(500, 450)
        btn_quitter.clicked.connect(self.closeApplication)

        # Création des layouts
        layout_general = QHBoxLayout()
        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()
        """          
        # Ajout de la table
        self.tableWidget = QTableWidget(self)
        onglets = QTabWidget(self)
        onglets.addTab(self.tableWidget, "Test")
        """  

        # Ajout des boutons au premier layout vertical
        layout_general.addWidget(btn_quitter)
        layout_general.addWidget(btn_selection)

        # Ajout d'autres widgets (si nécessaire) au deuxième layout vertical
        # Exemple : 
        widget = QWidget()
        layout_1.addWidget(widget)

        # Ajout d'autres widgets (si nécessaire) au deuxième layout vertical
        # Exemple : 
        widget = QWidget()
        layout_2.addWidget(widget)

        # Configuration du layout général pour la fenêtre
        self.setLayout(layout_general)
        
        # Ajout des boutons au premier layout vertical
        layout_1.addWidget(btn_quitter)
        layout_1.addWidget(btn_selection)
    
    def closeApplication(self):
        QApplication.closeAllWindows()
           
    """
    def mousePressEvent(self, event):
        print("appui souris")
        
    """
    
#------------------------------------------------------------------------------    

# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication
app = QApplication.instance() 
if not app: # sinon on crée une instance de QApplication
    app = QApplication(sys.argv)
#------------------------------------------------------------------------------    

fen = Fenetre()

fen.show()
# exécution de l'application, l'exécution permet de gérer les événements
app.exec_()