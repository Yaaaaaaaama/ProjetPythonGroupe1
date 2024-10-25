import pandas as pd

# Lire le fichier log.txt dans un DataFrame
df_logs = pd.read_csv('log.txt', sep="\n", header=None, names=["Log"])

# Afficher le contenu du fichier
print("Contenu du fichier log.txt ")
print(df_logs)

# Compter le nombre de lignes
print("\nNombre de lignes dans le fichier log.txt ")
print(len(df_logs))

# Enregistrer le DataFrame dans un fichier CSV (optionnel)
df_logs.to_csv('logs.csv', index=False)
print("\nLogs enregistrés dans 'logs.csv'")