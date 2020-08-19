from threading import Lock
from typing import Generator

from logic.file_handler.ifile_handler import IFileHandler


class TextFileHandler(IFileHandler):
    """
    Singelton Class For using Parsing a Text File
    """
    __instance = None

    def __init__(self, file_path : str, *args, **kwargs) -> None:
        """ Initialization of the Class """
        self._file_path = file_path
    
    def __new__(cls, file_path : str, *args, **kwargs) -> 'TextFileHandler':
        """ Constructor's Double Check Lock for Handling a Singelton Instance """
        if not cls.__instance: 
            with Lock(): 
                if not cls.__instance: 
                    cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance 

    def __repr__(self) -> str:
        """ Representaion the the Class """
        return f"TextFileHandler({self._file_path})"

    @property
    def base_currency(self) -> str:
        return self._base_currency

    @property
    def target_currency(self) -> str:
        return self._target_currency

    @property
    def file_path(self) -> str:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path : str) -> None:
        self._file_path = file_path

    def parse_file_headers(self) -> None:
        """ Parsing text file's Headers - getting Base & Target Currency """
        try:
             with open(self._file_path, "r") as data_file:
                self._base_currency = str.strip(next(data_file), ' \n')
                self._target_currency = str.strip(next(data_file), ' \n')

        except FileNotFoundError as fnfe:
            print("Error Has Occured: File Not Found, Please try again.")
            raise
            # Logger Option with the error message
        except Exception as e:
            print("Error Has Occured, Please try again.")
            # Logger Option with the error message

    def parse_file_data(self) -> Generator[str, None, None] :
        """ Parsing text file in order to gets the value for converting """
        try:
            with open(self._file_path, "r") as data_file:
                next(data_file)
                next(data_file)
                yield from data_file

        except FileNotFoundError as fnfe:
            print("Error Has Occured: File Not Found, Please try again.")
            raise
            # Logger Option with the error message
        except Exception as e:
            print("Error Has Occured, Please try again.")
            # Logger Option with the error message