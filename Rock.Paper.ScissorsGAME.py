import random

# Introduction to game. Gives the instructions.
def introduce_game():
    print('Rock. Paper. Scissors.' '\n' 'Enter 1 for Rock, 2 for Paper or 3 for Scissors.', '\n')
    enter_player_answer()


# Generate Random Integers.
def generate_random_int():
    return random.randrange(1,3)

# Function that gets player choice with validation loop.
def enter_player_answer():
    player = int(input('Enter your choice: '))
# Input validation loop
    while player != 1 and player != 2 and player != 3:
        print('invalid entry. Please try again. ')
        player = int(input('Enter 1, 2, 3:'))
    display_computer_answer(player)

# Function that displays computer answer
def display_computer_answer(player):
    c_answer = generate_random_int()
    print('Computer picks', c_answer, '\n')
    determine_winner(c_answer, player)

# function that determines the winner.
def determine_winner(c,p):
    if c == p:
        print('Try again.')
        enter_player_answer()
    elif c == 1 and p ==2:
        print('Paper covers rock. Player Wins! ')
    elif c == 1 and p == 3:
        print('Rock smashes scissors. Computer Wins! ')
    elif c == 2 and p == 1:
        print('Paper Covers Rock. Computer Wins!')
    elif c == 2 and p == 3:
        print('Scissors cut paper. player wins ')


introduce_game()




