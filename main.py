# main.py
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup, QGraphicsBlurEffect
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve

from ui_main_window import Ui_MainWindow
from weather import Weather
from worker import DataWorker
from music_player import MusicPlayer
from date_time import DateTime


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # تنظیمات اولیه رابط کاربری
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.minimizebtn.clicked.connect(self.showMinimized)
        self.ui.closebtn.clicked.connect(self.close)
        self.ui.menubtn.clicked.connect(self.slideLeftMenu)

        # مدیریت صفحات
        self.ui.stackedWidget.setCurrentWidget(self.ui.home_page)
        self.ui.home_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        self.ui.music_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.music_page))
        self.ui.gpt_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.chatgpt_page))

        # تنظیمات حرکت پنجره
        self.ui.tittle_bar.mouseMoveEvent = self.moveWindow
        self.ui.tittle_bar.mousePressEvent = self.mousePressEvent

        # تنظیم گروه دکمه‌ها
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)
        self.button_group.addButton(self.ui.home_btn)
        self.button_group.addButton(self.ui.music_btn)
        self.button_group.addButton(self.ui.gpt_btn)
        self.ui.home_btn.setChecked(True)
        self.button_group.buttonClicked.connect(self.on_button_clicked)

        # تنظیمات تاریخ و ساعت
        self.date_time = DateTime(self.ui)

        # تنظیمات آب و هوا
        self.weather = Weather(self.ui)

        # تنظیمات موزیک پلیر
        self.music_player = MusicPlayer(self.ui)
        self.ui.play_stop_btn.clicked.connect(self.toggle_music)

        # تنظیمات Worker
        self.worker = DataWorker()
        self.worker.data_fetched.connect(self.music_player.on_song_data_fetched)

    def toggle_music(self):
        if self.ui.play_stop_btn.isChecked():
            self.worker.start()
        else:
            self.music_player.stop_song()

    def slideLeftMenu(self):
        width = self.ui.left_side_menu.width()
        new_width = 125 if width == 50 else 50
        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.OutBack)
        self.animation.start()

    def on_button_clicked(self, button):
        button.setChecked(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPosition = event.globalPosition().toPoint()

    def moveWindow(self, event):
        if not self.isMaximized() and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
            self.clickPosition = event.globalPosition().toPoint()
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
