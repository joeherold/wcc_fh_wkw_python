# Challenge #4 - Magic Triangle

Hallo zusammen!

Bei dieser Aufgabe geht es darum zu versuchen, eine reale Problemstellung digital abzubilden.

- Programmiersprache: Python
- Hilfsmittel (CheatSheet)

## Folgende Aufgabenstellung:

Das Ziel ist von einem Dreieck die/den

1. Umfang
2. Fläche
3. Schwerpunkt

zu berechnen.

**Hierzu gehe bitte wie folgt vor**

Dein Programm soll via Eingabe 3 Punkte Abfragen, die du in der Form 2/5 oder 2|5 oder 2,5 eingeben kannst, die folglich eine X und eine Y Koordinaten angebe ( 2/5 ... x=2, y=5).

Nachdem 3 mal ein x/y Punkt abgefragt wurde, soll dein Programm eine Ausgabe machnen, dass den Umfang, die Fläche und den Schwerpunkt als x/y Koordinate angibt.

### Tipp 0

Probiere es erst mal mit einem Dreieck, dass "flach" am Boden liegt und gehe dann erst zu einer allgemeinen Lage im Raum.

### Tipp 1

Verwende als Datenstruktur entweder ein Dictionary in der Form:

```python
pointOne = {x: 2, y:8}
```

oder aber Tupeln in der Form

```python
pointTwo = (2,8)
```

_Weil es beim zum Nachvollziehen im Code einfacher ist mit X und Y zu Arbeiten, empfehle ich die Dictionary-Variante, auch weil diese Werte dann direkt über ihre Koodinaten X&Y editiert werden können._

### Tipp 2

Erstelle dir für die einzelnen Teilaufgaben Funktionen, die dir Beispielsweise die Länge von 2 Punkten ausgeben, oder aber den Mittelpunkt einer Linie von 2 Punkten als x/y Koordinate ausgibt

```python
def getAbstand(pointOne, pointTwo):
  # Dein Code hier...

def getNormalvekter(point):
  # Dein Code hier...

def getMittelpunkt(pointOne, pointTwo):
  # Dein Code hier...

def getUmfang(pointOne, pointTwo):
  # Dein Code hier...
  # Nutze hier auch vorhergehende Funktionen, wenn es Sinn macht

def getSchnittpunkt(pointOneLineOne, pointTwoLineTwo, pointOneLineTwo, pointTwoLineTwo):
  # Dein Code hier...
  # Nutze hier auch vorhergehende Funktionen, wenn es Sinn macht

def getFläche(pointOne, pointTwo):
  # Dein Code hier...
  # Nutze hier auch vorhergehende Funktionen, wenn es Sinn macht

def getSchwerpunkt(pointOne, pointTwo):
  # Dein Code hier...
  # Nutze hier auch vorhergehende Funktionen, wenn es Sinn macht

# und alle weiteren Funktionen, die du benötigst

```

### Info

Wie berechnen ich von einem Vektor in der Ebene einen um 90° verdrehten Vekter, einen sogenannten Normalvektor, der normal zum gegebenen Vektor steht.
Bei 2 Achsen (x/y) wird einfach von einem der Vektoren x und y vertauscht und bei einem das Vorzeichen geändert, automatisch ist dann der Vektor um 90° Verdreht.

Kontrolle:
vektor1: (1/1) zeigt nach rechts oben, verdrehen wir zb. y, so wird daraus (1/-1) und er zeigt nach rechts unten.

### Bitte ansehen

Bitte aufmerksam ansehen **bevor** ihr die Übung macht.

- [Wiederholung Vektoren, falls du es vergessen hast](https://www.youtube.com/watch?v=dzxmbcL4fE8)
- [Umnfang und Fläche ermitteln](https://www.youtube.com/watch?v=M-Cx36dVWw0)
- [Schwerpunkt grafisch ermitteln](https://www.youtube.com/watch?v=g4KdVurVrvo)

## Bonus-Aufgabe:

Den Schwerpunkt zu berechnen, ist mit Vektoren ziemlich trivial, daher folgende Bonunsaufgabe:
Versuche deinen Algorythmus so anzupassen, dass du den Schwerpunkt so ermittelst, wie man es auch graphisch lösen würde.

## Bonus-Aufgabe EXTREME:

Wenn du mit dem vorhergehenden überfordert bist, dann ändere deinen Code so ab, dass es auch im 3d Raum geht, also mit X/Y/Z Koordinaten.

## Hilfsmittel:

- [CheatCheet für Basics](https://teams.microsoft.com/l/file/577FC335-F5B4-4A56-B307-D7ED57E48403?tenantId=b8192970-931b-4546-97ce-a6a611c24bd9&fileType=pdf&objectUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345%2FFreigegebene%20Dokumente%2FWeekly%20Coding%20Challenge%2FMaterialien%2Fbeginners_cheat_sheet.pdf&baseUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345&serviceName=teams&threadId=19:a6077bbb7c794716aef8ef6264849648@thread.skype&groupId=fe5a1a58-19cb-498f-88e0-617b2206af7e),
- Fragen [als Issue](https://github.com/joeherold/wcc_fh_wkw_python/issues) oder als [Formular](https://forms.office.com/Pages/ResponsePage.aspx?Host=Teams&lang=%7Blocale%7D&groupId=%7BgroupId%7D&tid=%7Btid%7D&teamsTheme=%7Btheme%7D&upn=%7Bupn%7D&id=cCkZuBuTRkWXzqamEcJL2Rcv0_AVGQVMpyxsXq73-hxUOUM1QVo0WTA3T1dOSEQ3NkxCN0Y1MjZBUC4u) erstellen.

**VIEL ERFOLG! Gemeinsame Auflösung nächstes Wochenende**
