import pandas as pd
import re

with open('log.txt', 'r') as file:
    logs = file.readlines()

data = []

log_pattern = re.compile(r'\[(.*?)\]\s+(\w+):\s+(.*)')

for log in logs:
    match = log_pattern.match(log)
    if match:
        data.append({'Date': match.group(1), 'Niveau': match.group(2), 'Message': match.group(3)})

df_logs = pd.DataFrame(data)

erreurs = df_logs[df_logs['Niveau'] == 'ERROR']
avertissements = df_logs[df_logs['Niveau'] == 'WARNING']
infos = df_logs[df_logs['Niveau'] == 'INFO']

print("Logs d'erreurs :")
print(erreurs)

print("\nLogs d'avertissements :")
print(avertissements)

print("\nLogs d'information :")
print(infos)
