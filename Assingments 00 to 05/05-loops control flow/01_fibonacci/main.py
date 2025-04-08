max_value: int= 10000
def main():
    current_term = 0
    next_term =1

    while current_term <= max_value:
        print(current_term)
        after_next_term = current_term + next_term
        current_term = next_term
        next_term = after_next_term


if __name__ == "__main__":
    main()
