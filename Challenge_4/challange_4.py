
def getAbstand(p1, p2): 
  # Calculate distance between two point tupels

  # frist get delta x
  x1 = p1[0]
  x2 = p2[0]
  deltaX = x2 - x1

  # then get delta y
  y1 = p1[1]
  y2 = p2[1]
  deltaY = y2 - y1

  # then we take advantage of Pythagoras a^2 + b^2 = c^2
  distance = ( deltaX**2 + deltaY**2 ) ** 0.5

  return distance


def getUmfang(p1, p2, p3):
  # here we sum up the distances between the three points
  a = getAbstand(p1, p2)
  b = getAbstand(p2, p3)
  c = getAbstand(p3, p1)
  return (a + b + c)

def getFlaeche(p1, p2, p3):
  # with semiperimeter by the Heron Formlar
  # s = (a + b + c)/2 = Umfang / 2
  
  a = getAbstand(p1,p2)
  b = getAbstand(p2,p3)
  c = getAbstand(p3,p1)

  # semiparameter
  s = (a + b + c)/2
  
  # Heron Fomulrar: area = ( s * (s - a) * (s - b) * (s - c) )^0.5
  return (s * (s-a) * (s-b) * (s-c))**0.5


def getSchwerpunkt(p1, p2, p3):
  # S = (A+B+C)/3
  return (
    (p1[0]+p2[0]+p3[0])/3 , # x = (x1 + x2 + x3) / 3
    (p1[1]+p2[1]+p3[1])/3   # y = (y1 + y2 + y3) / 3
    )
 

# This function is ment to generalize the point input and conversion
def enterPoint(nameOfPoint):
  # we wrap the input and conversion in a try block
  # to handle wrong inputs...
  try:
    print(f"Punkt {nameOfPoint}: x,y")
    pointInput = input()
    arrPoint = pointInput.split(",")
    return (float(arrPoint[0]), float(arrPoint[1]))
  except:
    print(f"Deine Eingabe {pointInput} war ungüligt. Es wird stattdessen der Punkt 0,0 verwendet")
    return (0,0)
  
  


def main():
  print("### Magic Triangle ###")
  print("Bitte gebe 3 Punkte an, aus denen ein Dreieck gebildet wird")
  A = enterPoint("A")
  B = enterPoint("B")
  C = enterPoint("C")

  umfang = getUmfang(A,B,C)
  schwerpunkt = getSchwerpunkt(A,B,C)
  flaeche = getFlaeche(A,B,C)

  print(f"Umfang: {round(umfang,3)}cm")
  print(f"Semiperimeter (Halbumfang): {round(umfang/2,3)}cm")
  print(f"Schwerpunkt: x={round(schwerpunkt[0],3)}cm, y={round(schwerpunkt[1],3)}cm")
  print(f"Fläche: {round(flaeche,3)} cm^2")

main()