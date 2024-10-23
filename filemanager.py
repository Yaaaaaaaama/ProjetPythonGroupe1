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
<<<<<<< HEAD
=======
        
    def search_keyword(self, keyword):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
                found = False
                for line in lines:
                    if keyword in line:
                        print(line.strip())
                        found = True
                if not found:
                    print(f"Le mot-clé '{keyword}' n'a pas été trouvé.")
        except FileNotFoundError:
            print(f"Le fichier {self.file_path} est introuvable.")
>>>>>>> 3130d74850cc4199f34489036f8e405b86e409c0
        except Exception as e:
            print(f"Une erreur s'est produite lors de la recherche du mot-clé : {e}")


