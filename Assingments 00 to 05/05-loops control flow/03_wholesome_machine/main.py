affirmation : str = "I am capable of doing anything"
def main():
    # print("\nplease type the following affirmation:", affirmation)
    print(affirmation)
    user_input = input("\nplease type the following affirmation:\n ")
    while affirmation != user_input:
        print("\nIncorrect! Try again.\n")
        print(affirmation)
        
        user_input = str(input("\nplease type the following affirmation: "))

    print("\nCorrect! You typed the affirmation correctly.")
    print("Thank you for participating in this affirmation exercise.")
    print("You are capable of doing anything.")


if __name__ == "__main__":
    main()
