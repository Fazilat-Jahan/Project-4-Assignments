def main():
        fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
        total_costs =0
        for fruit in fruits:
            price = fruits[fruit]
            amount= int(input(f"\nHow many {fruit.upper()} do you want to buy?: "))
            total_costs +=( price * amount)
        print(f"\nYour Total cost: ${total_costs}")



if __name__ == "__main__":
    main()
