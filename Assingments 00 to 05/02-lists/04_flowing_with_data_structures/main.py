def three_copies(list, data):
    for i in range(3):
        list.append(data)

def main():
        message= input("Enter a message to be repeated 3 times: ")    
        list =[]
        print("list before:", list)
        three_copies(list, message)
        print("list after:", list)
    


if __name__ == "__main__":
    main()
