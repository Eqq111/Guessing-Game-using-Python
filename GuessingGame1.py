#Get the user's guess
guess = (int) (input("Enter your guess between 1 and 100:"))

#generate a random number between 1 and 100
randnum = random.randint(1,101)

if guess < randnum:
  print ("higher")
else guess > randnum:
  print ("lower")
else:
  print ("you guessed it!")
