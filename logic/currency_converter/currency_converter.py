from threading import Lock
from typing import Generator

from logic.file_handler.text_file_handler import TextFileHandler
from logic.http_service.currency_rates_api import CurrencyRatesAPI


class CurrencyConverter:
    """
    Singelton Class of Curreny Convereter Componenet which implement the Dependency Injection principle
    Dependency Injection:
    1. TextFileHandler
    2. CurrencyRatesAPI
    """
    
    __instance = None
    
    def __init__(self, file_handler : TextFileHandler, api_session : CurrencyRatesAPI) -> None:
        """ Initialization of the Class """
        self._file_handler = file_handler
        self._file_handler.parse_file_headers()
        self._api_session = api_session
        self._api_session.base_currency = self._file_handler.base_currency
        self._api_session.target_currency = self._file_handler.target_currency
        self._api_session.request = self._api_session.get_request()
        self._current_rate = self._api_session.current_rate
    
    def __new__(cls, file_handler : TextFileHandler, api_session : CurrencyRatesAPI, *args, **kwargs) -> 'CurrencyConverter':
        """ Constructor's Double Check Lock for Handling a Singelton Instance """
        if not cls.__instance: 
            with Lock(): 
                if not cls.__instance: 
                    cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance 

    def __repr__(self) -> str:
        """ Representaion the the Class """
        return f"CurrencyConverter({self._file_handler}, {self._api_session})"

    @property
    def current_rate(self) -> float:
        return self._current_rate

    @current_rate.setter
    def current_rate(self, current_rate : float) -> None:
        self._current_rate = current_rate

    def _parse_number(self, string_number : str) -> float:
        """ Parse/Convert numbers from string to int/float """
        clean_string_number = str.strip(string_number, ' \n')      
        return float(clean_string_number)

    def convert_currency(self) -> Generator[float, None, None]:
        """ Convert To Target Currency's Value """
        for number in self._file_handler.parse_file_data():
            current_number = self._parse_number(number)
            yield ( current_number * self._current_rate )
