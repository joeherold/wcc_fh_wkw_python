# gegebene Liste
myNumberList = [25, 45, 25, 78, 21, 14, 87, 32, 57, 54]
# gewünschtes Ergebnis
# mySortedNumberList = [14, 21, 25, 25, 32, 45, 54, 57, 78, 87]

# Bonusaufgabe
# gewünschtes Ergebnis ist das Auffüllen der leeren Stellen zwischen den Zahlen mit 0
myFancySortedNumberList = [14, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 25, 25, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0, 87] 

# sortieren der Liste
# Anzahl der Eingträge
# wenn eintrag größer dann weiter
# wenn eintrag kleiner dann vorher einfügen 
# einfügen mit append an letzter Stelle
# verwenden der Count funktion
# vergleich der Einträge von vorne bis zum letzten


def sortieren():
    count = 0
    stop = len(myNumberList) - 1
    while count < stop:
        #print(list(myNumberList))
        if myNumberList[count] > myNumberList[count + 1]: # Wenn größer, dann ausschneiden und eine Position danach einfügen. 
            #print(myNumberList[count],">=",myNumberList[count + 1])
            #print("Count steht bei: ",count,"- Nr. ",myNumberList[count])
            value = myNumberList[count]
            #print("Count + 1 = ",count + 1)
            del myNumberList[count]
            newPosition = count + 1
            newPosition = int(newPosition)
            myNumberList.insert(newPosition, value)
            print(myNumberList)
            count = 0    
        elif myNumberList[count] <= myNumberList[count + 1]: # Wenn kleiner gleich, dann eine Position weiter gehen. 
            #print(myNumberList[count],"<=",myNumberList[count + 1])
            count += 1
        else:
            print("Es gibt einen Fehler")

# ausfüllen 
# Abfrage der Zahl
# Vergleich der Differenz zwischen Zahl 1 und 2
# Ausfüllen der Stellen bis Zahl 2 erreich ist
# weiter gehen zur zweiten Zahl

def ausfuellen(): # Füllt die 0er zwischen den Zahlen ein, entsprechend der fehlenden Stellen
    count2 = 0
    stop = len(myNumberList) - 1
    while count2 < stop:
        vergleich = myNumberList[count2 + 1] - myNumberList[count2]
        if  vergleich == 1:
            #print(myNumberList[count2 + 1]," - ", myNumberList[count2], " = ",myNumberList[count2 + 1] - myNumberList[count2])
            count2 += 1
        elif vergleich == 0:
            #print(myNumberList[count2 + 1]," - ", myNumberList[count2]," = ",myNumberList[count2 + 1] - myNumberList[count2])
            count2 += 1
        elif vergleich > 1:
            print("So viele 0 müssen eingefüllt werden:",vergleich - 1)
            abschnitt = count2 + vergleich - 1
            while count2 < abschnitt:
                count2 += 1
                myNumberList.insert(count2, 0)
            print(myNumberList)
            count2 += 1
        else:
            print("Done")
        stop = len(myNumberList) - 1

def sortierauftrag():
    print("Das ist die Anzahl der Zahlen:", len(myNumberList))
    print("Das ist die Liste der Zahlen:")
    print(list(myNumberList))
    print("")
    print("Jetzt werden diese sortiert:")
    sortieren()
    print("")
    print("Alle Nummern wurden sortiert:")
    print("")
    print(list(myNumberList))
    print("")
    print("Jetzt werden die Leerstellen aufgefüllt:")
    print("")
    ausfuellen()
    print("")
    print("Das ist die Lösung der Bonusaufgabe:")
    print(list(myNumberList))
    print("")
    print("Alle Aufgaben gelöst!")

sortierauftrag()
