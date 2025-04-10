import random

def play():
    user = input("Enter your choice: r for 'rock', p for 'paper', s for 'scissors'): ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Oh! It is a tie!'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    # Return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
       


if __name__ == "__main__":
    print(play())  
