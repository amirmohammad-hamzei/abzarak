# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowBsIbDZ.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMaximumSize(QSize(1000, 700))
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 40))
        self.main_header.setStyleSheet(u"")
        self.main_header.setFrameShape(QFrame.Shape.NoFrame)
        self.main_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tittle_bar_container = QFrame(self.main_header)
        self.tittle_bar_container.setObjectName(u"tittle_bar_container")
        self.tittle_bar_container.setStyleSheet(u"border-bottom:1px solid #000;\n"
"border-right:none;\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"")
        self.tittle_bar_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet(u"QFrame{\n"
"border-bottom:1px solid #000;\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.left_menu_toggle.setFrameShape(QFrame.Shape.NoFrame)
        self.left_menu_toggle.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menubtn = QPushButton(self.left_menu_toggle)
        self.menubtn.setObjectName(u"menubtn")
        self.menubtn.setMinimumSize(QSize(0, 0))
        self.menubtn.setStyleSheet(u"QFrame{\n"
"background-color: #000;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:5px 10px ;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color:#fff;\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"background-color: #6b75ff;\n"
"border: none;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/feather/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menubtn.setIcon(icon)
        self.menubtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.menubtn)


        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.tittle_bar = QFrame(self.tittle_bar_container)
        self.tittle_bar.setObjectName(u"tittle_bar")
        self.tittle_bar.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.tittle_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.tittle_bar.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.tittle_bar)


        self.horizontalLayout_2.addWidget(self.tittle_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMinimumSize(QSize(0, 0))
        self.top_right_btns.setMaximumSize(QSize(100, 16777215))
        self.top_right_btns.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"border-bottom:2px solid #000;\n"
"border-left:none;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover{\n"
"background-color: #6b75ff;\n"
"border: none;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        self.top_right_btns.setFrameShape(QFrame.Shape.NoFrame)
        self.top_right_btns.setFrameShadow(QFrame.Shadow.Plain)
        self.top_right_btns.setLineWidth(1)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizebtn = QPushButton(self.top_right_btns)
        self.minimizebtn.setObjectName(u"minimizebtn")
        self.minimizebtn.setMinimumSize(QSize(0, 0))
        self.minimizebtn.setMaximumSize(QSize(30, 30))
        self.minimizebtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/feather/window_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizebtn.setIcon(icon1)
        self.minimizebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizebtn)

        self.closebtn = QPushButton(self.top_right_btns)
        self.closebtn.setObjectName(u"closebtn")
        self.closebtn.setMaximumSize(QSize(30, 30))
        self.closebtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/feather/window_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closebtn.setIcon(icon2)
        self.closebtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closebtn)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.Shape.NoFrame)
        self.main_body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        self.left_side_menu.setMinimumSize(QSize(0, 0))
        self.left_side_menu.setMaximumSize(QSize(50, 16777215))
        self.left_side_menu.setSizeIncrement(QSize(0, 0))
        self.left_side_menu.setStyleSheet(u"QFrame{\n"
"background-color: #000;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:20px 10px ;\n"
"border:none;\n"
"border-radius:10px;\n"
"background-color: #000;\n"
"color:#fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #4CAF50; \n"
"    border-radius:5px;\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover{\n"
"background-color: #6b75ff;\n"
"border: none;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"")
        self.left_side_menu.setFrameShape(QFrame.Shape.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_btn = QFrame(self.left_side_menu)
        self.left_menu_top_btn.setObjectName(u"left_menu_top_btn")
        self.left_menu_top_btn.setStyleSheet(u"QFrame{\n"
"    border:none;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.left_menu_top_btn.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_menu_top_btn.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.left_menu_top_btn)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.left_menu_top_btn)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(125, 0))
        self.home_btn.setStyleSheet(u"padding-right:22px;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/material_design/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_btn.setIcon(icon3)
        self.home_btn.setIconSize(QSize(30, 30))
        self.home_btn.setCheckable(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.home_btn)

        self.music_btn = QPushButton(self.left_menu_top_btn)
        self.music_btn.setObjectName(u"music_btn")
        self.music_btn.setMinimumSize(QSize(125, 0))
        self.music_btn.setStyleSheet(u"padding-right:25px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/font_awesome/solid/music.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.music_btn.setIcon(icon4)
        self.music_btn.setIconSize(QSize(30, 30))
        self.music_btn.setCheckable(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.music_btn)

        self.gpt_btn = QPushButton(self.left_menu_top_btn)
        self.gpt_btn.setObjectName(u"gpt_btn")
        self.gpt_btn.setMinimumSize(QSize(125, 0))
        self.gpt_btn.setStyleSheet(u"padding-left:10px;")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/font_awesome/solid/robot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.gpt_btn.setIcon(icon5)
        self.gpt_btn.setIconSize(QSize(30, 30))
        self.gpt_btn.setCheckable(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.gpt_btn)


        self.verticalLayout_2.addWidget(self.left_menu_top_btn)


        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setMinimumSize(QSize(0, 0))
        self.center_main_items.setStyleSheet(u"background-color: white;")
        self.center_main_items.setFrameShape(QFrame.Shape.NoFrame)
        self.center_main_items.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.stackedWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget.setLineWidth(1)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.home_page.sizePolicy().hasHeightForWidth())
        self.home_page.setSizePolicy(sizePolicy1)
        self.home_page.setStyleSheet(u"background-color: rgb(69, 78, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.home_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.home_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(938, 299))
        self.frame_7.setStyleSheet(u"background-color: rgb(69, 78, 255);")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridFrame = QFrame(self.frame_9)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.gridFrame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.time = QLabel(self.gridFrame)
        self.time.setObjectName(u"time")
        font1 = QFont()
        font1.setPointSize(55)
        self.time.setFont(font1)
        self.time.setStyleSheet(u"margin-top:40px;")
        self.time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.time, 0, 1, 1, 2)

        self.date = QLabel(self.gridFrame)
        self.date.setObjectName(u"date")
        font2 = QFont()
        font2.setPointSize(25)
        self.date.setFont(font2)
        self.date.setStyleSheet(u"")
        self.date.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.date, 1, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.day = QLabel(self.gridFrame)
        self.day.setObjectName(u"day")
        self.day.setFont(font2)
        self.day.setStyleSheet(u"margin-left:20px;")
        self.day.setFrameShadow(QFrame.Shadow.Raised)
        self.day.setTextFormat(Qt.TextFormat.RichText)
        self.day.setScaledContents(False)
        self.day.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day.setWordWrap(False)

        self.gridLayout_3.addWidget(self.day, 1, 2, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_2 = QSpacerItem(80, 0, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 3, 2, 1)

        self.horizontalSpacer = QSpacerItem(80, 0, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 2, 1)


        self.verticalLayout_10.addWidget(self.gridFrame)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_10)
        self.verticalLayout_11.setSpacing(9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.widget_6 = QWidget(self.frame_10)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.search = QLineEdit(self.widget_6)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 25))
        self.search.setMaximumSize(QSize(300, 16777215))
        self.search.setStyleSheet(u"background-color: rgb(255, 215, 252);\n"
"border-radius:10px;\n"
"color: rgb(54, 54, 54);\n"
"padding:6px;\n"
"")

        self.horizontalLayout_12.addWidget(self.search)

        self.go = QPushButton(self.widget_6)
        self.go.setObjectName(u"go")
        self.go.setMaximumSize(QSize(65, 16777215))
        self.go.setStyleSheet(u"background-color: rgb(56, 255, 106);\n"
"padding:5px;\n"
"")

        self.horizontalLayout_12.addWidget(self.go)


        self.verticalLayout_11.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.frame_10)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"QWidget{\n"
"background-color: rgb(178, 179, 255);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QLabel{\n"
"padding:10px;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_5)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.weather_temp = QLabel(self.widget_5)
        self.weather_temp.setObjectName(u"weather_temp")
        self.weather_temp.setFont(font2)
        self.weather_temp.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.weather_temp, 1, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.weather_icon = QLabel(self.widget_5)
        self.weather_icon.setObjectName(u"weather_icon")
        self.weather_icon.setMinimumSize(QSize(70, 70))
        self.weather_icon.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.weather_icon, 0, 3, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.weather_text = QLabel(self.widget_5)
        self.weather_text.setObjectName(u"weather_text")
        font3 = QFont()
        font3.setPointSize(15)
        self.weather_text.setFont(font3)
        self.weather_text.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.weather_text, 0, 0, 1, 3)

        self.weather_name = QLabel(self.widget_5)
        self.weather_name.setObjectName(u"weather_name")
        font4 = QFont()
        font4.setPointSize(13)
        self.weather_name.setFont(font4)
        self.weather_name.setStyleSheet(u"")
        self.weather_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.weather_name, 1, 1, 1, 1)

        self.weather_region = QLabel(self.widget_5)
        self.weather_region.setObjectName(u"weather_region")
        font5 = QFont()
        font5.setPointSize(16)
        self.weather_region.setFont(font5)
        self.weather_region.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.weather_region, 1, 2, 1, 2)


        self.verticalLayout_11.addWidget(self.widget_5)

        self.events = QLabel(self.frame_10)
        self.events.setObjectName(u"events")
        self.events.setMinimumSize(QSize(0, 100))
        font6 = QFont()
        font6.setPointSize(12)
        self.events.setFont(font6)
        self.events.setStyleSheet(u"border:1px solid red;\n"
"border-radius:20px;\n"
"background-color: rgba(162, 83, 227, 50);")
        self.events.setTextFormat(Qt.TextFormat.MarkdownText)
        self.events.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.events.setMargin(10)

        self.verticalLayout_11.addWidget(self.events)


        self.horizontalLayout_10.addWidget(self.frame_10)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QWidget{\n"
"border-radius:15px;\n"
"backdrop-filter: blur(10px);\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0.485, y1:0.598818, x2:0.49, y2:0, stop:0.159341 rgba(44, 117, 255, 255), stop:0.340659 rgba(73, 136, 255, 255), stop:0.648352 rgba(119, 166, 255, 255), stop:0.82967 rgba(161, 193, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QFrame{\n"
"	background-color: transparent;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.widget_2 = QWidget(self.frame_8)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.widget_2)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font7 = QFont()
        font7.setPointSize(20)
        self.label_4.setFont(font7)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignVCenter)

        self.tomorrow_icon = QLabel(self.widget_2)
        self.tomorrow_icon.setObjectName(u"tomorrow_icon")
        self.tomorrow_icon.setMinimumSize(QSize(70, 70))
        self.tomorrow_icon.setStyleSheet(u"image: url(:/newPrefix/font_awesome/solid/sun.png);")

        self.verticalLayout_12.addWidget(self.tomorrow_icon, 0, Qt.AlignmentFlag.AlignVCenter)

        self.tomorrow_forecast = QLabel(self.widget_2)
        self.tomorrow_forecast.setObjectName(u"tomorrow_forecast")
        self.tomorrow_forecast.setMinimumSize(QSize(0, 0))
        self.tomorrow_forecast.setFont(font2)
        self.tomorrow_forecast.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.tomorrow_forecast, 0, Qt.AlignmentFlag.AlignVCenter)

        self.tomorrow_temp = QLabel(self.widget_2)
        self.tomorrow_temp.setObjectName(u"tomorrow_temp")
        self.tomorrow_temp.setFont(font7)
        self.tomorrow_temp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.tomorrow_temp, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.widget_2)

        self.widget_7 = QWidget(self.frame_8)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.widget_7)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lbl_1 = QLabel(self.widget_7)
        self.lbl_1.setObjectName(u"lbl_1")
        self.lbl_1.setFont(font7)
        self.lbl_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.lbl_1, 0, Qt.AlignmentFlag.AlignVCenter)

        self.icon_1 = QLabel(self.widget_7)
        self.icon_1.setObjectName(u"icon_1")
        self.icon_1.setMinimumSize(QSize(70, 70))
        self.icon_1.setStyleSheet(u"image: url(:/newPrefix/font_awesome/solid/sun.png);")

        self.verticalLayout_15.addWidget(self.icon_1, 0,Qt.AlignmentFlag.AlignVCenter)

        self.forecast_1 = QLabel(self.widget_7)
        self.forecast_1.setObjectName(u"forecast_1")
        self.forecast_1.setMinimumSize(QSize(0, 0))
        self.forecast_1.setFont(font2)
        self.forecast_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.forecast_1, 0, Qt.AlignmentFlag.AlignVCenter)

        self.temp_1 = QLabel(self.widget_7)
        self.temp_1.setObjectName(u"temp_1")
        self.temp_1.setFont(font7)
        self.temp_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.temp_1, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.widget_7)

        self.widget_4 = QWidget(self.frame_8)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lbl_2 = QLabel(self.widget_4)
        self.lbl_2.setObjectName(u"lbl_2")
        self.lbl_2.setFont(font7)
        self.lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.lbl_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.icon_2 = QLabel(self.widget_4)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setMinimumSize(QSize(70, 70))
        self.icon_2.setStyleSheet(u"image: url(:/newPrefix/font_awesome/solid/sun.png);")

        self.verticalLayout_14.addWidget(self.icon_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.forecast_2 = QLabel(self.widget_4)
        self.forecast_2.setObjectName(u"forecast_2")
        self.forecast_2.setMinimumSize(QSize(0, 0))
        self.forecast_2.setFont(font2)
        self.forecast_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.forecast_2, 0, Qt.AlignmentFlag.AlignVCenter)

        self.temp_2 = QLabel(self.widget_4)
        self.temp_2.setObjectName(u"temp_2")
        self.temp_2.setFont(font7)
        self.temp_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.temp_2, 0,Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_13.addWidget(self.widget_4)


        self.verticalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.home_page)
        self.music_page = QWidget()
        self.music_page.setObjectName(u"music_page")
        self.music_page.setStyleSheet(u"#music_page{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 255, 255), stop:0.0274725 rgba(166, 0, 255, 255), stop:0.989011 rgba(255, 155, 34, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.music_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.music_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 420))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0274725 rgba(166, 0, 255, 255), stop:0.989011 rgba(255, 155, 34, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: transparent;")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(80, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(300, 300))
        self.frame_5.setStyleSheet(u"border:2px solid  rgb(255, 93, 65);\n"
"border-radius:35px;\n"
"background-color: rgb(255, 93, 65);\n"
"")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_widget = QWidget(self.frame_5)
        self.image_widget.setObjectName(u"image_widget")
        self.image_widget.setMaximumSize(QSize(290, 290))
        self.image_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.image_widget.setAutoFillBackground(False)
        self.image_widget.setStyleSheet(u"#image_widget{\n"
"border-radius:35px;\n"
"border-image: url(:/newPrefix/font_awesome/solid/image.png);\n"
"\n"
"}")
        self.image_widget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout_2.addWidget(self.image_widget, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_5)


        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: transparent;")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.about_music = QFrame(self.frame_4)
        self.about_music.setObjectName(u"about_music")
        self.about_music.setMinimumSize(QSize(300, 300))
        self.about_music.setMaximumSize(QSize(300, 300))
        self.about_music.setStyleSheet(u"QFrame{\n"
"border-radius:20px;\n"
"background-color: rgba(127, 77, 113, 100);\n"
"\n"
"\n"
"}\n"
"QLabel{\n"
"padding:10px;\n"
"margin:20px;\n"
"border-bottom:1px outset #fff;\n"
"background-color: transparent;\n"
"}")
        self.about_music.setFrameShape(QFrame.Shape.NoFrame)
        self.about_music.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.about_music)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.text = QLabel(self.about_music)
        self.text.setObjectName(u"text")
        self.text.setStyleSheet(u"")
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.text, 0, Qt.AlignmentFlag.AlignVCenter)

        self.artist = QLabel(self.about_music)
        self.artist.setObjectName(u"artist")
        self.artist.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.artist, 0, Qt.AlignmentFlag.AlignVCenter)

        self.title = QLabel(self.about_music)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.title, 0,Qt.AlignmentFlag.AlignVCenter)

        self.title.raise_()
        self.artist.raise_()
        self.text.raise_()

        self.horizontalLayout_8.addWidget(self.about_music, 0,Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.music_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"background-color: rgb(75, 75, 75);\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(60)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(75, 0, 15, 0)
        self.play_stop_btn = QPushButton(self.frame_2)
        self.play_stop_btn.setObjectName(u"play_stop_btn")
        self.play_stop_btn.setMinimumSize(QSize(100, 100))
        self.play_stop_btn.setStyleSheet(u"QPushButton{\n"
"image: url(:/newPrefix/material_design/play_circle_outline.png);\n"
"border-radius:50px;\n"
"background-color: rgb(156, 126, 255);\n"
"padding:10px;\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"background-color: rgb(255, 82, 52);\n"
"border-radius:50px;\n"
"padding:0px;\n"
" }\n"
"\n"
"QPushButton:checked { \n"
"image: url(:/newPrefix/material_design/pause_circle_outline.png);\n"
"border-radius:50px;\n"
"padding:10px;\n"
"background-color: rgb(24, 255, 8);\n"
" }\n"
"\n"
"\n"
"QPushButton:checked:hover { \n"
"background-color: rgb(255, 82, 52);\n"
"border-radius:50px;\n"
"padding:0px;\n"
" }\n"
"\n"
"")
        self.play_stop_btn.setIconSize(QSize(50, 50))
        self.play_stop_btn.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.play_stop_btn)

        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"max-width:500px;\n"
