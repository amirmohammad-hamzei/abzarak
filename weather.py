from datetime import datetime, timedelta

from PySide6.QtCore import QSettings

from worker_weather import DataWorker_Weather


class Weather():
    def __init__(self, ui):
        self.ui = ui

        self.settings = QSettings("MyApp", "Weather")
        saved_city = self.settings.value("city", "tehran", str)


        self.time = datetime.now()
        time_1 = self.time + timedelta(days=2)
        self.ui.lbl_1.setText(time_1.strftime("%a"))
        time_2 = self.time + timedelta(days=3)
        self.ui.lbl_2.setText(time_2.strftime("%a"))

        self.ui.go.clicked.connect(self.city_search)

        self.city_weather(saved_city)

    def update_weather(self, data):
        if data:
            self.ui.weather_text.setText(data["text"])
            self.ui.weather_name.setText(data["name"])
            self.ui.weather_temp.setText(data["temp_c"] + "℃")
            self.ui.weather_region.setText(data["region"])
            self.ui.weather_icon.setStyleSheet(f"image: url({data["icon"]});")

            self.ui.tomorrow_icon.setStyleSheet(f"image: url({data["day_0_condition_icon"]});")
            self.ui.tomorrow_forecast.setText(data["day_0_condition_text"])
            self.ui.tomorrow_temp.setText(data["day_0_maxtemp_c"] + "°C")

            self.ui.icon_1.setStyleSheet(f"image: url({data["day_1_condition_icon"]});")
            self.ui.forecast_1.setText(data["day_1_condition_text"])
            self.ui.temp_1.setText(data["day_1_maxtemp_c"] + "°C")

            self.ui.icon_2.setStyleSheet(f"image: url({data["day_2_condition_icon"]});")
            self.ui.forecast_2.setText(data["day_2_condition_text"])
            self.ui.temp_2.setText(data["day_2_maxtemp_c"] + "°C")

        else:
            print("Error fetching weather data.")

    def city_weather(self, city):
        if city != "":
            self.settings.setValue("city", city)
            self.worker = DataWorker_Weather(city)
            self.worker.weather_data_fetched.connect(self.update_weather)
            self.worker.start()
        else:
            print("empty")

    def city_search(self):
        self.search = self.ui.search.text()
        self.city_weather(self.search)
        self.ui.search.setText("")
