import random





def did_ai_win_or_lose(player, game_over):
    if player == 'A.I. Bot' and game_over == True:
        print('A.I. Bot lost!')
        return False
    elif player != 'A.I. Bot' and game_over == True:
        print('{} lost!'.format(player))
        return True


def ai_bot_turn(number_of_sticks, hat_dict):
    this_turns_guess = int(random.choice(hat_dict[number_of_sticks]))
    return this_turns_guess


def if_ai_won_update_hat_dict(did_ai_win, good_guesses, hat_dict):
    if did_ai_win == True:
        for key, value in good_guesses.items():
            hat_dict[key].append(value)
        return hat_dict



# def update_ai_hat_dict(good_guesses, hat_dict):
#     for sticks in good_guesses:
