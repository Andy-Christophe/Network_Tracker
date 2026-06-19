🌐 Network Tracker

Petit outil permettant de détecter, suivre et gérer les appareils présents sur votre réseau local.

🚀 Fonctionnalités
🔍 Scan périodique du réseau local avec conservation des appareils détectés.
🗄️ Stockage des informations dans une base SQLite.
🌐 API REST pour consulter les appareils enregistrés.
⚡ Exécution de scans Nmap à la demande.
🖥️ Interface web simple pour visualiser les appareils et lancer des actions.
🔒 Base prévue pour de futures fonctionnalités de gestion et de blocage des équipements.
📂 Structure du projet
.
├── api.py           # API Flask (port 5000)
├── main.py          # Scanner réseau périodique
├── database.py      # Gestion de la base SQLite
└── frontend/
    ├── index.html   # Interface web
    ├── script.js    # Logique frontend
    └── style.css    # Styles
Composants
Fichier	Description
api.py	Fournit une API Flask permettant de récupérer la liste des appareils et d'exécuter des scans Nmap.
main.py	Lance des scans réseau réguliers via arp-scan et synchronise les résultats avec la base de données.
database.py	Gère le stockage et la mise à jour des appareils détectés dans SQLite.
frontend/	Tableau de bord web pour visualiser et administrer le réseau.
⚙️ Prérequis
Python 3
arp-scan (nécessite généralement les privilèges administrateur)
nmap
📦 Installation (Debian / Ubuntu)
sudo apt update
sudo apt install python3 python3-pip arp-scan nmap
▶️ Lancement
1. Démarrer l'API
python3 api.py

L'API sera accessible sur :

http://localhost:5000
2. Démarrer le scanner réseau
python3 main.py
3. Lancer le tableau de bord web
cd frontend
python3 -m http.server 8080

Puis ouvrir :

http://localhost:8080
🛠️ Outils utilisés
Flask — API REST
SQLite — Base de données légère
arp-scan — Découverte des appareils sur le réseau
Nmap — Analyse réseau avancée
HTML / CSS / JavaScript — Interface utilisateur
🔮 Évolutions prévues
Blocage d'appareils depuis l'interface.
Historique des connexions.
Notifications lors de l'apparition d'un nouvel appareil.
Authentification et gestion des utilisateurs.
Déploiement via Docker.
📌 Notes

arp-scan nécessite souvent des privilèges élevés pour fonctionner correctement. Selon votre configuration, il peut être nécessaire d'exécuter le scanner avec sudo.

Un script de démarrage automatisé sera ajouté dans les prochains commits afin de simplifier le lancement de l'ensemble des services.
