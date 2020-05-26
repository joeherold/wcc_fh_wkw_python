def removeTrailingNewLine(value):
    return value.rstrip("\n")
def addTrailingNewLine(value):
    return value + ("\n")

def readFileAndGetAsList(pathToFile):
  f = open(pathToFile, "r")
  if f.mode == 'r':
    contents = f.readlines()
    f.close()
    return list(map(removeTrailingNewLine, contents))
  else:
    return []

    
def writeListToFile(pathToFile, dataAsList=[]):
  f = open(pathToFile, "w+")
  listWithNewsLintes = list(map(addTrailingNewLine, dataAsList))
  f.writelines(listWithNewsLintes)
  f.close()



pathToFile = "/Users/johannespichler/Development/FHWKW/WeeklyCodingChallenge/weekly_coding_challenge_fwkwkw_python/Challenge_3/tasks.txt"

lines = readFileAndGetAsList(pathToFile)
print(lines)
lines.append("holladrio")
print(lines)
writeListToFile(pathToFile, lines)