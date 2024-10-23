class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            # Ouverture du fichier en mode lecture ('r') et lecture du contenu
            with open(self.file_path, 'r') as file:
                contenu = file.read()  # Lecture de tout le contenu du fichier
                print("Contenu du fichier :")
                print(contenu)  # Affichage du contenu du fichier
        except FileNotFoundError:
            # Message d'erreur si le fichier n'existe pas
            print(f"Le fichier {self.file_path} n'a pas été trouvé.")
    

    def write_to_file(self, data):
        # Ouverture du fichier en mode écriture ('w'), écrase le contenu si le fichier existe
        with open(self.file_path, 'a') as file:
            file.write(data + '\n')  # Ajoute les données avec un saut de ligne
            print("Les données ont été ajoutées à la fin du fichier.")
    

    def count_lines(self):
        try:
            # Ouverture du fichier en mode lecture
            with open(self.file_path, 'r') as file:
                nbr_lignes = file.readlines()  # Lit toutes les lignes du fichier et les stocke dans une liste lignes
                # readlines() est une methode prédéfinie lit toutes les lignes d'un fichier ouvert et les renvoyer sous forme de liste
                return len(nbr_lignes)  # Retourne le nombre d'éléments dans la liste lignes
        except FileNotFoundError:
            # Message d'erreur si le fichier n'existe pas
            print(f"Le fichier {self.file_path} n'a pas été trouvé.")
            return 0  # Retourne 0 car le fichier n'existe pas
        

    def search_keyword(self, keyword):
        try:
            # Ouverture du fichier en mode lecture
            with open(self.file_path, 'r') as file:
                liste = []  # Liste pour stocker les lignes contenant le mot-clé
                for ligne in file:
                    if keyword in ligne:  # Vérification si le mot-clé est dans la ligne
                        liste.append(ligne)  # Ajoute la ligne correspondante à la liste
                if liste:
                    # Si des lignes contenant le mot-clé ont été trouvées, les afficher
                    print(f"Lignes contenant '{keyword}':")
                    for lis in liste:
                        print(lis)  # Affichage de chaque ligne correspondante
                else:
                    # Si aucune ligne ne contient le mot-clé
                    print(f"Aucune ligne trouvée contenant '{keyword}'.")
        except FileNotFoundError:
            # Message d'erreur si le fichier n'existe pas
            print(f"Le fichier {self.file_path} n'a pas été trouvé.")



app=FileManager('log.txt')
if __name__ == "__main__":
    # Spécification du chemin de fichier
    file_path = 'log.txt'
    
    # Création de l'instance FileManager
    manager = FileManager(file_path)

    # Test de la lecture du fichier
    print("\n=== Test de la lecture du fichier ===")
    manager.read_file()
    
     # Test de l'ajout d'une nouvelle ligne
    print("\n=== Ajout d'une nouvelle ligne ===")
    manager.write_to_file("[2024-10-20 11:38:00] INFO: Nouvelle ligne ajoutée pour test.")
    
    # Lecture du fichier après l'ajout
    print("\n=== Lecture après ajout ===")
    manager.read_file()
    
    # Test du comptage des lignes
    print("\n=== Comptage des lignes ===")
    line_count = manager.count_lines()
    print(f"Nombre total de lignes : {line_count}")
    
    # Test de la recherche d'un mot-clé
    print("\n=== Recherche du mot-clé 'ERROR' ===")
    manager.search_keyword("ERROR")
