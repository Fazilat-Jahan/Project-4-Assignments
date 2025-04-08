def get1st_element(firstE):
    print(firstE[0])

list=[]
while True:
    element= input("Enter a list element (or type 'done' to finish): ")
    if element.lower() == 'done':
        break
    list.append(element)
get1st_element(list)    





