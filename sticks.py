import sys
import random
from sticks_ai import *
import pickle
import os

def print_game_options():
    print('\nWelcome to the Game of Sticks!')
    print('\n    Game Options:'
    '\n \nPlay against a friend (1)'
    '\nPlay against the computer (2)'
    '\nComputer plays against the computer (3)')


def which_game_user_input():
    while True:
        game_choice = input('Which option do you take (1, 2, or 3)?')
        try:
            game_choice = int(game_choice)
            which_game(game_choice)
            return game_choice
        except:
            print('Please enter 1, 2, or 3')

def which_game(game_choice):
    if game_choice == 1:
        return 1
    elif game_choice == 2:
        return 2
    elif game_choice == 3:
        print('Skynet Initializing...')
    else:
        print('Please enter 1, 2, or 3')


def fetch_ai_data():
    with open('hat_dict_pickle.pickle', 'rb') as handle:
      hat_dict = pickle.load(handle)
    return hat_dict

def push_ai_data(hat_dict):
    with open('hat_dict_pickle.pickle', 'wb') as output:
      pickle.dump(hat_dict, output, -1)

def initial_number_of_sticks():
    while True:
        user_input_num_of_sticks = input('How many sticks are there on the table initially (10-100)?')
        try:
            user_input_num_of_sticks = int(user_input_num_of_sticks)
            if 10 <= user_input_num_of_sticks <= 100:
                return user_input_num_of_sticks
            else:
                print('Please enter a number between 10 and 100')
        except:
            print('Please enter a number between 10 and 100')


# def create_list_ten_to_num_of_sticks(number_of_start_sticks):
#     return list(range(10,number_of_start_sticks))

def user_one_name(game_choice):
    return input('Please enter player 1\'s name: ')



def user_two_name(game_choice):
    if game_choice == 1:
        user_two_name = input('Please enter player 2\'s name: ')
        return user_two_name
    elif game_choice == 2:
        user_two_name = 'A.I. BOT'
        return user_two_name
    # elif game_choice == 3:
    #     break


def number_of_sticks_to_remove(player, number_of_sticks, hat_dict, good_guesses):
    if player == 'A.I. BOT':
        this_turns_guess = ai_bot_turn(number_of_sticks, hat_dict)
        good_guesses[number_of_sticks] = this_turns_guess
        print('A.I. Bot removed {} sticks'.format(this_turns_guess))
        return number_of_sticks - this_turns_guess
    while True:
        try:
            number_to_remove = int(input('{}: How many sticks do you take (1-3)?'.format(player)))
            if 1 <= number_to_remove <=3:
                number_of_sticks = number_of_sticks - number_to_remove
                return number_of_sticks
            else:
                print('Please enter 1, 2, or 3')
        except:
            print('Please enter 1, 2, or 3')

def which_users_turn(count_of_turns, user_one, user_two):
    if count_of_turns % 2 == 1:
        return user_one
    elif count_of_turns % 2 == 0:
        return user_two

def is_game_over(number_of_sticks):
    if number_of_sticks <= 0:
        return True


def play_again():
    return input('Would you like to play again? Y/N: ')









def main():
    good_guesses = {}
    count_of_turns = 1

    print_game_options()

    game_choice = which_game_user_input()

    user_one = user_one_name(game_choice)

    user_two = user_two_name(game_choice)

    number_of_sticks = initial_number_of_sticks()

    hat_dict = fetch_ai_data()


    while number_of_sticks > 0:

        os.system('clear')

        print('good_gueeses - {}'.format(good_guesses))

        print(hat_dict)


        print('\nThere are {} sticks on the table\n'.format(number_of_sticks))

        player = which_users_turn(count_of_turns, user_one, user_two)

        number_of_sticks = number_of_sticks_to_remove(player, number_of_sticks, hat_dict, good_guesses)

        game_over = is_game_over(number_of_sticks)

        did_ai_win = did_ai_win_or_lose(player, game_over)

        if_ai_won_update_hat_dict(did_ai_win, good_guesses, hat_dict)

        count_of_turns += 1

        push_ai_data(hat_dict)

        if game_over:
            if play_again() == 'y':
                main()
            break

















if __name__ == "__main__":
    main()
