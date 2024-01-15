from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, \
    QLabel, QMessageBox, QFileDialog, QMenuBar, QMenu, QAbstractItemView
from PyQt5.QtCore import Qt
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
        self.list_widget_bourse = QListWidget()
        self.list_widget_epargne = QListWidget()
        self.list_widget_charge_personelle = QListWidget()
        self.list_widget_depense_personnelle = QListWidget()
        self.list_widget_restaurant = QListWidget()
        self.list_widget_note_de_frais = QListWidget()
        self.list_widget_course_annexe = QListWidget()
        self.list_widget_travail = QListWidget()
        self.list_widget_sante = QListWidget()
        self.list_widget_annexe = QListWidget()

        # Configurer le mode de sélection des listes
        self.list_widget_general.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_charges_foyer.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_bourse.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_epargne.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_charge_personelle.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_depense_personnelle.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_restaurant.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_note_de_frais.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_course_annexe.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_travail.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_sante.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.list_widget_annexe.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Créer les labels pour chaque liste
        self.label_general = QLabel("Général")
        self.label_charges_foyer = QLabel("Charges du foyer")
        self.label_bourse = QLabel("Bourse")
        self.label_epargne = QLabel("Épargne")
        self.label_charge_personelle = QLabel("Charges personnelles")
        self.label_depense_personnelle = QLabel("Dépenses personnelles")
        self.label_restaurant = QLabel("Restaurant")
        self.label_note_de_frais = QLabel("Note de frais")
        self.label_course_annexe = QLabel("Course annexe")
        self.label_travail = QLabel("Travail")
        self.label_sante = QLabel("Santé")
        self.label_annexe = QLabel("Annexe")

        # Créer les boutons
        self.button_remove_category = QPushButton("Supprimer la catégorie")
        self.button_classify_as_charges_foyer = QPushButton("Classer comme Charges du foyer")
        self.button_classify_as_bourse = QPushButton("Classer comme Bourse")
        self.button_classify_as_epargne = QPushButton("Classer comme Épargne")
        self.button_classify_as_charge_personelle = QPushButton("Classer comme Charges personnelles")
        self.button_classify_as_depense_personnelle = QPushButton("Classer comme Dépenses personnelles")
        self.button_classify_as_restaurant = QPushButton("Classer comme Restaurant")
        self.button_classify_as_note_de_frais = QPushButton("Classer comme Note de frais")
        self.button_classify_as_course_annexe = QPushButton("Classer comme Course annexe")
        self.button_classify_as_travail = QPushButton("Classer comme Travail")
        self.button_classify_as_sante = QPushButton("Classer comme Santé")
        self.button_classify_as_annexe = QPushButton("Classer comme Annexe")

        # Connecter les boutons à leurs fonctions correspondantes
        self.button_remove_category.clicked.connect(self.remove_category)
        self.button_classify_as_charges_foyer.clicked.connect(self.classify_as_charges_foyer)
        self.button_classify_as_bourse.clicked.connect(self.classify_as_bourse)
        self.button_classify_as_epargne.clicked.connect(self.classify_as_epargne)
        self.button_classify_as_charge_personelle.clicked.connect(self.classify_as_charge_personelle)
        self.button_classify_as_depense_personnelle.clicked.connect(self.classify_as_depense_personnelle)
        self.button_classify_as_restaurant.clicked.connect(self.classify_as_restaurant)
        self.button_classify_as_note_de_frais.clicked.connect(self.classify_as_note_de_frais)
        self.button_classify_as_course_annexe.clicked.connect(self.classify_as_course_annexe)
        self.button_classify_as_travail.clicked.connect(self.classify_as_travail)
        self.button_classify_as_sante.clicked.connect(self.classify_as_sante)
        self.button_classify_as_annexe.clicked.connect(self.classify_as_annexe)

        # Créer le layout pour les boutons
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.button_remove_category)
        self.button_layout.addWidget(self.button_classify_as_charges_foyer)
        self.button_layout.addWidget(self.button_classify_as_bourse)
        self.button_layout.addWidget(self.button_classify_as_epargne)
        self.button_layout.addWidget(self.button_classify_as_charge_personelle)
        self.button_layout.addWidget(self.button_classify_as_depense_personnelle)
        self.button_layout.addWidget(self.button_classify_as_restaurant)
        self.button_layout.addWidget(self.button_classify_as_note_de_frais)
        self.button_layout.addWidget(self.button_classify_as_course_annexe)
        self.button_layout.addWidget(self.button_classify_as_travail)
        self.button_layout.addWidget(self.button_classify_as_sante)
        self.button_layout.addWidget(self.button_classify_as_annexe)

        # Créer le layout pour chaque liste et son label
        self.layout_general = QVBoxLayout()
        self.layout_general.addWidget(self.label_general)
        self.layout_general.addWidget(self.list_widget_general)
        self.layout_charges_foyer = QVBoxLayout()
        self.layout_charges_foyer.addWidget(self.label_charges_foyer)
        self.layout_charges_foyer.addWidget(self.list_widget_charges_foyer)
        self.layout_bourse = QVBoxLayout()
        self.layout_bourse.addWidget(self.label_bourse)
        self.layout_bourse.addWidget(self.list_widget_bourse)
        self.layout_epargne = QVBoxLayout()
        self.layout_epargne.addWidget(self.label_epargne)
        self.layout_epargne.addWidget(self.list_widget_epargne)
        self.layout_charge_personelle = QVBoxLayout()
        self.layout_charge_personelle.addWidget(self.label_charge_personelle)
        self.layout_charge_personelle.addWidget(self.list_widget_charge_personelle)
        self.layout_depense_personnelle = QVBoxLayout()
        self.layout_depense_personnelle.addWidget(self.label_depense_personnelle)
        self.layout_depense_personnelle.addWidget(self.list_widget_depense_personnelle)
        self.layout_restaurant = QVBoxLayout()
        self.layout_restaurant.addWidget(self.label_restaurant)
        self.layout_restaurant.addWidget(self.list_widget_restaurant)
        self.layout_note_de_frais = QVBoxLayout()
        self.layout_note_de_frais.addWidget(self.label_note_de_frais)
        self.layout_note_de_frais.addWidget(self.list_widget_note_de_frais)
        self.layout_course_annexe = QVBoxLayout()
        self.layout_course_annexe.addWidget(self.label_course_annexe)
        self.layout_course_annexe.addWidget(self.list_widget_course_annexe)
        self.layout_travail = QVBoxLayout()
        self.layout_travail.addWidget(self.label_travail)
        self.layout_travail.addWidget(self.list_widget_travail)
        self.layout_sante = QVBoxLayout()
        self.layout_sante.addWidget(self.label_sante)
        self.layout_sante.addWidget(self.list_widget_sante)
        self.layout_annexe = QVBoxLayout()
        self.layout_annexe.addWidget(self.label_annexe)
        self.layout_annexe.addWidget(self.list_widget_annexe)

        # Créer le layout principal
        self.layout = QHBoxLayout()

        # Ajouter les layouts à la mise en page principale
        self.layout.addLayout(self.layout_general)
        self.layout.addLayout(self.layout_charges_foyer)
        self.layout.addLayout(self.layout_bourse)
        self.layout.addLayout(self.layout_epargne)
        self.layout.addLayout(self.layout_charge_personelle)
        self.layout.addLayout(self.layout_depense_personnelle)
        self.layout.addLayout(self.layout_restaurant)
        self.layout.addLayout(self.layout_note_de_frais)
        self.layout.addLayout(self.layout_course_annexe)
        self.layout.addLayout(self.layout_travail)
        self.layout.addLayout(self.layout_sante)
        self.layout.addLayout(self.layout_annexe)
        self.layout.addLayout(self.button_layout)

        # Cacher toutes les colonnes sauf "Général"
        self.list_widget_charges_foyer.hide()
        self.list_widget_bourse.hide()
        self.list_widget_epargne.hide()
        self.list_widget_charge_personelle.hide()
        self.list_widget_depense_personnelle.hide()
        self.list_widget_restaurant.hide()
        self.list_widget_note_de_frais.hide()
        self.list_widget_course_annexe.hide()
        self.list_widget_travail.hide()
        self.list_widget_sante.hide()
        self.list_widget_annexe.hide()

        self.label_charges_foyer.hide()
        self.label_bourse.hide()
        self.label_epargne.hide()
        self.label_charge_personelle.hide()
        self.label_depense_personnelle.hide()
        self.label_restaurant.hide()
        self.label_note_de_frais.hide()
        self.label_course_annexe.hide()
        self.label_travail.hide()
        self.label_sante.hide()
        self.label_annexe.hide()

        # Créer un widget central pour la fenêtre
        self.central_widget = QWidget()

        # Appliquer le layout au widget central
        self.central_widget.setLayout(self.layout)

        # Définir le widget central de la fenêtre
        self.setCentralWidget(self.central_widget)

        # Lire les données
        self.data = pd.DataFrame()

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
    def classify_as_charges_foyer(self):
        # Obtenir l'item sélectionné dans la liste générale
        item_general = self.list_widget_general.currentItem()

        # Obtenir l'item sélectionné dans les autres listes
        item_other = None
        for list_widget in [self.list_widget_bourse, self.list_widget_epargne, self.list_widget_charge_personelle,
                            self.list_widget_depense_personnelle, self.list_widget_restaurant,
                            self.list_widget_note_de_frais, self.list_widget_course_annexe, self.list_widget_travail,
                            self.list_widget_sante, self.list_widget_annexe]:
            if list_widget.currentItem() is not None:
                item_other = list_widget.currentItem()
                list_widget_other = list_widget
                break

        # Si un item est sélectionné dans la liste générale ou dans une autre liste
        if item_general is not None or item_other is not None:
            if item_general is not None:
                # Ajouter l'item à la liste des charges du foyer
                self.list_widget_charges_foyer.addItem(item_general.text())

                # Supprimer l'item de la liste générale
                self.list_widget_general.takeItem(self.list_widget_general.row(item_general))

                # Mettre à jour le DataFrame
                for index, row in self.data.iterrows():
                    if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item_general.text():
                        self.data.at[index, 'Catégorie'] = 'Charges du foyer'
                        break
            else:
                # Ajouter l'item à la liste des charges du foyer
                self.list_widget_charges_foyer.addItem(item_other.text())

                # Supprimer l'item de l'autre liste
                list_widget_other.takeItem(list_widget_other.row(item_other))

                # Mettre à jour le DataFrame
                for index, row in self.data.iterrows():
                    if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item_other.text():
                        self.data.at[index, 'Catégorie'] = 'Charges du foyer'
                        break

            # Vérifier si la liste est vide
            if self.list_widget_charges_foyer.count() > 0:
                self.list_widget_charges_foyer.show()
                self.label_charges_foyer.show()

    def classify_as_bourse(self):
        # Obtenir l'item sélectionné dans la liste générale
        item_general = self.list_widget_general.currentItem()

        # Obtenir l'item sélectionné dans les autres listes
        item_other = None
        for list_widget in [self.list_widget_bourse, self.list_widget_epargne, self.list_widget_charge_personelle,
                            self.list_widget_depense_personnelle, self.list_widget_restaurant,
                            self.list_widget_note_de_frais, self.list_widget_course_annexe, self.list_widget_travail,
                            self.list_widget_sante, self.list_widget_annexe]:
            if list_widget.currentItem() is not None:
                item_other = list_widget.currentItem()
                list_widget_other = list_widget
                break

        # Si un item est sélectionné dans la liste générale ou dans une autre liste
        if item_general is not None or item_other is not None:
            if item_general is not None:
                # Ajouter l'item à la liste des Bourses
                self.list_widget_bourse.addItem(item_general.text())

                # Supprimer l'item de la liste générale
                self.list_widget_general.takeItem(self.list_widget_general.row(item_general))

                # Mettre à jour le DataFrame
                for index, row in self.data.iterrows():
                    if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item_general.text():
                        self.data.at[index, 'Catégorie'] = 'Bourse'
                        break
            else:
                # Ajouter l'item à la liste des Bourses
                self.list_widget_bourse.addItem(item_other.text())

                # Supprimer l'item de l'autre liste
                list_widget_other.takeItem(list_widget_other.row(item_other))

                # Mettre à jour le DataFrame
                for index, row in self.data.iterrows():
                    if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item_other.text():
                        self.data.at[index, 'Catégorie'] = 'Bourse'
                        break

            # Vérifier si la liste est vide
            if self.list_widget_bourse.count() > 0:
                self.list_widget_bourse.show()
                self.label_bourse.show()

    def classify_as_epargne(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_epargne.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Epargne'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_epargne.count() > 0:
                self.list_widget_epargne.show()
                self.label_epargne.show()

    def classify_as_charge_personelle(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_charge_personelle.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Charge_Personnelle'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_charge_personelle.count() > 0:
                self.list_widget_charge_personelle.show()
                self.label_charge_personelle.show()

    def classify_as_depense_personnelle(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_depense_personnelle.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Depense_Personnelle'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_depense_personnelle.count() > 0:
                self.list_widget_depense_personnelle.show()
                self.label_depense_personnelle.show()

    def classify_as_restaurant(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_restaurant.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Restaurant'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_restaurant.count() > 0:
                self.list_widget_restaurant.show()
                self.label_restaurant.show()

    def classify_as_note_de_frais(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_note_de_frais.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Note de frais'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_note_de_frais.count() > 0:
                self.list_widget_note_de_frais.show()
                self.label_note_de_frais.show()

    def classify_as_course_annexe(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_course_annexe.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Course_Annexe'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_course_annexe.count() > 0:
                self.list_widget_course_annexe.show()
                self.label_course_annexe.show()

    def classify_as_travail(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_travail.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Travail'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_travail.count() > 0:
                self.list_widget_travail.show()
                self.label_travail.show()

    def classify_as_sante(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_sante.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Santé'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_sante.count() > 0:
                self.list_widget_sante.show()
                self.label_sante.show()

    def classify_as_annexe(self):
        # Obtenir l'item sélectionné
        item = self.list_widget_general.currentItem()

        # Si un item est sélectionné
        if item is not None:
            # Ajouter l'item à la liste des charges du foyer
            self.list_widget_annexe.addItem(item.text())

            # Supprimer l'item de la liste générale
            self.list_widget_general.takeItem(self.list_widget_general.row(item))

            # Mettre à jour le DataFrame
            for index, row in self.data.iterrows():
                if f"{row['Date']} ; {row['Montant']} ; {row['Nom']}" == item.text():
                    self.data.at[index, 'Catégorie'] = 'Annexe'
                    break

            # Vérifier si la liste est vide
            if self.list_widget_annexe.count() > 0:
                self.list_widget_annexe.show()
                self.label_annexe.show()


# Ajoutez des méthodes similaires pour les autres catégories...


# Créer une instance de l'application
app = QApplication(sys.argv)

# Créer une instance de la fenêtre principale
window = MainWindow()

# Afficher la fenêtre
window.show()

# Exécuter l'application
sys.exit(app.exec_())
