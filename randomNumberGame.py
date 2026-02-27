#Making a number guessing game just to get back into coding
import random #to randomly generate numbers

Username = input("Enter your name: ")#stores users name
number = 0 #stores their guess
actualNumber = 0 #python generated number
attempts = 3 #number of attempts user has

#Introductory message
def intro():
    print(f"Welcome to the guessing game {Username}\nInstructions:\nEnter a number between 1 and 5.\n"
          "If the number you entered matches the generated number, you win. Else you lose.\n3 attempts\n")
#generating num
def printNum():
    global actualNumber

    actualNumber = random.randint(1, 5)
    return actualNumber

#getting user num
def getNum():
    global number

    number = int(input("Enter a number between 1 and 5: "))
    return number

#comparing user entry to see if they guessed correctly
def numberEntry():
    global attempts

    while attempts > 0:
        if number == actualNumber:
            print(f"\nCongratulations {Username}, you won!")
            exit()
        elif number != actualNumber:
            attempts -= 1
            print(f"\nSorry, {Username}, you lost!\n"
                  f"Number was {actualNumber}.\nYou have {attempts} attempts left\n")
            getNum()
            printNum()
        else:
            print(f"\nSorry, {Username}, you lost. Better luck next time.")

#basically main: starting the game
intro()
getNum()
numberEntry()