from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, \
    QLabel, QMessageBox, QFileDialog, QMenuBar, QMenu, QAbstractItemView
from functools import partial
import pandas as pd
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Charger la feuille de style
        with open("style.css", "r") as f:
            style = f.read()
        # Appliquer la feuille de style à l'application entière
        app.setStyleSheet(style)

        # Définir le titre de la fenêtre
        self.setWindowTitle("Classification des transactions")
        # Définir la taille de la fenêtre
        self.setGeometry(100, 100, 800, 600)
        # Créer la barre de menu
        self.menu_bar = QMenuBar()
        # Créer le menu "Fichier"
        self.file_menu = QMenu("Fichier", self)
        # Créer les actions "Enregistrer" et "Charger"
        self.save_action = self.file_menu.addAction("Enregistrer")
        self.load_action = self.file_menu.addAction("Charger")
        # Ajouter un séparateur
        self.file_menu.addSeparator()
        # Créer l'action "Quitter"
        self.quit_action = self.file_menu.addAction("Quitter")

        # Connecter les actions à leurs fonctions correspondantes
        self.save_action.triggered.connect(self.save_data)
        self.load_action.triggered.connect(self.load_data)
        self.quit_action.triggered.connect(self.close)

        # Ajouter le menu "Fichier" à la barre de menu
        self.menu_bar.addMenu(self.file_menu)
        # Définir la barre de menu de la fenêtre
        self.setMenuBar(self.menu_bar)

        # Créer les listes pour chaque catégorie
        self.list_widget_general = QListWidget()
        self.list_widget_charges_foyer = QListWidget()

        # Configurer le mode de sélection des listes
        self.list_widget_general.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Créer les labels pour chaque liste
        self.label_general = QLabel("Général")

        # Créer les boutons
        self.category_buttons = {}
        # Créer le layout pour les boutons
        self.button_layout = QVBoxLayout()
        for category in ['Charges du foyer', 'Bourse', 'Épargne', 'Charges personnelles', 'Dépenses personnelles',
                         'Restaurant', 'Note de frais', 'Course annexe', 'Travail', 'Santé', 'Annexe']:
            button = QPushButton(f'{category} (0)')
            button.clicked.connect(partial(self.classify_transaction, category))
            self.category_buttons[category] = button
            self.button_layout.addWidget(button)

        self.button_remove_category = QPushButton("Supprimer la catégorie")

        # Connecter les boutons à leurs fonctions correspondantes
        self.button_remove_category.clicked.connect(self.remove_category)

        # Créer le layout pour les boutons
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.button_remove_category)

        # Créer le layout pour chaque liste et son label
        self.layout_general = QVBoxLayout()
        self.layout_general.addWidget(self.label_general)
        self.layout_general.addWidget(self.list_widget_general)

        # Créer le layout principal
        self.layout = QHBoxLayout()

        # Ajouter les layouts à la mise en page principale
        self.layout.addLayout(self.layout_general)
        self.layout.addLayout(self.button_layout)

        # Créer un widget central pour la fenêtre
        self.central_widget = QWidget()
        # Appliquer le layout au widget central
        self.central_widget.setLayout(self.layout)
        # Définir le widget central de la fenêtre
        self.setCentralWidget(self.central_widget)

        # Lire les données
        self.data = pd.DataFrame()

    def toggle_category(self):
        # Get the category from the button that sent the signal
        category = self.sender().text().split(' ')[0]
        print(f"Toggle category: {category}")

    def save_data(self):
        # Ouvrir le dialogue de fichier pour sélectionner un emplacement pour enregistrer
        filename, _ = QFileDialog.getSaveFileName(self, "Enregistrer", "", "CSV Files (*.csv)")

        if filename:
            try:
                # Écrire les données dans un nouveau fichier CSV
                self.data.to_csv(filename, sep=';', index=False)
            except Exception as e:
                # Afficher un message d'erreur
                QMessageBox.critical(self, "Erreur", str(e))

    def load_data(self):
        # Ouvrir le dialogue de fichier pour sélectionner un fichier à charger
        filename, _ = QFileDialog.getOpenFileName(self, "Charger", "", "CSV Files (*.csv)")

        if filename:
            # Définir les noms des colonnes
            column_names = ["Date", "Montant", "Méthode", "Compte", "Nom", "Information", "0", "Catégorie"]

            try:
                # Lire le fichier CSV
                self.data = pd.read_csv(filename, sep=';', header=None, names=column_names)

                # Vider les listes
                self.list_widget_general.clear()
                self.list_widget_charges_foyer.clear()
                self.list_widget_bourse.clear()
                self.list_widget_epargne.clear()
                self.list_widget_charge_personelle.clear()
                self.list_widget_depense_personnelle.clear()
                self.list_widget_restaurant.clear()
                self.list_widget_note_de_frais.clear()
                self.list_widget_course_annexe.clear()
                self.list_widget_travail.clear()
                self.list_widget_sante.clear()
                self.list_widget_annexe.clear()

                # Ajouter les transactions aux listes correspondantes
                for index, row in self.data.iterrows():
                    item = f"{row['Nom']} ; {row['Montant']} ; {row['Date']}"
                    self.list_widget_general.addItem(item)
                    if row['Catégorie'] == 'Charges du foyer':
                        self.list_widget_charges_foyer.addItem(item)
                    elif row['Catégorie'] == 'Bourse':
                        self.list_widget_bourse.addItem(item)
                    elif row['Catégorie'] == 'Épargne':
                        self.list_widget_epargne.addItem(item)
                    elif row['Catégorie'] == 'Charges personnelles':
                        self.list_widget_charge_personelle.addItem(item)
                    elif row['Catégorie'] == 'Dépenses personnelles':
                        self.list_widget_depense_personnelle.addItem(item)
                    elif row['Catégorie'] == 'Restaurant':
                        self.list_widget_restaurant.addItem(item)
                    elif row['Catégorie'] == 'Note de frais':
                        self.list_widget_note_de_frais.addItem(item)
                    elif row['Catégorie'] == 'Course annexe':
                        self.list_widget_course_annexe.addItem(item)
                    elif row['Catégorie'] == 'Travail':
                        self.list_widget_travail.addItem(item)
                    elif row['Catégorie'] == 'Santé':
                        self.list_widget_sante.addItem(item)
                    elif row['Catégorie'] == 'Annexe':
                        self.list_widget_annexe.addItem(item)

            except Exception as e:
                # Afficher un message d'erreur
                QMessageBox.critical(self, "Erreur", str(e))

    def remove_category(self):
        # Parcourir toutes les listes
        for list_widget in [self.list_widget_charges_foyer, self.list_widget_bourse, self.list_widget_epargne,
                            self.list_widget_charge_personelle, self.list_widget_depense_personnelle,
                            self.list_widget_restaurant, self.list_widget_note_de_frais, self.list_widget_course_annexe,
                            self.list_widget_travail, self.list_widget_sante, self.list_widget_annexe]:
            # Obtenir l'item sélectionné
            item = list_widget.currentItem()

            # Si un item est sélectionné
            if item is not None:
                # Ajouter l'item à la liste générale
                self.list_widget_general.addItem(item.text())

                # Supprimer l'item de la liste actuelle
                list_widget.takeItem(list_widget.row(item))

                # Vérifier si la liste est vide
                if self.list_widget_charges_foyer.count() == 0:
                    self.list_widget_charges_foyer.hide()
                    self.label_charges_foyer.hide()
                if self.list_widget_charges_foyer.count() == 0:
                    self.list_widget_charges_foyer.hide()
                    self.label_charges_foyer.hide()
                if self.list_widget_bourse.count() == 0:
                    self.list_widget_bourse.hide()
                    self.label_bourse.hide()
                if self.list_widget_epargne.count() == 0:
                    self.list_widget_epargne.hide()
                    self.label_epargne.hide()
                if self.list_widget_charge_personelle.count() == 0:
                    self.list_widget_charge_personelle.hide()
                    self.label_charge_personelle.hide()
                if self.list_widget_depense_personnelle.count() == 0:
                    self.list_widget_depense_personnelle.hide()
                    self.label_depense_personnelle.hide()
                if self.list_widget_restaurant.count() == 0:
                    self.list_widget_restaurant.hide()
                    self.label_restaurant.hide()
                if self.list_widget_note_de_frais.count() == 0:
                    self.list_widget_note_de_frais.hide()
                    self.label_note_de_frais.hide()
                if self.list_widget_course_annexe.count() == 0:
                    self.list_widget_course_annexe.hide()
                    self.label_course_annexe.hide()
                if self.list_widget_travail.count() == 0:
                    self.list_widget_travail.hide()
                    self.label_travail.hide()
                if self.list_widget_sante.count() == 0:
                    self.list_widget_sante.hide()
                    self.label_sante.hide()
                if self.list_widget_annexe.count() == 0:
                    self.list_widget_annexe.hide()
                    self.label_annexe.hide()

                # Mettre à jour le DataFrame
                for index, row in self.data.iterrows():
                    if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                        self.data.at[index, 'Catégorie'] = 'Général'
                        break

                # Sortir de la boucle une fois que l'item a été traité
                break

    # Vous devrez également ajouter des méthodes pour chaque nouvelle catégorie, comme celle-ci :
    def classify_transaction(self, category):
        # Obtenir l'item sélectionné dans la liste générale
        item_general = self.list_widget_general.currentItem()

        # Obtenir l'item sélectionné dans les autres listes
        item_other = None
        list_widget_other = None
        for category, list_widget in self.category_lists.items():
            if list_widget.currentItem() is not None:
                item_other = list_widget.currentItem()
                list_widget_other = list_widget
                break

        # Si un item est sélectionné dans la liste générale ou dans une autre liste
        if item_general is not None or item_other is not None:
            if item_general is not None:
                # Ajouter l'item à la liste de la catégorie correspondante
                self.category_lists[category].addItem(item_general.text())

                # Supprimer l'item de la liste générale
                self.list_widget_general.takeItem(self.list_widget_general.row(item_general))

                # Mettre à jour le DataFrame
                for index, row in self.data.iterrows():
                    if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item_general.text():
                        self.data.at[index, 'Catégorie'] = category
                        break
            else:
                # Ajouter l'item à la liste de la catégorie correspondante
                self.category_lists[category].addItem(item_other.text())

                # Supprimer l'item de l'autre liste
                list_widget_other.takeItem(list_widget_other.row(item_other))

                # Mettre à jour le DataFrame
                for index, row in self.data.iterrows():
                    if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item_other.text():
                        self.data.at[index, 'Catégorie'] = category
                        break

            # Vérifier si la liste est vide
            if self.category_lists[category].count() > 0:
                self.category_lists[category].show()
                # Ici, nous supposons que vous avez aussi un dictionnaire self.category_labels qui associe chaque catégorie à son label correspondant
                self.category_labels[category].show()

# Ajoutez des méthodes similaires pour les autres catégories...


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()