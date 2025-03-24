def main():
    user_input= float(input("Type a number to check its square: "))
    square= user_input**2
    print(f"{user_input} squared is {square}") #first method

    # or using pow() function for the same purpose.
    print(f"{user_input} squared is {pow(user_input,2)}") 


if __name__ == "__main__":
    main()
