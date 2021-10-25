"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_02_one_person_one_friend_different_last(self):
        param = {'Clare Dunphy': ['Phil McQuid']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'McQuid': ['Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_03_one_person_multi_friend_different_last(self):
        param = {'Clare Dunphy': ['Phil McQuid', 'Bob Marley']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'McQuid': ['Phil'], 'Marley': ['Bob']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
    
    def test_04_one_person_mutli_friend_different_last_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil McQuid', 'Bob McQuid']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'McQuid': ['Bob', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_05_one_person_mutli_friend_same_last_with_one_friend(self):
        param = {'Clare Dunphy': ['Phil Dunphy', 'Bob McQuid']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil'], 'McQuid': ['Bob']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)     
    
    def test_06_multi_person_one_friend_different_last(self):
        param = {'Clare Dunphy': ['Phil McQuid'], 
                 'Bob Marley': ['G W Bush']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'McQuid': ['Phil'], 
                    'Marley': ['Bob'], 'Bush':['G W']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
    
    def test_07_multi_person_multi_friend_different_last(self):
        param = {'Clare Dunphy': ['Phil McQuid', 'Bob Marley'], 
                 'Bob Marley': ['G W Bush', 'Phil McQuid']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'McQuid': ['Phil'], 
                    'Marley': ['Bob'], 'Bush':['G W']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_08_multi_person_multi_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy', 'Bob Dunphy'], 
                 'Bob Dunphy': ['G W Dunphy', 'Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Bob', 'Clare', 'G W', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_09_multi_person_multi_friend_same_and_different_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy', 'Bob Marley'], 
                 'Bob Marley': ['G W Dunphy', 'Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'G W', 'Phil'], 'Marley': ['Bob']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)     


if __name__ == '__main__':
    unittest.main(exit=False)
