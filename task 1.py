import random
guesses_allowed = 10
print("Welcome to the guessing game!")
number = random.randint(1,100)
for i in range(guesses_allowed):
    guess = int(input("What's your guess? "))
    if guess == number:
        print("Congratulations, you guessed the number!!, Would you like to play again?")
        break
    else:
        if guess > number:
            print("Your guess is too high. Try again.")
        else:
            print("Your guess is too low. Try again.")
if guess != number:
    print("Sorry, you didn't guess the number")
