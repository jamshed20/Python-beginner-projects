import random

def play():
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n")
    computer = random.choice(['R', 'P', 'S'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') \
        or (player == 'P' and opponent == 'R'):
        return True

print(play())
