def main():
    divide = float(input("Enter a number to divided: "))
    divided = float(input("Enter a number to divide by: "))

    remainder = divide % divided
    quotient = divide // divided

    print(f"The result of {divide}/{divided} is {quotient} with a remainder of {remainder}")


if __name__ == "__main__":
    main()
