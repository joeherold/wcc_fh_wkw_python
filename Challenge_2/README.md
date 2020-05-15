# Challenge #2

Hallo zusammen!

Nachdem wir zusammen schon erfolgreich die erste Challenge geschafft haben hat sich gezeigt, dass es noch Bedarf am Verstehen der verschiedenen Daten-Typen gibt. Was sind die verschiedenen Grund-Datentypen, was sind Datenstrukturen.

- Programmiersprache: Python
- Hilfsmittel (CheatSheet)

## Folgende Aufgabenstellung:

Macht euch mit den Grund-Datentypen und den Rechenoperationen bzw. Vergleichsoperatoren vertraut, und spielt damit rum.
Macht euch mit Lists vertraut und spielt damit etwas rum.

**Gewünschtes Ziel: Bitte versucht mit allen Daten-Typen und der Datenstruktur List alle Rechenoperationen und Vertleichs-Operatoren durchzuführen.**

Macht das immer in einem try-except Block, damit bei einer unmöglichen Konstellation das Programm nicht abbricht.
Überlegt auch, wie man durch einen kleinen Type-Cast (z.B.: `int("45")`) einen Fehler vermeiden kann.

### Beispiel

```python
# Strings multiplizieren
try:
  result = "text1" * "text2"
  print("Strings können multipliziert werden")
  print(result)
except:
  print("Strings können nicht multipliziert werden")

# Strings addieren
try:
  result = "25" + "25"
  print("Strings können addiert werden, aber etwas ist besonders... was denn?")
  print(result)

except:
  print("Strings können nicht addiert werden")

# Boolean mit Integer multiplizieren
try:
  result = True * 43
  print("Boolean kann mit Int multipliziert werden")
  print(result)
except:
  print("Boolean kann nicht mit Int multipliziert werden")

# List mit List addieren
try:
  result = ["hello", "world"] + ["oh dear"]
  print("Lists können addiert werden")
  print(result)
except:
  print("Lists können nicht addiert werden")

... usw
```

### Bitte lesen

Diese Infos bitte ansehen, weil: Das Verständnis von Grund-Typen ist essentiell. Bitte aufmerksam durchlesen **bevor** ihr die Übung macht.

- [Rechen- und Vergleichs-Operatoren](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md)
- [Strings](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/04_Day_Strings/04_string.md)
- [Infos zu Lists](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/05_Day_Lists/05_list.md)

### Datemstrukturen

Ist eine "Zusammensetzung" aus den Grund-Datentypen

```python

Boolean: True False
String: "hallo" oder 'hallo'
Integer: 1 2 3 4
Float: 1.2  3.234234
...
```

### Datentypen

```python
List
Dictionary
... und weitere, die wir noch nicht betrachten
```

### Grundrechenarten

```python
+ ... Addition
- ... Subdraktion
* ... Multiplikation
/ ... Division
% ... Modulo (Der Rest Operator)
```

### Vergleichsoperatoren

```python
< ... kleiner
> ... größer
<= ... kleiner gleich
>= ... größer gleich
== ... ist gleich
```

```python
try:
  # my code that can cause a problem comes here
except:
  # here we handle the exception
```

## Bonus-Aufgabe:

Erstelle eine Funktion **getPrimeNumbers**, die 2 Parameter übernimmt **start** und **count**. Diese Funktion soll dir ab dem **start** Wert die Anzahl aufsteigender Prim-Zahlen ausgeben, die es gibt.

- Beispiel: start = 0, count = 3
- Ergebnis: 2,3,5
- _Wichtig:_ Es müssen die Primzahlen berechnet werden, sodass ich z.B. als Start auch 1200 und Count 45 eingeben kann.

### Definition Primzahl:

Eine Primzahl ist ein natürliche Zahl, die größer als 1 ist und nur durch sich selbst und 1 teilbar ist, also nur bei einer Division durch 1 oder sich selbst als Rest 0 hat. Zur Berechung des Restes könnt ihr den Modulo `%` Operator verwenden. 5/2 = 2,5 aber 5%2 = 1 da hier nur der Rest übergeben wird. 10/2 = 5 aber 10%2 = 0.

```python
def getPrimeNumbers(start, count):
  #do some code
```

## Hilfsmittel:

- [Primzahl auf Wikipedia](https://de.wikipedia.org/wiki/Primzahl)

- [CheatCheet für Basics](https://teams.microsoft.com/l/file/577FC335-F5B4-4A56-B307-D7ED57E48403?tenantId=b8192970-931b-4546-97ce-a6a611c24bd9&fileType=pdf&objectUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345%2FFreigegebene%20Dokumente%2FWeekly%20Coding%20Challenge%2FMaterialien%2Fbeginners_cheat_sheet.pdf&baseUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345&serviceName=teams&threadId=19:a6077bbb7c794716aef8ef6264849648@thread.skype&groupId=fe5a1a58-19cb-498f-88e0-617b2206af7e),
- [CheatSheet für Lists](https://teams.microsoft.com/l/file/FA626DD4-119C-4335-BC3D-6F5BE93997FE?tenantId=b8192970-931b-4546-97ce-a6a611c24bd9&fileType=pdf&objectUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345%2FFreigegebene%20Dokumente%2FWeekly%20Coding%20Challenge%2FMaterialien%2Fbeginners_python_cheat_sheet_pcc_lists.pdf&baseUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345&serviceName=teams&threadId=19:a6077bbb7c794716aef8ef6264849648@thread.skype&groupId=fe5a1a58-19cb-498f-88e0-617b2206af7e)
- Fragen [als Issue](https://github.com/joeherold/wcc_fh_wkw_python/issues) oder als [Formular](https://forms.office.com/Pages/ResponsePage.aspx?Host=Teams&lang=%7Blocale%7D&groupId=%7BgroupId%7D&tid=%7Btid%7D&teamsTheme=%7Btheme%7D&upn=%7Bupn%7D&id=cCkZuBuTRkWXzqamEcJL2Rcv0_AVGQVMpyxsXq73-hxUOUM1QVo0WTA3T1dOSEQ3NkxCN0Y1MjZBUC4u) erstellen.

**VIEL ERFOLG! Gemeinsame Auflösung nächstes Wochenende**
