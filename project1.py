import random


def roll():
    min_value = 1
    max_value = 6
    roll_ = random.randint(min_value, max_value)
    return roll_


while True:
    players = input('Enter the number of players (2 - 4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4")
    else:
        print('Invalid, Try again.')

max_scores = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_scores:
    for player_inx in range(players):
        print("\nPlayer number", player_inx + 1, 'turn has just started!\n')
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break
            value = roll()
            if value == 1:
                print('You rolled a 1! Turn done')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a ', value)
            print('Your score is ', current_score)
        player_scores[player_inx] += current_score
        print('Your total score is: ', player_scores[player_inx])
