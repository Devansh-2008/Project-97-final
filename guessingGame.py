import random

number = random.randint(1, 9)

chances=0

print("Print a number between 1 and 9")
print("You have 5 chances")

while chances < 5:
    numberGuess = int(input("Enter your guess: "))
    chances = chances + 1

    if numberGuess < number:
        print("Your guess is too low! Guess a number higher than ", numberGuess)
        
    if numberGuess > number:
        print("Your guess is too high! Guess a number lower than ", numberGuess)

    if numberGuess == number:
        print("Congratulations YOU WON!!!")
        break

    if not chances < 5:
        print("You LOSE!!! The number is ", number)
        