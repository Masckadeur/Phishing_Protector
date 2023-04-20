# Pré-requis
* Python3.9

## BlackList
dans le dossier *ban*, des fichiers *.txt sont présent, il suffit d'ajouter des lignes avec les informations correspondantes (adresse email, nom de domaine, extension de fichier) afin de les ajouter comme données qui permettent de dire au script ce qu'il peut être ban.

## Tests
Utilisation de Pytest

Des mails ont été télécharger au format html afin d'être analysé,  ( vous pouvez les retrouvrez sur l'adresse mail fourni)
C'est test font uniquement vérifié si des lien de redirection sont présent. Aussi bien des lien vers des sites mailveillants que des redirections sur un site qui n'étais a l'origine pas celui affiché.

```bash
pytest
```
