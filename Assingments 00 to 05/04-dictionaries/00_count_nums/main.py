def get_numbers():
    user_numbers =[]
    while True:
        user_input= input("Enter a number or 'done' to finish: ")
        if user_input.lower() == 'done':
            break

        user_numbers.append(user_input) 
    return user_numbers

def count_numbers(number):
    num_dict ={}
    for num in number:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_numbers(num_dict):
    for num in num_dict:
        print(f"{num} appears: {num_dict[num]} times")
    



def main():
    user_numbers = get_numbers()
    num_dict= count_numbers(user_numbers)
    print_numbers(num_dict)


if __name__ == "__main__":
    main()