"max-height:100px;\n"
"}")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.vol = QLabel(self.widget)
        self.vol.setObjectName(u"vol")
        self.vol.setMinimumSize(QSize(40, 40))
        self.vol.setStyleSheet(u"image: url(:/newPrefix/feather/volume-1.png);\n"
"")

        self.gridLayout.addWidget(self.vol, 1, 1, 1, 1)

        self.vol_slider = QSlider(self.widget)
        self.vol_slider.setObjectName(u"vol_slider")
        self.vol_slider.setMaximum(100)
        self.vol_slider.setValue(50)
        self.vol_slider.setTracking(True)
        self.vol_slider.setOrientation(Qt.Orientation.Horizontal)
        self.vol_slider.setInvertedAppearance(False)
        self.vol_slider.setInvertedControls(False)

        self.gridLayout.addWidget(self.vol_slider, 1, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.widget)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.music_page)
        self.chatgpt_page = QWidget()
        self.chatgpt_page.setObjectName(u"chatgpt_page")
        self.chatgpt_page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.chatgpt_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.webEngineView = QWebEngineView(self.chatgpt_page)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setUrl(QUrl(u"https://chatgpt.com/"))

        self.verticalLayout_6.addWidget(self.webEngineView)

        self.stackedWidget.addWidget(self.chatgpt_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_items)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 50))
        self.main_footer.setMaximumSize(QSize(16777215, 50))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"border-top-color:1px solid #000;\n"
