from filemanager import FileManager

file_manager = FileManager('log.txt')

if __name__ == "__main__":
    print("Lecture du fichier log.txt :")
    file_manager.read_file()

    print("\nAjout d'un nouveau log :")
    file_manager.write_to_file("[2024-10-20 12:00:00] INFO: Nouveau log ajouté")

    print("\nRecherche du mot-clé 'ERROR' :")
    file_manager.search_keyword("ERROR")

    print(f"\nNombre de lignes dans le fichier : {file_manager.count_lines()}")
