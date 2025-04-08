def get_list():
    list = []
    while True:    
        value= input("enter a value: ")
        if value == "":
            print("here's the list:", list)
            break
        list.append(value)

get_list()