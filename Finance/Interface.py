import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface PyQt5")
        self.setGeometry(100, 100, 400, 300)

        # Création des boutons
        button1 = QPushButton("Bouton 1", self)
        button2 = QPushButton("Bouton 2", self)
        button3 = QPushButton("Bouton 3", self)
        button4 = QPushButton("Bouton 4", self)

        # Création du tableau
        table = QTableWidget(self)
        table.setColumnCount(1)
        table.setRowCount(5)
        table.setHorizontalHeaderLabels(["Table"])
        
        #Création des layouts
        layout_general = QHBoxLayout()
        layout_nav = QVBoxLayout()
        layout_table = QVBoxLayout()
        
        #Ajout des layouts au layout general
        layout_general.addLayout(layout_nav)
        layout_general.addLayout(layout_table)
        
        # Ajout des boutons au layout vertical
        layout_nav.addWidget(button1)
        layout_nav.addWidget(button2)
        layout_nav.addWidget(button3)
        layout_nav.addWidget(button4)
        layout_table.addWidget(table)

        # Création du widget central
        central_widget = QWidget()
        central_widget.setLayout(layout_nav)
        self.setCentralWidget(central_widget)

        # Bouton "Quitter"
        quit_button = QPushButton("Quitter", self)
        quit_button.move(300, 250)
        quit_button.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
