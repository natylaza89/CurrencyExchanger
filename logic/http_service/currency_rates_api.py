import requests
from requests.exceptions import Timeout, TooManyRedirects, HTTPError, ConnectionError
import json
from threading import Lock

from logic.http_service.ihttp_service import IHTTPService


class CurrencyRatesAPI(IHTTPService):
    """
    Singelton Class For using Currency Rate's API
    """
    __instance = None

    def __init__(self) -> None:
        """ Initialization of the Class """
        self._base_currency = None
        self._target_currency = None
        self._current_rate = None
        self._data = None
        self._request_status = None

    def __repr__(self) -> str:
        """ Representaion the the Class """
        return f"CurrencyRatesAPI()"
    
    def __new__(cls, *args, **kwargs) -> 'CurrencyRatesAPI':
        """ Constructor's Double Check Lock for Handling a Singelton Instance """
        if not cls.__instance: 
            with Lock(): 
                if not cls.__instance: 
                    cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance 

    @property
    def base_currency(self) -> str:
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency : str) -> None:
        self._base_currency = base_currency

    @property
    def target_currency(self) -> str:
        return self._target_currency

    @target_currency.setter
    def target_currency(self, target_currency : str) -> None:
        self._target_currency = target_currency

    @property
    def current_rate(self) -> float:
        """ Capture Current Rate if data exists and current rate is empty """
        try:
            self._current_rate = self._data["rates"][self._target_currency]
        except KeyError as kerr:
            print("Error Has Occured: ", kerr)
            self._current_rate = 0
        finally:
            return self._current_rate  
    
    @property
    def url_query(self) -> str:
        return self._url_query

    @url_query.setter
    def url_query(self, url_query : str) -> None:
        self._url_query = url_query

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, data : dict) -> None:
        self._data = data

    @property
    def request_status(self) -> str:
        return self._request_status

    def get_request(self) -> str:
        """ Exchangeratesapi's API Session for Fetting Currency Rate """
        self._url_query = f"https://api.exchangeratesapi.io/latest?base={self._base_currency}&symbols={self._target_currency}"

        try:
            self._api_response = requests.get(self._url_query)
            if self._api_response.ok:
                self._data = json.loads(self._api_response.content)
                self._request_status = 'Success'
            else:
                self._request_status = 'Failure'
                self._api_response.raise_for_status()
        except (Timeout, TooManyRedirects, HTTPError, ConnectionError) as error:
            self._request_status = 'Failure'
            print("Error Has Occured:", error)
            #Logging..
        finally:
            return self._request_status

    def post_request(self) -> Exception:
        raise NotImplementedError