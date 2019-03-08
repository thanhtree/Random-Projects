from random import randint

#Prints a string containing a random order of dancing monkeys for slack
#about 3727 or 4k characters long 
textlength = 4000
monkey = [":monkey2:",":monkeydance:",":dancingmonkey:"]
outputstring = []
currentlength = 0
while currentlength < textlength:
  tempstring = monkey[randint(0,2)]
  currentlength += len(tempstring)
  outputstring.append(tempstring)

print(outputstring)
