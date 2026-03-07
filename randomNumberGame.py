#Making a number guessing game just to get back into coding
import random #to randomly generate numbers

Username = input("Enter your name: ")#stores users name

#Introductory message
def intro():
    print(f"Welcome to the guessing game {Username}\nInstructions:\nEnter a number between 1 and 5.\n"
          "If the number you entered matches the generated number, you win. Else you lose.\n3 attempts\n")

#getting user num
def getNum():

    while True:
        try:
            number = int(input("Enter a number between 1 and 5: "))
            if 1 <= number <= 5:
                return number
            else:
                print("Please stay within the range (1-5).")
        except ValueError:
            print("Invalid input! Please enter a whole number.")

#comparing user entry to see if they guessed correctly
def play():
    intro()
    attempts = 3 #number of attempts user has

    while attempts > 0:
        number = getNum()
        actualNumber = random.randint(1, 5)

        if number == actualNumber:
            print(f"\nCongratulations {Username}, you won!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong! The number was {actualNumber}.")
                print(f"You have {attempts} attempts left.\n")
            else:
                print(f"Wrong! The number was {actualNumber}.")
                print(f"\nGame Over, {Username}. You've run out of attempts.")

#Play game
play()