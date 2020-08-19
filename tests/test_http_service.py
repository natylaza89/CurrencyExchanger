import unittest
from unittest.mock import patch
import json
import sys

sys.path.append('../')
from logic.http_service.currency_rates_api import CurrencyRatesAPI

class TestHttpService(unittest.TestCase):

    def setUp(self):
        self.api_session1 = CurrencyRatesAPI()
        self.api_session2 = CurrencyRatesAPI()


    def test_if_object_is_singelton_and_subclass(self):
        # Checks if it's a sub class of IFileHandler
        self.assertIsInstance(self.api_session1, CurrencyRatesAPI)
        self.assertIsInstance(self.api_session2, CurrencyRatesAPI)

        # Checks if the singelton pattern works - same addresses in memory.
        self.assertEqual(id(self.api_session1), id(self.api_session2))

    def test_current_rate(self):
        self.assertIsNone(self.api_session1.current_rate)

        #Mocked Data
        self.api_session1.data = {"rates":{"EUR":0.84623847},"base":"USD","date":"2020-08-07"}
        self.api_session1.target_currency = [key for key in self.api_session1.data["rates"].keys()][0]
        current_rate = self.api_session1.current_rate

        self.assertEqual(current_rate, 0.84623847)


    def test_get_request(self):
        with patch('logic.http_service.currency_rates_api.requests.get') as mocked_get:
            # Check a successfull http get request
            mocked_get.return_value.ok = True
            mocked_get.return_value.content = b'{"rates":{"EUR":0.84623847},"base":"USD","date":"2020-08-07"}'
            data = json.loads( mocked_get.return_value.content)
            self.api_session1.base_currency = data["base"]
            self.api_session1.target_currency = data["rates"].popitem()[0]

            response = self.api_session1.get_request()
            mocked_get.assert_called_with('https://api.exchangeratesapi.io/latest?base=USD&symbols=EUR')
            self.assertEqual(response, 'Success')

            # Check a failure http get request
            mocked_get.return_value.ok = False
            mocked_get.return_value.status_code = 404

            self.api_session2.target_currency = "EURO"
            response = self.api_session2.get_request()
            mocked_get.assert_called_with('https://api.exchangeratesapi.io/latest?base=USD&symbols=EURO')
            self.assertEqual(response, 'Failure')

    def test_post_request(self):
        pass

if __name__ == '__main__':
    unittest.main()
