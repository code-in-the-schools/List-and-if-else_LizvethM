###Part1
userInput = input(str("Type anything here :D "))
print(userInput.lower())
print()




###Part2
userInput2 = input(str("Type anything here :D "))


for i in range(len(userInput2)):
  list= userInput2[i]
  if(list=="a" or list=="e"or list=="i"or list== "o" or list== "u"):
    print(str(list)+" | Vowel")
  else:
    print(str(list)+" | Consonant")
