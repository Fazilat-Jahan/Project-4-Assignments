import random

def main():
    print("I am thinking of a number between 0 and 99...\n")
   
    numbers = int(input("Guess any number: "))
    random_number= random.randint(0, 9)
    while numbers != random_number:
        if numbers == "":
            print("\nOh! You Quit")
            break
        
        elif int(numbers) < random_number:
            print("\nYour guess is too low")
            
        else:
           print("\nYour guess is too high")
        

        numbers = input("\nEnter New Number: ")      
        
    print("\nCorrect Number was", random_number)

    
   


if __name__ == "__main__":
    main()
