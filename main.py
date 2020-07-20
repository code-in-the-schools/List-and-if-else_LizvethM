###Part1
userInput = input(str("Type anything here :D "))
print(userInput.lower())
print()
uInput= userInput.lower()

vowels= 0
consonants= 0


###Part2


for i in range(len(uInput)):
  list= uInput[i]
  if(list=="a" or list=="e"or list=="i"or list== "o" or list== "u"):
    print(str(list)+" | Vowel")
    vowels = vowels+1

  else:
    print(str(list)+" | Consonant")
    consonants= consonants+1

print()
print("There are "+str(vowels)+ " vowels")
print("There are "+str(consonants)+ " consonants")




