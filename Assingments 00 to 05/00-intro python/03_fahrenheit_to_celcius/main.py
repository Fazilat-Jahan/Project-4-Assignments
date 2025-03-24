def main():
    degrees_fahrenheit= float(input("Enter temperature in Ferhenheit: "))
    celcius = (degrees_fahrenheit-32)*5.0/9.0
    print(f"{degrees_fahrenheit}°F in celcius is {celcius}°C")

if __name__ == "__main__":
    main()
