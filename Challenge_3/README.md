# Challenge #3

Hallo zusammen!

Bei dieser Aufgabe geht es darum, das Dateisystem zu nutzen.

- Programmiersprache: Python
- Hilfsmittel (CheatSheet)

## Folgende Aufgabenstellung:

Das Ziel ist, dass wir einen ein kleines ToDo Programm erstellen, welches unsere Tasks in eine Datei schreibt.
Erstellt hierzu einen Ornder und darin eine Python Datei namens _main.py_ und eine Datei namens _todo.txt_.
Wenn euer Programm gestartet wird, sollen alle bestehenden ToDos (am Anfang gibt es natürlich noch keine) aufgelistet werden. Dazu soll immer eine aufsteigende Nummer vorangestellt sein, damit jeder Task somit identifizierbar ist.
Das Programm soll dich dann fragen, ob du einen neuen Task anlegen willst, oder einen löschen willst. Neue Tasks werden hinten angefügt, eh klar :-)

- Wenn du einen hinzufügen willst, dann mache bitte einen Input mit dem gewünschten Text. Danach werden die bestehenden Tasks wieder in aufsteigender Reihenfolge angezeigt.
- Wenn du einen Task löschen willst, dann gib die Nummer an, die geöscht werden soll. Danach werden die bestehenden Tasks wieder in aufsteigender Reihenfolge angezeigt.

Beachte bitte, dass stets, nach dem Hinzufügen oder Löschen eines Tasks, die Tasks in die Datei geschrieben werden. Beim erneuten starten des Programms sollen die Tasks dann wieder eingelesen werden und entsprechend ausgegeben werden.

### Beispiel zum Lesen und Schreiben von einer Text-Datei

```python
# das "Neue Zeile" Zeichen am Ende des Strings entfernen
def removeTrailingNewLine(value):
    return value.rstrip("\n")
# das "Neue Zeile" Zeichen am Ende des Strings hinzufügen
def addTrailingNewLine(value):
    return value + ("\n")

# Datei als Liste auslesen
def readFileAndGetAsList(pathToFile):
  f = open(pathToFile, "r")
  if f.mode == 'r':
    contents = f.readlines()
    f.close()
    return list(map(removeTrailingNewLine, contents))
  else:
    return []

# Liste als Datei wieder schreiben
def writeListToFile(pathToFile, dataAsList=[]):
  f = open(pathToFile, "w+")
  listWithNewsLintes = list(map(addTrailingNewLine, dataAsList))
  f.writelines(listWithNewsLintes)
  f.close()


pathToFile = "absoluter/oder/relativer/pfad/zu/deiner/datei/tasks.txt"

# List von Datei laden
lines = readFileAndGetAsList(pathToFile)

# Wert hinzufügen
lines.append("holladrio")

# Liste neu speichern
writeListToFile(pathToFile, lines)
```

### Bitte lesen

Diese Infos bitte ansehen, weil: Das Verständnis von Grund-Typen ist essentiell. Bitte aufmerksam durchlesen **bevor** ihr die Übung macht.

- [Umgang mit Dateien in Python (lesen, schreiben, ...)](https://www.guru99.com/reading-and-writing-files-in-python.html)
- [map](https://www.geeksforgeeks.org/python-map-function/)
- [remove trailng newline in python](https://kite.com/python/answers/how-to-remove-a-trailing-newline-in-python)

## Bonus-Aufgabe:

Wem das zu leicht ist (kann ich mir nicht vorstellen), der kann anstatt Tasks zu löschen, diese in eine \_tasks*done.txt* speichern und in der Auflistung diese als erledigt ausgeben.

## Hilfsmittel:

- [CheatCheet für Basics](https://teams.microsoft.com/l/file/577FC335-F5B4-4A56-B307-D7ED57E48403?tenantId=b8192970-931b-4546-97ce-a6a611c24bd9&fileType=pdf&objectUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345%2FFreigegebene%20Dokumente%2FWeekly%20Coding%20Challenge%2FMaterialien%2Fbeginners_cheat_sheet.pdf&baseUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345&serviceName=teams&threadId=19:a6077bbb7c794716aef8ef6264849648@thread.skype&groupId=fe5a1a58-19cb-498f-88e0-617b2206af7e),
- [CheatSheet für Lists](https://teams.microsoft.com/l/file/FA626DD4-119C-4335-BC3D-6F5BE93997FE?tenantId=b8192970-931b-4546-97ce-a6a611c24bd9&fileType=pdf&objectUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345%2FFreigegebene%20Dokumente%2FWeekly%20Coding%20Challenge%2FMaterialien%2Fbeginners_python_cheat_sheet_pcc_lists.pdf&baseUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345&serviceName=teams&threadId=19:a6077bbb7c794716aef8ef6264849648@thread.skype&groupId=fe5a1a58-19cb-498f-88e0-617b2206af7e)
- Fragen [als Issue](https://github.com/joeherold/wcc_fh_wkw_python/issues) oder als [Formular](https://forms.office.com/Pages/ResponsePage.aspx?Host=Teams&lang=%7Blocale%7D&groupId=%7BgroupId%7D&tid=%7Btid%7D&teamsTheme=%7Btheme%7D&upn=%7Bupn%7D&id=cCkZuBuTRkWXzqamEcJL2Rcv0_AVGQVMpyxsXq73-hxUOUM1QVo0WTA3T1dOSEQ3NkxCN0Y1MjZBUC4u) erstellen.

**VIEL ERFOLG! Gemeinsame Auflösung nächstes Wochenende**
