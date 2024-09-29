'''

We are going to write a program that generates a random number and asks the user to 
guess it.
If the player's guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user's guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number.
Hint: Use the random module


'''

import random
randomnum = random.randint(1,100)
print(randomnum)
count = 0
while True:
    count=count+1
    guess = int(input("Can you guess the number? "))
    if (guess == randomnum):
        print(f"Perfect ! Your guess {guess} is correct")
        print(f"Number of attempts are {count}")
        break
    elif(guess<randomnum):
        print("Please choose higher number")
    elif(guess>randomnum):
        print("Please choose lower number")
    else:
        print("Plese choose only numbers")
    

