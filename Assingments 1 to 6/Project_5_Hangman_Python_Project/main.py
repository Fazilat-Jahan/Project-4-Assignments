import random
from words import words  # Assuming 'words' is your noun list
import string

def main(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Convert word to uppercase

def hangman():
    word = main(words)  # Now word is uppercase, e.g., "APPLE"
    word_letters = set(word)  # Letters in the word, e.g., {'A', 'P', 'L', 'E'}
    alphabet = set(string.ascii_uppercase)  # Uppercase alphabet
    used_letters = set()  # Letters guessed by user

    # Game loop
    while len(word_letters) > 0:
        print("\nYou have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_list))
        
        user_letter = input("\nGuess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("\nLetter is not in the word.")
        elif user_letter in used_letters:
            print("\nYou have already used that letter. Try again.")
        else:
            print("\nInvalid character. Please try again.")

    # Removed redundant input block; loop handles all guesses
    print("\nCongratulations! You guessed the word:", word)



if __name__ == "__main__":
    hangman()