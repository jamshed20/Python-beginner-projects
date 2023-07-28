import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess < random_number:
            print('Sorry. Guess again. Too low.')
        elif guess > random_number:
            print('Sorry. Guess again. Too high.')

    print(f'Yay. You have guessed the number {random_number} correct.')

# guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C'and low != high :
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high(H), too low(L) or correct(C) : ')
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1

    print(f'Yay. Computer guessed your number {x} correctly.')


computer_guess(20)
