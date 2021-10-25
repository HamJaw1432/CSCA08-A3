"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_02_one_person_more_than_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', 
                                   'Rock N Rollers']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg) 
    
    def test_03_more_than_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association'],
                 'Joey Gladstone': ['Comics R Us']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)    
        
    def test_04_more_than_one_person_different_num_of_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', 
                                   'Rock N Rollers'],
                 'Joey Gladstone': ['Comics R Us']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
    
    def test_05_more_than_one_person_more_than_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', 
                                   'Rock N Rollers'],
                 'Joey Gladstone': ['Comics R Us', 'CS Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)         


if __name__ == '__main__':
    unittest.main(exit=False)
