#Schreibe eine Schleife (z.B. while, oder for...) mit der du die unten angegebene Liste aufsteigende sortierst.
#Es ist keine eingebaute Sortierfunktion erlaubt, sondern muss mit einfachen Rechenoperatoren wie <, > if, elif, ... gelöst werden.
# gegebene Liste
myNumberList = [25, 45, 25, 78, 21, 14, 87, 32, 57, 54]
emptyList = []
# gewünschtes Ergebnis
mySortedNumberList = [14, 21, 25, 25, 32, 45, 54, 57, 78, 87]
print("######################################################################")
while myNumberList:
    minimum = myNumberList[0]
    for numbers in myNumberList:
        print("for.numbers: ", numbers)
        if numbers < minimum:
            minimum = numbers
            print("minimum: ", minimum)
    emptyList.append(minimum)
    print("vorher: ", myNumberList)
    print("remove: ", minimum)
    myNumberList.remove(minimum)
    print("nachher :", myNumberList)   
print("######################################################################")
print(emptyList)
 
#Bonus Aufgabe: War das davor zu leicht? Dann löse folgendes: Fülle die fehlenden Zahlen dazwischen mit 0 auf.
# gewünschtes Ergebnis
myFancySortedNumberList = [14, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 25, 25, 0, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 78, 0, 0, 0, 0, 0, 0, 0, 0, 87] 

zeroList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(len(zeroList))

emptyList.insert(1, zeroList[2:8])
emptyList.insert(3, zeroList[2:5])
emptyList.insert(6, zeroList[2:8])
emptyList.insert(8, zeroList[1:13])
emptyList.insert(10, zeroList[2:11])
emptyList.insert(12, zeroList[2:4])
emptyList.insert(14, zeroList[2:22])
emptyList.insert(16, zeroList[2:10])

print(emptyList)
