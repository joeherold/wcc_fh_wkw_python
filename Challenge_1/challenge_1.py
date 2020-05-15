'''
CHALLENGE #1
SORT LISTS manually
https://repl.it/repls/LostKnobbyTree
'''

# given list to be sorted
myNumberList = [25,45,25,78,21,14,87,32,57,54]
print("before sorting") 
print(myNumberList) 

# we get the length of the list
length = len(myNumberList)

# we create a runner variable
currentIndex = 0

# we loop over the items and compare allways two values
while currentIndex < length-1:
  # we get te number at the current index
  currentNumber = myNumberList[currentIndex]
  # we get the number right next to it
  nextNumber = myNumberList[currentIndex+1]
  # if the next number is smaller than the current number
  # we have to reattanger them
  if(nextNumber < currentNumber):
    # here we switch the both numbers
    myNumberList[currentIndex] = nextNumber
    myNumberList[currentIndex+1] = currentNumber
    # then we reset the index to zero to start again from the beginning
    currentIndex = 0
  else:
    # otherwise we increate the index to process the next number pair
    currentIndex+=1

# finally we prent the result to the console
print("after sorting") 
print(myNumberList) 



'''
CHALLENGE #1 BONUS
ADD 0 BETWEEN THE NUMBERS
'''
# for the super motivated, here the bonus challenge
print("bonus sorting, add 0 in between")

# we get the length of the list again
length = len(myNumberList)
# then we start at the last number in the list
currentIndex = length - 1
# we iterate again over the numbers
while currentIndex >= 1:
  # we get the number at the current position
  currentNumber = myNumberList[currentIndex]
  # we get the number before it
  prevNumber = myNumberList[currentIndex-1]
  # we check if the distance is greater 1 and if the prev
  # example 87 - 78 = 9 so greater 1, we need to put 0 in between
  distance = currentNumber - prevNumber
  # if the distance is greater 1
  if(distance > 1):
    # here we put as many 0 in between, as the distance is long
    for x in range(1, distance):
      myNumberList.insert(currentIndex, 0)
  # else we go to the next number one index below
  else:
    currentIndex-=1
 

print("bonus sorting after sorting") 
print(myNumberList) 