"\n"
"}")
        self.main_footer.setFrameShape(QFrame.Shape.NoFrame)
        self.main_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.main_footer)
        self.version.setObjectName(u"version")
        font8 = QFont()
        font8.setPointSize(11)
        self.version.setFont(font8)

        self.horizontalLayout_7.addWidget(self.version)


        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menubtn.setText("")
        self.minimizebtn.setText("")
        self.closebtn.setText("")
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"      HOME", None))
        self.music_btn.setText(QCoreApplication.translate("MainWindow", u"       MUSIC", None))
        self.gpt_btn.setText(QCoreApplication.translate("MainWindow", u"     CHATGPT", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.day.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"City", None))
        self.go.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.weather_temp.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.weather_text.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.weather_name.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.weather_region.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.events.setText(QCoreApplication.translate("MainWindow", u"\u0645\u0646\u0627\u0633\u0628 \u0627\u0645\u0631\u0648\u0632", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tomorrow", None))
        self.tomorrow_icon.setText("")
        self.tomorrow_forecast.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.tomorrow_temp.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lbl_1.setText("")
        self.icon_1.setText("")
        self.forecast_1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.temp_1.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lbl_2.setText("")
        self.icon_2.setText("")
        self.forecast_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.temp_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.text.setText(QCoreApplication.translate("MainWindow", u"TEXT", None))
        self.artist.setText(QCoreApplication.translate("MainWindow", u"ARTIST", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"TITLE", None))
        self.play_stop_btn.setText("")
        self.vol.setText("")
        self.version.setText(QCoreApplication.translate("MainWindow", u"v 1.0", None))
    # retranslateUi

