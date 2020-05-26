'''
CHALLENGE #2
GET PRIME NUMBERS
'''
# the function generate the prime numberes output
# it has two parameters: start and count
def getPrimeNumbers(start, count):
  # get the start variable as cv (cur)
  cv = start
  # we create a counter for the number of found prime numbers
  found = 0

  # if count is not a positive number, we default it to 1
  if (not count > 0):
    count = 1
  # if the start value is lower than 3, we default it to 3
  if (cv < 3):
    cv = 3
  # we do an iteration, as long as our found variable
  # is lower then the desired count
  while count > found:
    # here we iterate over each value starting from 2 ... currentValue in
    # steps of: 2,3,4,5....,currentValue
    for divider in range(2, cv, 1):
      # then we check if the division has no rest
      # for prime numbers, this should only be the number itself
      if cv % divider == 0:
        # if yes, this is not a prime number
        # we increase the current value and stop the for loop
        # to get back to the outer while loop
        cv += 1
        break
      
      if divider == cv - 1:
        # here we reached the almost last number ( currentValue - 1 )
        # so the if clause before had a rest, so this value is the last
        # value before we would divide by itself => Yeah, this currentValue
        # is a prime number, so we increase the found number, print it out and increase
        # the current vlue
        found += 1
        print(f"{found}) \t {cv}")
        cv += 1

# same function without comments, to illustrate
# it takes only 15 lines of code
def getPrimeNumbersShort(start, count):
  cv = start
  found = 0
  if (not count > 0):
    count = 1
  if (cv < 3):
    cv = 3
  while count > found:
    for divider in range(2, cv, 1):
      if cv % divider == 0:
        cv += 1
        break
      if divider == cv - 1:
        found += 1
        print(f"{found}) \t {cv}")
        cv += 1


print("THE FABULOUS PRIME NUMBERS CALCULATOR\n")
print("Where should we start?:")
start = input()
print("How many Prime Numbers do you want?")
count = input()
try:
  start = int(start)
  count = int(count)
  print("OK, calculating Prime numbers:")
  getPrimeNumbers(start, count)
except:
  print("This only works, if you privide numbers only")
finally:
  print("THIS WAS THE FABULOUS PRIME NUMBERS CALCULATOR\n")
