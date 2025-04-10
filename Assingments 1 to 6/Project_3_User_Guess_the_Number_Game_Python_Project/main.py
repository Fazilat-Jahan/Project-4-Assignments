import random
def main(x):
    low =1
    high =x
    feedback =""

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess= low

        feedback = input(f"\nIs {guess} too high (h), too low (l), or correct (c)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"\nCongrats! The Computer Guessed Your number {guess} Correctly!")

    


if __name__ == "__main__":
    main(10)
