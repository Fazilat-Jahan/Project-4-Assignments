def main():
    age = int(input("Enter your age to find eligibility for Election: "))
    print("\n")
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else: 
        print("You can not vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else: 
        print("You can not vote in Stanlau where the voting age is 25.")       

    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else: 
        print("You can not vote in Mayengua where the voting age is 48.")       


if __name__ == "__main__":
    main()
