def read_phoneNumbers():
    phonebook={}

    while True:
        name = input("Name: ")
        if name == "":
            break

        number = input("Number: ")
        if number == "":
            break

        phonebook[name] = number
    return phonebook

# def print_phonebook(phonebook):
#     for name in phonebook:
#         print(f"{name}={phonebook[name]}")
   

def lookup_phonebook(phonebook):  
     while True:
        name = input("Enter name to search, or just enter nothing to exit: ")
        if name == "":
            break
        if name not in phonebook:
            print("Not found")
        else:
            print(f"{name}: {phonebook[name]}")          

def main():
    phonebook = read_phoneNumbers()
    # print_phonebook(phonebook)
    lookup_phonebook(phonebook)


if __name__ == "__main__":
    main()
