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


