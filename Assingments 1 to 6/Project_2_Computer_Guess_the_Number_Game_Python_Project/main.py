import random

def main(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess= int(input(f"\nGuess a number b/w 1 to {x}: "))
        if guess < random_number:
            print("\nSorry! Your Guess is Too low")
        elif guess > random_number:
            print("\nSorry! Your Guess is Too high")
       
    print(f"\nCongrats! You guessed the {random_number} number right!")


if __name__ == "__main__":
    main(10)
