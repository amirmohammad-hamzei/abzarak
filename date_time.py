import sys
from datetime import datetime, timedelta

from PySide6.QtCore import QTimer
from worker import DataWorker


class DateTime:
    def __init__(self, ui):
        self.ui = ui
        self.current_time = None

        # تنظیم تایمر برای به‌روز رسانی هر ثانیه
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time_locally)
        self.timer.start(1000)

        self.worker = DataWorker()
        self.worker.time_data_fetched.connect(self.update_time)
        self.worker.start()

    def update_time(self, time_data):
        if time_data and "timestamp" in time_data:
            self.current_time = datetime.fromtimestamp(int(time_data["timestamp"]))
            self.ui.time.setText(self.current_time.strftime("%H:%M:%S"))
            self.ui.date.setText(time_data["date"])
            self.ui.day.setText(time_data["weekdays"])
            self.ui.events.setText(time_data["day"])
        else:
            self.current_time = datetime.now()
            self.ui.time.setText(self.current_time.strftime("%H:%M:%S"))
            self.ui.date.setText(self.current_time.strftime("%Y-%m-%d"))
            self.ui.day.setText(self.current_time.strftime("%A"))

    def update_time_locally(self):
        if self.current_time:
            self.current_time += timedelta(seconds=1)
            self.ui.time.setText(self.current_time.strftime("%H:%M:%S"))
