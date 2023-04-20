import os
from collections import defaultdict

# Pfad zum gewünschten Ordner
ordner = '/path/to/your/directory'

# Wörterbuch für die Dateiendungen und deren Anzahl
dateiendungen = defaultdict(int)

# Ordnerinhalt durchgehen
for dateiname in os.listdir(ordner):
    # Dateipfad erstellen
    dateipfad = os.path.join(ordner, dateiname)
    
    # Nur Dateien berücksichtigen und versteckte Dateien ignorieren
    if os.path.isfile(dateipfad) and not dateiname.startswith('.'):
        # Dateiendung extrahieren
        _, dateiendung = os.path.splitext(dateiname)
        
        # Dateiendung zählen
        dateiendungen[dateiendung] += 1

# Tabelle ausgeben
print("Dateiendung | Anzahl")
print("---------------------")
for dateiendung, anzahl in dateiendungen.items():
    print(f"{dateiendung:11} | {anzahl}")
