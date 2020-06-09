#Imports the random library
import random

# Creates a list called rps with the words rock, paper, and scissors
rps = ["rock", "paper", "scissors"]

# Asks the user for their name
name = input("What is your name? ")
# Prints the user's name with hello and a description of the game
print("Hello " + name, "This is a game of rock, paper and scissors. You can play as long as you want. If you are done playing, you can exit. Have fun!")

for i in rps:
    print(i)
rps_person = input("Pick one: ")

rps_comp = random.choice(rps)

print(rps_comp)

while rps_person != "exit":

    if (rps_person == "rock" and rps_comp == "scissors"):
        print("You won, " + name)
        
    elif (rps_person == "rock" and rps_comp == "paper"):
        print("Sorry " + name, "but you lost")

    elif (rps_person == "paper" and rps_comp == "rock"):
        print("You won, " + name)

    elif (rps_person == "paper" and rps_comp == "scissors"):
        print("Sorry " + name, "but you lost")

    elif (rps_person == "scissors" and rps_comp == "rock"):
        print("Sorry " + name, "but you lost")

    elif (rps_person == "scissors" and rps_comp == "paper"):
        print("You won, " + name)

    elif (rps_person == "rock" and rps_comp == "rock"):
        print("Tied game, " + name)

    elif (rps_person == "paper" and rps_comp == "paper"):
        print("Tied game, " + name)

    elif (rps_person == "scissors" and rps_comp == "scissors"):
        print("Tied game, " + name)

    print("The computer picked " +rps_comp)
    
    rps_person = input("Pick one: ")

    rps_comp = random.choice(rps)
    