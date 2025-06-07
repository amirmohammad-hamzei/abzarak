from PySide6.QtCore import QThread, Signal
import requests

from datasong import Data


class DataWorker_Weather(QThread):
    weather_data_fetched = Signal(dict)

    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        try:
            data_obj = Data()

            weather_data = data_obj.weather(self.city)
            self.weather_data_fetched.emit(weather_data)



        except Exception as e:
            print(f"Error fetching data: {e}")
            self.weather_data_fetched.emit({})

