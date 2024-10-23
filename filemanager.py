class FileManager:
    # Stocker le chemin
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        # Lire / afficher le contenu
        with open(self.file_path, 'r') as file:
            content = file.read()
            print("Contenu du fichier :")
            print(content)

    def write_to_file(self, data):
        try:
            with open(self.file_path, 'a') as file:
                file.write(data + '\n') 
                print("Les données ont été ajoutées à la fin du fichier.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'écriture dans le fichier : {e}")
            
    def count_lines(self):
        try:
            with open(self.file_path, 'r') as file:
                nbr_lignes = file.readlines()  
                return len(nbr_lignes)  
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} n'a pas été trouvé.")
            return 0
        except Exception as e:
            print(f"Une erreur s'est produite lors de la recherche du mot-clé : {e}")


