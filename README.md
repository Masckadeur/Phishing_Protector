# Phishing_Protector

Ce projet développer en python à pour vocation à utiliser des outils pour aider à repérer des mails de phishing (Hameçonnage)

Le projet est composer de plusieurs programmes tous indépendants.

\textbf{collect_mail.py} comme son nom l'indique, ce programme va se connecter et récupérer des mails d'un compte.
Pour le moment seul les comptes Outlook fonctionne.
Plusieurs argument peuvent être demandé :
    - \textbf{host} -- par defaut : {outlook.office365.com}; pour un mail gmail : imap.gmail.com (Assurez vous que l'option less secure Apps est activé. Sinon Gmail refusera la connexion)
    - (falcutatif) fichier \textbf{credentials} à créer, comportant 2 lignes:
        - première ligne avec l'email
        - deuxième lignes avec le mot de passe du compte 

Vous pouvez, si vous le voulez, ne pas utiliser le programme de collect de mail. pour cela vous devrez télécharger votre mail à tester au format \textbf{HTML}. Par la suite vous devrez copier le contenu du mail dans un fichier mail.html.

\textbf{analyse_mail_html} est un programme qui utilise un mail au format \textbf{HTML} pour être analysé. Pour fonctionner il faut copier le contenu d'un mail dans le fichier \textbf{mail.txt}.