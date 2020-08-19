import unittest
import random
from itertools import tee
import sys

sys.path.append('../')
from logic.file_handler.ifile_handler import IFileHandler
from logic.file_handler.text_file_handler import TextFileHandler

class TestTextFileHandler(unittest.TestCase):

    def setUp(self):
        self.text_file_handler1 = TextFileHandler('../files/test_money.txt')
        self.text_file_handler2 = TextFileHandler('../files/test_money.txt')

    def test_if_object_is_singelton_and_subclass(self):
        # Checks if it's a sub class of IFileHandler
        self.assertIsInstance(self.text_file_handler1, IFileHandler)
        self.assertIsInstance(self.text_file_handler2, IFileHandler)

        # Checks if the singelton pattern works - same addresses in memory.
        self.assertEqual(id(self.text_file_handler1), id(self.text_file_handler2))


    def test_file_parsing_and_file_path_as_expected(self):
        # Checks if file path's initializtion works
        self.assertEqual(self.text_file_handler1.file_path, '../files/test_money.txt')
        
        #Injecting Mocked Data into a test text file
        random.seed(0)
        mocked_data_iter1, mocked_data_iter2 = tee(round(random.uniform(0, 15), random.randint(0, 10)) for _ in range(10))
        
        with open(self.text_file_handler1.file_path, 'w') as text_file:
            text_file.write('EUR\n') 
            text_file.write('USD\n')

            for number in mocked_data_iter1:
                text_file.write(f"{number}\n")

        #Checks if file's header parsed correctly
        self.text_file_handler1.parse_file_headers()
        self.assertEqual(self.text_file_handler1.base_currency, 'EUR')
        self.assertEqual(self.text_file_handler1.target_currency, 'USD')

        # Checking Equality of data
        for num in self.text_file_handler1.parse_file_data():
            self.assertEqual(str.strip(num, ' \n'), str(next(mocked_data_iter2)))

        # Check 2nd Object with wrong path
        self.text_file_handler2.file_path = '../files/test_rates.txt'
        self.assertEqual(self.text_file_handler2.file_path, '../files/test_rates.txt')
        
        # Checks if exception raises correctly
        with self.assertRaises(FileNotFoundError):
            self.text_file_handler2.parse_file_headers()           

if __name__ == '__main__':
    unittest.main()