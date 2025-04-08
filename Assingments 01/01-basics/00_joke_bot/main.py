def main():
    prompt: str = "What do you want?"
    joke:str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs."
    excuse:str = "Sorry I only tell jokes."

    user_input = input(f"{prompt}:  ")
    if "joke" in user_input:
        print("\n",joke)
    else:
        print("\n",excuse)
  




if __name__ == "__main__":
    main()
