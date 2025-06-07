from PySide6.QtCore import QThread, Signal
import requests

from datasong import Data


class DataWorker(QThread):
    data_fetched = Signal(dict)
    time_data_fetched = Signal(dict)


    def run(self):
        try:
            data_obj = Data()

            time_data = data_obj.get_time()
            self.time_data_fetched.emit(time_data)

            song_data = data_obj.SongData()
            self.data_fetched.emit(song_data)



        except Exception as e:
            print(f"Error fetching data: {e}")
            self.data_fetched.emit({})
            self.time_data_fetched.emit({})

