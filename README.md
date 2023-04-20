# Phishing_Protector

Ce projet développer en python à pour vocation à utiliser des outils pour aider à repérer des mails de phishing (Hameconnage)

Le projet est composer de plusieurs programmes tous indépendants.

\textbf{collect_mail.py} comme son nom l'indique, ce programme va se connecter et récupérer des mails d'un compte.
Pour le moment seul les comptes Outlook fonctionne.
Plusieurs argument peuvent être demandé :
    - \textbf{host} -- par defaut : {outlook.office365.com}
    - (falcutatif) fichier \textbf{credentials} à créer, comportant 2 lignes:
        - première ligne avec l'email
        - deuxième lignes avec le mot de passe du compte 
    