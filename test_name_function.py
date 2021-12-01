import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    #Tests for name_function.py

    def test_first_last_name(self):
        #Do names like Jimi Hendrix work?
        formatted_name = get_formatted_name('jimi','hendrix')
        self.assertEqual(formatted_name, 'Jimi Hendrix')  # testing to see if formatted_name = Jimi Hendrix

    def first_last_middle(self):
        #Do names like Timmy Cartman Clyde work?
        formatted_name = get_formatted_name('timmy', 'clyde','cartman')
        self.assetEqual(formatted_name, 'Timmy Cartman Clyde')

unittest.main()
