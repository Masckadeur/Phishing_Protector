# analyse_mail_html.py

Le script ne comporte qu'une seule fonctin qui va regarder si le code html comporte des lien vers des site mailveillant. les site mailveillant sont renseigné dans le fichier de configuration **ban/domaine.txt**.

La fonction vérifie plusieurs chose:
* elle cherche tous dabord les lien.
* elle vérifie que le lien afficher sur la page redirige bien sur cette page.
* elle regarde sur le lien redirige vers un domaine interdit.