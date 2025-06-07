# music_player.py
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QSettings, QTimer, QTime
from PySide6.QtWidgets import QProgressBar

from worker import DataWorker


class MusicPlayer:
    def __init__(self, ui):
        self.ui = ui
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # تنظیمات صدا
        self.settings = QSettings("MyApp", "MusicPlayer")
        saved_volume = self.settings.value("volume", 50, int)
        self.ui.vol_slider.setValue(saved_volume)
        self.ui.vol_slider.valueChanged.connect(self.set_volume)
        self.set_volume(saved_volume)

        # تایمر برای آپدیت پروگرس بار
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.duration = 0
        self.position = 0

        self.worker = DataWorker()
        self.worker.data_fetched.connect(self.on_song_time_fetched)



    def set_volume(self, value):
        self.audio_output.setVolume(value / 100.0)
        self.settings.setValue("volume", value)

    def play_song(self, url):
        self.player.setSource(QUrl(url))
        self.player.play()
        self.timer.start(1000)  # آپدیت هر ثانیه

    def stop_song(self):
        self.player.stop()
        # self.ui.progressBar.setValue(0)
        self.timer.stop()

    def update_progress_time(self, data):
        self.duration = data.get("duration", 0) + 40
        self.position = data.get("elapsed", 0)

    def update_progress(self):
        if self.duration > 0:
            self.position += 1
            if self.position >= self.duration:
                self.worker.start()
            # محاسبه زمان به دقیقه و ثانیه
            '''time_current = QTime(0, 0).addSecs(self.position)
            time_total = QTime(0, 0).addSecs(self.duration)

            # نمایش زمان به فرمت mm:ss
            self.ui.progressBar.setFormat(f"{time_current.toString('mm:ss')} / {time_total.toString('mm:ss')}")

            # تنظیم مقدار پروگرس بار
            progress = (self.position / self.duration) * 100
            self.ui.progressBar.setValue(progress)
            self.position += 1
            if self.position >= self.duration:
                self.stop_song()
        else:
            self.ui.progressBar.setFormat("00:00 / 00:00")
            self.ui.progressBar.setValue(0)'''


    def on_song_data_fetched(self, song_data):
        if song_data:
            self.update_progress_time(song_data)
            self.update_ui_with_song_data(song_data)
            self.play_song("https://radio.beeptunes.com/listen/pop/radio.mp3")
        else:
            print("Error: Could not fetch song data.")

    def on_song_time_fetched(self, song_data):
        if song_data:
            self.update_progress_time(song_data)
            self.update_ui_with_song_data(song_data)
        else:
            print("Error: Could not fetch song data.")

    def update_ui_with_song_data(self, song_data):
        self.ui.image_widget.setStyleSheet(
            f"#image_widget{{border-radius:25px; border:2px solid #000; "
            f"background-repeat: repeat; border-image: url({song_data['art']});}}"
        )
        self.ui.text.setText(song_data['text'])
        self.ui.artist.setText(song_data['artist'])
        self.ui.title.setText(song_data['title'])