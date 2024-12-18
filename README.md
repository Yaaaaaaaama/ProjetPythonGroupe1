# ProjetPythonGroupe1

## Description
Ce projet fournit une classe `FileManager` pour gérer un fichier de logs, permettant de lire le contenu,
 d'ajouter des lignes, et de rechercher des mots-clés.
**FileManager** est un petit projet Python qui a pour but de simplifier la gestion de fichiers texte (ici,log.txt). Le script inclut des fonctions pour lire un fichier, ajouter du contenu, compter les lignes, et rechercher des mots-clés dans un fichier.

# Fonctionnalités
- **Lire le contenu (read_file)** : Affiche tout le contenu du fichier.
- **Écrire dans le fichier (write_to_file)** : Ajoute une nouvelle ligne de texte à la fin du fichier.
- **Compter les lignes (count_lines)** : Retourne le nombre total de lignes dans le fichier.
- **Rechercher un mot-clé (search_keyword)** : Recherche et affiche les lignes contenant un mot-clé spécifique.

# Main.py
**Fonctionnement de main.py :**
Ce script utilise la classe `FileManager` pour manipuler un fichier `log.txt`.
Il permet de :
  - Lire et afficher le contenu de `log.txt`.
  - Ajouter une nouvelle entrée dans le fichier.
  - Rechercher un mot-clé, par exemple `ERROR`.
  - Afficher le nombre de lignes dans le fichier.

# Utilité de requirements.txt
Le fichier requirements.txt contient toutes les dépendances nécessaires pour exécuter ce projet. Cela permet de s'assurer que tous les utilisateurs peuvent installer les mêmes versions de packages, garantissant ainsi la compatibilité entre différentes installations.

Pour installer les dépendances du projet, exécutez :

- **pip install -r requirements.txt**

# Exécution et  Test
Le fichier principal pour tester `FileManager` est `main.py`. Pour exécuter le script, utilisez la commande :
- **python main.py**
