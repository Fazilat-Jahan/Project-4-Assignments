import random
def main():
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)

    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total of two Dice: {dice1 + dice2}")


if __name__ == "__main__":
    main()
