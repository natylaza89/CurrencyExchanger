from logic.currency_converter.currency_converter import CurrencyConverter
from logic.file_handler.text_file_handler import TextFileHandler
from logic.http_service.currency_rates_api import CurrencyRatesAPI


class App:
    def __init__(self, file_path : str) -> None:
        """ Initialization of the Class """
        self._file_path = file_path

    def __repr__(self) -> str:
        """ Representaion the the Class """
        return f"App({self._file_path})"

    def _format_text(self, converted_number : float) -> str: 
        """ Format the text before printing """
        formated_number = str(converted_number).split('.')[1]

        if len(formated_number) < 2:
            if formated_number != '0':
                formated_number = f"{converted_number:.1f}"
            else:
                formated_number = f"{converted_number:.0f}"
        else:
            formated_number = f"{converted_number:.2f}"

        return formated_number

    def start_app(self) -> None:
        """ Initializing Components: File Handler & Http Service to be injected
            into Currency Converter as part of Dependency Injection.
        """
        file_handler = TextFileHandler(self._file_path)
        api_session = CurrencyRatesAPI()
        currency_converter = CurrencyConverter(file_handler, api_session)

        #Print the convereted values to the screen
        for converted_value in currency_converter.convert_currency():
            formated_number = self._format_text(converted_value)
            print(formated_number)
