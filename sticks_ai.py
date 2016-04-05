import random


def ai_bot_create_dict(number_of_sticks):
    hat_dict = {}
    stick_count = 0
    while stick_count < number_of_sticks:
        hat_dict[stick_count] = [1, 2, 3]
        stick_count +=1
    return hat_dict


def did_ai_win_or_lose(player, game_over):
    if player == 'AI Bot' and game_over == True:
        print('AI Bot lost!')
        False
    elif player != 'AI Bot' and game_over == True:
        print('{} lost!'.format(player))
        True


def ai_bot_turn(number_of_sticks, hat_dict, good_guesses):
    this_turns_guess = random.choice(hat_dict[number_of_sticks])
    good_guesses[number_of_sticks] = this_turns_guess
    return this_turns_guess, good_guesses

# def update_ai_hat_dict(good_guesses, hat_dict):
#     for sticks in good_guesses:
