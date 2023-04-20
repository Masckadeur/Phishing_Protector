# collect_mail.py

Ce script elle le coeur du projet.
Il à pour mission de récupéré les mails, et de lancer les analyses.

## Première étape
Les premier pas du script sont la pour permettre de ce connecter au serveur contenant tous les mails.

pour cela vous aurez besoin de l'host (outlook.office365.fr; imap.google.fr; rtc..), l'identifiant (email), du mot de passe.

après s'être connecté, on renseigne le nombre de mail que l'on veux récupérer (N dernier mails reçu).

après nous avons la partie d'analyse:
* nous commençons par chercher le sujet du mail, l'émetteur.
* nous cherchons par la suite le mail au format html, nous récupérons le contenue, et nous l'écrivons dans un dossier qui porte le nom du sujet du mail. Ce fichier sera utilisé par la suite pour être analysé afin de déterminer si des liens frauduleux sont présent
* Nous affichons par la suite le contenue du mail dans un terminal.
* la dernière étape est de regarder si une pièce jointe est présente, si une pièce jointe est bien présente, nous regardons si le fichier joint est autorisé. Si non, nous affichons un message au format :
```bash
name_of_file    !!!! fichier interdit
```

# Séparation des mails
Les mails sont séparé par des lignes
```bash
=================================================
```