# Evaluation
Ce projet a été développé pour un exercice python à EPITA.

## Déroulement du test

Nous vous conseillons d'utilisé un fichier credentials avec les informations de conexion. Autre information importante est que l'hote des mails à été tester sur outlook.office365.fr car il permette plsu de liberté, et les connexion avec la librairy python imaplib fonctionne.

Vous pouvez utiliser un compte gmail si vous le souhaitez. pour cela changer l'hoste par : imap.gmail.com (Assurez vous que l'option **less secure Apps** est activé. Sinon Gmail refusera la connexion)

Pour tester le projet il faut tous d'abord lancer la commande :
```bash
python3 script/collectmail.py
```

Cette commande lance un mini programme qui va aller récupérer des mails pour les analyser.

Le programme va nous demander des informations, dans le cadre du projet EPITA, il suffit d'utilisé celle par défaut.

* Tapez sur la touche entrer 2 fois de suite.

Par la suite un nombre d'email à récupérer est demandé, entrez le nombre **7**.

Le programme affiche ensuite les 7 mails au format :

```bash
----------------------------------------------------------------------------------------------------
Subject: test ...
From: ...

Bonjour,

.......

Bien Cordialement,

Moi-même
```

