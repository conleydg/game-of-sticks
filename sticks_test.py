import unittest

from sticks import *

class TestGame(unittest.TestCase):

    def test_user_name_two(self):
        self.assertEqual(user_name_two(2), 'AI BOT')


    def test_which_users_turn(self):
        self.assertEqual(which_users_turn(1, 'user_one', 'user_two'), 'user_one')
        self.assertEqual(which_users_turn(2, 'user_one', 'user_two'), 'user_two')
        self.assertEqual(which_users_turn(5, 'user_one', 'user_two'), 'user_one')
        self.assertEqual(which_users_turn(200, 'user_one', 'user_two'), 'user_two')
        self.assertNotEqual(which_users_turn(5, 'user_one', 'user_two'), 'user_two')
        self.assertNotEqual(which_users_turn(200, 'user_one', 'user_two'), 'user_one')





if __name__ == '__main__':
    unittest.main()
