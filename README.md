# File-Extension-Analyzer

Der File Extension Analyzer ist ein einfach zu verwendendes Python-Skript, das einen Ordner analysiert und die Anzahl der Dateien nach Dateiendungen aufschlüsselt. Es ist ein nützliches Tool für IT-Forensik, um schnell einen Überblick über die Dateitypen in einem bestimmten Verzeichnis zu erhalten.

Anforderungen:
- Python 3.6 oder höher

Verwendung:
- Führe das Skript file_extension_analyzer.py aus, indem du den gewünschten Ordnerpfad als Argument übergibst:

python file_extension_analyzer.py /path/to/your/directory

Das Skript analysiert den angegebenen Ordner und gibt eine Tabelle mit Dateiendungen und der Anzahl der entsprechenden Dateien aus.
Beispiel

Ein Ordner hat folgenden Inhalt:
sample_directory/
. |-- image1.jpg
. |-- image2.png
. |-- document.pdf
. |-- notes.txt

Führe das Skript nun für diesen Ordner aus:

python file_extension_analyzer.py /path/to/sample_directory

Die Ausgabe würde dann wie folgt aussehen:

.Dateiendung | Anzahl
---------------------
.jpg        | 1
.png        | 1
.pdf        | 1
.txt        | 1


Ziel ist es, sich leicht Übersicht über große Ordner zu verschaffen. In zukünftigen Versionen werde ich weitere Features verbauen.
