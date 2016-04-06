import unittest

from sticks import *

class TestGame(unittest.TestCase):

    def test_user_name_two(self):
        self.assertEqual(user_two_name(2), 'A.I. BOT')


    def test_which_users_turn(self):
        self.assertEqual(which_users_turn(1, 'user_one', 'user_two'), 'user_one')
        self.assertEqual(which_users_turn(2, 'user_one', 'user_two'), 'user_two')
        self.assertEqual(which_users_turn(5, 'user_one', 'user_two'), 'user_one')
        self.assertEqual(which_users_turn(200, 'user_one', 'user_two'), 'user_two')
        self.assertNotEqual(which_users_turn(5, 'user_one', 'user_two'), 'user_two')
        self.assertNotEqual(which_users_turn(200, 'user_one', 'user_two'), 'user_one')

    def test_which_game_choice(self):
        self.assertEqual(which_game(1), 1)
        self.assertEqual(which_game(2), 2)
        self.assertEqual(which_game(3), print('Skynet Initializing...'))
        self.assertNotEqual(which_game(1), 2)

    def test_is_game_over(self):
        self.assertTrue(is_game_over(-5))
        self.assertFalse(is_game_over(5))

    def test_did_ai_win(self):
        self.assertTrue(did_ai_win_or_lose('abcd', True))
        self.assertFalse(did_ai_win_or_lose('abcd', False))
        self.assertFalse(did_ai_win_or_lose('A.I. Bot', False))





if __name__ == '__main__':
    unittest.main()
