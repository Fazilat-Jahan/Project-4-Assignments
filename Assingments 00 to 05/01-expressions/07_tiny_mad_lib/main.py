def main():
    sentenced = "Coding is my hobby & Code with coffee is fun, but "
    print("\nWelcome to the madlib game!")
    print("In this game, you will create a fun sentence by filling in the blanks.")
    print("You will be asked to provide an adjective, a noun, and a verb.")
    print("The madlib will be displayed at the end.")
    print("hint: sentence is about coding")
    print("Let's get started!")
    advjective = (input("please type adjective: "))
    noun = (input("please type noun: "))
    verb = (input("please type verb: "))
    sentence = sentenced + advjective + " " + noun + " " + verb

    print(f"{sentence}")



if __name__ == "__main__":
    main()
