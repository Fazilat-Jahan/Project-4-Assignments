def getLast_element(last):
    print(last[-1])


list=[]
while True:
    element= input("Enter an element (or 'done' to finish): ")
    if element.lower() == 'done':
        break
    list.append(element)

getLast_element(list)