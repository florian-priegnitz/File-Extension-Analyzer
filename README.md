# File Extension Analyzer

Der File Extension Analyzer ist ein einfach zu verwendendes Python-Skript, das einen Ordner analysiert und die Anzahl der Dateien nach Dateiendungen aufschlüsselt. Es ist ein nützliches Tool für IT-ForensikerInnen, um schnell einen Überblick über die Dateitypen in einem bestimmten Verzeichnis zu erhalten.

## Anforderungen
- Python 3.6 oder höher

##Verwendung
- Führe das Script "file_extension_analyzer.py" aus indem Du den gewünschten Ordnerpfad als Argument übergibts:
- Das Skript analysiert den angegebenen Ordner und gibt eine Tabelle mit Dateiendungen und der Anzahl der entsprechenden Dateien aus.

## Beispiel

sample_directory/ enthält:

- image1.jpg
- image2.jpg
- document.pdf
- notes1.txt
- notes2.txt
- notes3.txt
- image3.png
- image4.png
- image5.png

Dann würde das Script wie folgt aufgerufen werden: 

```python
python file_extension_analyzer.py /path/to/sample_directory
```

Die Ausgabe würde dann ergeben:
- Dateiendung | Anzahl
- .jpg        | 2
- .png        | 3
- .pdf        | 1
- .txt        | 3

