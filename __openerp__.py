# -*- coding: utf-8 -*-

{
  "name" : "InfoSaône - Module OpenERP Tutoriel 09",
  "version" : "0.1",
  "author" : "InfoSaône",
  "category" : "InfoSaône/Tutoriel",


  'description': """
InfoSaône / Module OpenERP Tutoriel 09
===================================================

Le but de ce module est de montrer comment personnaliser la mise en page des formulaires avec des colonnes, des onglets et des tableaux.

Ce module dépend du module `infosaone_tutoriel08` car il crée de nouvelles vues en utilisant le modèle (objet) de ce tutoriel.

Ce module crée le sous-menu `Tutoriel 09` pour pouvoir accèder aux nouvelles vues.

""",

  'maintainer': 'InfoSaône',
  'website': 'http://www.infosaone.com',
  "depends" : ["openerp_tutoriel_08"],              # Liste des dépendances (autres modules nececessaire au fonctionnement de celui-ci)
  "init_xml" : [],                                  # Liste des fichiers XML à installer uniquement lors de l'installation du module
  "demo_xml" : [],                                  # Liste des fichiers XML à installer pour charger les données de démonstration

  "update_xml" : ["infosaone_tutoriel09_view.xml"], # Liste des fichiers XML à installer lors d'une mise à jour du module (ou lord de l'installation)

  "installable": True,  # Si False, ce module sera visible mais non installable (intéret ?)
  "active": False       # Si True, ce module sera installé automatiquement dés la création de la base de données d'OpenERP
}

