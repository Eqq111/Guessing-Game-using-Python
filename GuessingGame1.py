


#generate a random number between 1 and 100
randnum = random.randint(1,101)

count = 0
guess = -99

while (guess != randnum):
    #Get the user's guess
    guess = (
    if guess < randnum:
            print ("higher")
    else guess > randnum:
            print ("lower")
    else:
            print ("you guessed it!")
            break
    count = count +1
#end of while loop
