""" Unit test for jumble word module """

import unittest

import jumble_word


class JumbleWordTest(unittest.TestCase):
    """ Define unit-test cases """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_happy_case(self):
        """ Test to check if the output is correct """
        expected = ['do', 'dog', 'gd', 'go', 'god', 'od']
        actual = jumble_word.run("dog")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
