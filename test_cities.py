import unittest
from city_functions import city_description

class MyTestCase(unittest.TestCase):
    #Testing if inputs like 'santiago','chile' work
    def test_city_country(self):
        city_country_formatted = city_description('santiago','chile')
        self.assertEqual(city_country_formatted, "Santiago, Chile")  # add assertion here

    def test_city_country_population(self):
        city_country_population = city_description('santiago','chile',5000000)
        self.assertEqual(city_country_population,"Santiago, Chile - Population 5000000")
if __name__ == '__main__':
    unittest.main()
