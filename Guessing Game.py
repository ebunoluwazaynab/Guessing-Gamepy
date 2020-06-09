"""
This is a guess the number game

using python
"""

import random
print("NUMBER GUESSING GAME")

# ask user for name
print("Hello!, What is your name?")
name = input()
print(f"{name},I am thinking of a number between 1 to 20, guess the number ")


def guesses():
    # randint function to generate a random number between 1 to 30
    number = random.randint(1, 30)

    # to play again
    def try_again():
        retry = input("Enter Yes to retry\nEnter No to end game: ").lower()
        if retry == 'yes':
            guesses()
        elif retry == 'no':
            print("Thank you for your time")
            exit()
        else:
            print('Invalid output')
            try_again()

    # hint that tells user if guess is an even or odd number
    def hint():
        if number % 2 == 0:
            print("Hint: An even number")
        elif number % 2 != 0:
            print("Hint: An odd number")

    # number of tries to be given to user to guess the number
    tries = 0

    # tries are 5
    # while loop to count the number of tries
    while tries < 5:

        # Enter a number between 1 to 30
        print("Take a guess.")
        guess = int(input())

        # Compare the user entered number with the number to be guessed

        # if number entered by user is same as the generated number by randint function
        if guess == number:
            print("Congratulations! You won.")
            try_again()

        # if guess is not from 1 to 30
        if guess > 30 or guess < 0:
            print("You have to guess from 1 to 30")

        # check if number entered is less than the generated number
        elif guess < number:
            print("Your guess was too low: Guess a number higher than", guess)
            hint()

        # check if number entered is higher than the generated number
        elif guess > number:
            print("Your guess was too high: Guess a number lower than", guess)
            hint()

        # Increase the value of tries by 1
        tries += 1
    # if user didn't guess the number right
    if not tries < 5:
        print("YOU LOSE!! The number is", number)
        try_again()


guesses()

