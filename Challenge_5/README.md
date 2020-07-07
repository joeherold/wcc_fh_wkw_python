# Challenge #5 - We request data from an open API

Hallo zusammen!

Bei dieser Aufgabe geht es darum Daten von einer offenen Sample-Data API zu konsumieren und als CSV Datei abzuspeichern.

- Programmiersprache: Python
- Hilfsmittel (CheatSheet)

## Folgende Aufgabenstellung:

Das Ziel ist:

1. Einen HTTP Request zu https://jsonplaceholder.typicode.com/ zu machen
2. Den JSON Response verarbeiten
3. Die Daten in ein CSV konvertieren und abspeichern

**Hierzu gehe bitte wie folgt vor**

Wir konsumieren Daten von jsonplaceholder, und zwar die Posts von Users über folgende URL: **https://jsonplaceholder.typicode.com/users/1/posts**. (Du kannst diese URL zum Testen im Browser aufrufen)

```python
# JSON Library
import json
# urllib Library
import urllib.request

# request data from url
with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/1/posts') as response:
  # read data in response
  html = response.read()
  # get content encoding
  encoding = response.info().get_content_charset('utf-8')
  # create a Dictionary
  JSON_object = json.loads(html.decode(encoding))
  print(JSON_object)
```

Danach ersetllen bitte eine response.csv, die so wie in Challenge 3, neben deiner Python Datei abgelegt wird. Prüfe bitte mit Excel, ob dein erstelltes CSV File lesbar und verarbeitbar ist oder teste die Datei online mit dem CSV Validator: [https://csvlint.io/](https://csvlint.io/)

## Bonus-Aufgabe:

Als Bonus versuche eine gültige XML Datei zusätzlich zur CSV Datei zu erstellen.
Hier kannst du die XML Datei auf Gültigkeit validieren: [https://www.xmlvalidation.com/](https://www.xmlvalidation.com/?L=2)

## Hilfsmittel:

- [Challenge 3, arbeiten mit Dateien](https://github.com/joeherold/wcc_fh_wkw_python/tree/master/Challenge_3)
- [CheatCheet für Basics](https://teams.microsoft.com/l/file/577FC335-F5B4-4A56-B307-D7ED57E48403?tenantId=b8192970-931b-4546-97ce-a6a611c24bd9&fileType=pdf&objectUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345%2FFreigegebene%20Dokumente%2FWeekly%20Coding%20Challenge%2FMaterialien%2Fbeginners_cheat_sheet.pdf&baseUrl=https%3A%2F%2Ffhwzid.sharepoint.com%2Fsites%2FAT_DiBBA_2019_876338345&serviceName=teams&threadId=19:a6077bbb7c794716aef8ef6264849648@thread.skype&groupId=fe5a1a58-19cb-498f-88e0-617b2206af7e),
- Fragen [als Issue](https://github.com/joeherold/wcc_fh_wkw_python/issues) oder als [Formular](https://forms.office.com/Pages/ResponsePage.aspx?Host=Teams&lang=%7Blocale%7D&groupId=%7BgroupId%7D&tid=%7Btid%7D&teamsTheme=%7Btheme%7D&upn=%7Bupn%7D&id=cCkZuBuTRkWXzqamEcJL2Rcv0_AVGQVMpyxsXq73-hxUOUM1QVo0WTA3T1dOSEQ3NkxCN0Y1MjZBUC4u) erstellen.

**VIEL ERFOLG! Gemeinsame Auflösung nächstes Wochenende**
