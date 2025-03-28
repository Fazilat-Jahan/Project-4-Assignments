import math
def main():
    ab = float(input("Enter the length of side AB: "))
    ac = float(input("Enter the length of side AC: "))

    bc: float= math.sqrt(ab**2 + ac**2)
    print("The length of side BC is:", bc)


if __name__ == "__main__":
    main()
