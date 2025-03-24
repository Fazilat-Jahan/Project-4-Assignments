import random
sides =6

def dice_roll():
    """Simulates rolling two dice and prints their total!"""
    dice1 = random.randint(1, sides)
    dice2 = random.randint(1, sides)
    total = dice1 + dice2
    print(f"Rolling... dice1: {dice1}, dice2: {dice2}, Total of two dice is: {total}")
def main():
    dice1 = 10
    print(f"\ndice 1 starts as = {dice1}")
    dice_roll()
    dice_roll()
    dice_roll()
    print(f"dice 1 end as = {dice1}")



if __name__ == "__main__":
    main()
