import unittest
import sys

sys.path.append('../')
from logic.file_handler.text_file_handler import TextFileHandler
from logic.http_service.currency_rates_api import CurrencyRatesAPI
from logic.currency_converter.currency_converter import CurrencyConverter


class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        api_session = CurrencyRatesAPI()
        text_file_handler = TextFileHandler('../files/test_money.txt')
        self.currency_converter_handler1 = CurrencyConverter(text_file_handler, api_session)
        self.currency_converter_handler2 = CurrencyConverter(text_file_handler, api_session)

    def test_if_object_is_singelton(self):
        # Checks if the singelton pattern works - same addresses in memory.
        self.assertEqual(id(self.currency_converter_handler1), id(self.currency_converter_handler2))
    
    def test_convert_currency_operation_output_as_expected(self):
        
        mocked_data = iter([10.722363497661654, 0.5140655802842818, 6.17023618037572, 12.289003639851598,
                            7.407940404514799, 6.408448319540439, 1.77770253108, 7.851942774777399,
                            12.536094150302041, 12.4792873450884])
        self.currency_converter_handler1.current_rate = 0.8465250148
        calculated_values = self.currency_converter_handler1.convert_currency()

        for value in calculated_values:
            self.assertEqual(value, next(mocked_data))


if __name__ == '__main__':
    unittest.main()