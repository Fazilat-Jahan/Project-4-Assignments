max_length =3
def shorten(element):
    while len(element) > max_length:
        removed = element.pop()
        print(f"Removed {removed} from list{element}")

def main():
    lists=[]
    while True:
        item =input("Enter an item (or 'done' to finish): ")
        
        if item.lower() =='done':
            break
        lists.append(item)
        
    shorten(lists)
    print(f"final list: {lists}")



if __name__ == "__main__":
    main()
