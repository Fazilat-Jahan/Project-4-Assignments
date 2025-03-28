def main():
    massToKg= float(input("Enter kilos in mass: "))

    energyInJoule: float=  massToKg * (299792458**2)

    print("E=m*c^2")
    print(f"m= {massToKg} kg")
    print("c=299792458 m/s")
    print(f"{energyInJoule} Joules of energy")
# upper code is required onr and below is mine editionn
    print("\n\n")
    print(f"Mass in kg: {massToKg}")
    print("Speed of light in m/s: 299792458")
    print(f"Energy in Joules: {energyInJoule}")


if __name__ == "__main__":
    main()
