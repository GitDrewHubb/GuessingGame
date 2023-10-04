## ANDREW NALLY
## CIS261 - OOP1
## Guessing Game - Console Application
## 10/04/2023

import random

#function to display the heading
def display_heading():
    print("*************************")
    print("Guessing Game: Guess A Number!")
    print("Guess the number I am thinking of for the win!")
    print("May the odds forever be in your favor!")
    print("*************************")


#function to play the game
def play_game():
    #Generates a random number between 1 and the limit
    random_number = random.randint(1, limit)
    print(f"I have selected a number between 1 and {limit}.")
    #keeps track of the number of attempts the user takes to guess the correct number
    attempts = 0
    #the first while loop
    while True:
       try:
           # Prompts the user to guess a number
           guess = int(input("Enter your guess: "))
           
            #adds 1 to the total of attempts
           attempts += 1
           #compares the user's guess to the generated random number
           if guess == random_number:
               print(f"Congratulations! You have guessed the right number {guess} in {attempts} attempts. ")
               break
           elif guess < random_number:
               print("Too low. Try again")
           else: 
               print("Too high. Try again")
               #added exception handling for when the user enters an invalid number the program wont break
       except ValueError:
           print(f"Invalid number. Enter a valid number from 1 to {limit}.")
#function to prompt the user to play again       
def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice =='y':
            play_game()
        elif choice == 'n':
            return False
        else:
            print("Invalid answer. Enter 'y' for yes and 'n' for no")
            
#Main
display_heading()

while True:
    limit =  int(input("Enter a number greater than 5 for the number range: "))
    play_game()
    
    if not play_again():
        print("Good game friend! Goodbye!")
    break