
secret_numbers = 23
guess = 0

while guess != secret_numbers:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < secret_numbers:
        print("Too low!")
    elif guess > secret_numbers:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number!")
