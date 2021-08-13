# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainV1eQqJKF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1267, 898)
        MainWindow.setMinimumSize(QSize(1200, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1024, 0))
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setMinimumSize(QSize(1024, 0))
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 0.9), stop:0.555556 rgba(28, 29, 73, 0.9));\n"
"border-radius:10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout = QVBoxLayout(self.drop_shadow_frame)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(1, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color:none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.title_bar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        self.frame_title.setLayoutDirection(Qt.RightToLeft)
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Roboto Medium")
        font.setPointSize(10)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(60, 231, 195);\n"
"")
        self.label_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.label_title)

        self.frame_btns = QFrame(self.frame_title)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setLayoutDirection(Qt.LeftToRight)
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 0, 0,150);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_close)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 170, 0,150);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(16, 16))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius:8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(85, 255, 127,150);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_maximize)


        self.horizontalLayout_19.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.frame_title)


        self.drop_shadow_layout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setMinimumSize(QSize(1024, 0))
        self.content_bar.setStyleSheet(u"background-color:none;")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_bar)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_bar)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1024, 0))
        self.stackedWidget.setMaximumSize(QSize(16777209, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setMinimumSize(QSize(1024, 0))
        self.verticalLayout_7 = QVBoxLayout(self.page_home)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_content_home = QFrame(self.page_home)
        self.frame_content_home.setObjectName(u"frame_content_home")
        self.frame_content_home.setFrameShape(QFrame.StyledPanel)
        self.frame_content_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_content_home)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_17 = QFrame(self.frame_content_home)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 250))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 120, 0)
        self.frame_GestiuneDeVanzari = QFrame(self.frame_17)
        self.frame_GestiuneDeVanzari.setObjectName(u"frame_GestiuneDeVanzari")
        self.frame_GestiuneDeVanzari.setMinimumSize(QSize(150, 150))
        self.frame_GestiuneDeVanzari.setMaximumSize(QSize(150, 150))
        self.frame_GestiuneDeVanzari.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_GestiuneDeVanzari.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:75px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_GestiuneDeVanzari.setFrameShape(QFrame.StyledPanel)
        self.frame_GestiuneDeVanzari.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_GestiuneDeVanzari)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 30, 0, 30)
        self.label_numarCercMijloc_2 = QLabel(self.frame_GestiuneDeVanzari)
        self.label_numarCercMijloc_2.setObjectName(u"label_numarCercMijloc_2")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(20)
        self.label_numarCercMijloc_2.setFont(font1)
        self.label_numarCercMijloc_2.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_2.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercMijloc_2.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_2.setScaledContents(False)
        self.label_numarCercMijloc_2.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_2.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_numarCercMijloc_2)

        self.label_textSusCercMijloc_2 = QLabel(self.frame_GestiuneDeVanzari)
        self.label_textSusCercMijloc_2.setObjectName(u"label_textSusCercMijloc_2")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(14)
        self.label_textSusCercMijloc_2.setFont(font2)
        self.label_textSusCercMijloc_2.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_2.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_2.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_2.setScaledContents(False)
        self.label_textSusCercMijloc_2.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_2.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_textSusCercMijloc_2)

        self.label_textJosCercMijloc_2 = QLabel(self.frame_GestiuneDeVanzari)
        self.label_textJosCercMijloc_2.setObjectName(u"label_textJosCercMijloc_2")
        self.label_textJosCercMijloc_2.setFont(font2)
        self.label_textJosCercMijloc_2.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercMijloc_2.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textJosCercMijloc_2.setTextFormat(Qt.AutoText)
        self.label_textJosCercMijloc_2.setScaledContents(False)
        self.label_textJosCercMijloc_2.setAlignment(Qt.AlignCenter)
        self.label_textJosCercMijloc_2.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_textJosCercMijloc_2)


        self.horizontalLayout_17.addWidget(self.frame_GestiuneDeVanzari)

        self.label = QLabel(self.frame_17)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(500, 120))
        self.label.setMaximumSize(QSize(500, 120))
        self.label.setPixmap(QPixmap(u"../../myAmanet-Manager/env/assets/logo/easy 1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.label)


        self.verticalLayout_35.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_content_home)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(1200, 0))
        font3 = QFont()
        font3.setPointSize(14)
        self.frame_16.setFont(font3)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_cercStanga = QFrame(self.frame_16)
        self.frame_cercStanga.setObjectName(u"frame_cercStanga")
        self.frame_cercStanga.setMinimumSize(QSize(250, 250))
        self.frame_cercStanga.setMaximumSize(QSize(250, 250))
        self.frame_cercStanga.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_cercStanga.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercStanga.setFrameShape(QFrame.StyledPanel)
        self.frame_cercStanga.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_cercStanga)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 50, 10, 50)
        self.label_numarCercStanga = QLabel(self.frame_cercStanga)
        self.label_numarCercStanga.setObjectName(u"label_numarCercStanga")
        font4 = QFont()
        font4.setFamily(u"Roboto")
        font4.setPointSize(70)
        self.label_numarCercStanga.setFont(font4)
        self.label_numarCercStanga.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercStanga.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercStanga.setTextFormat(Qt.AutoText)
        self.label_numarCercStanga.setScaledContents(False)
        self.label_numarCercStanga.setAlignment(Qt.AlignCenter)
        self.label_numarCercStanga.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_numarCercStanga)

        self.label_textSusCercStanga = QLabel(self.frame_cercStanga)
        self.label_textSusCercStanga.setObjectName(u"label_textSusCercStanga")
        self.label_textSusCercStanga.setFont(font2)
        self.label_textSusCercStanga.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercStanga.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercStanga.setTextFormat(Qt.AutoText)
        self.label_textSusCercStanga.setScaledContents(False)
        self.label_textSusCercStanga.setAlignment(Qt.AlignCenter)
        self.label_textSusCercStanga.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_textSusCercStanga)

        self.label_textJosCercStanga = QLabel(self.frame_cercStanga)
        self.label_textJosCercStanga.setObjectName(u"label_textJosCercStanga")
        self.label_textJosCercStanga.setFont(font2)
        self.label_textJosCercStanga.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercStanga.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textJosCercStanga.setTextFormat(Qt.AutoText)
        self.label_textJosCercStanga.setScaledContents(False)
        self.label_textJosCercStanga.setAlignment(Qt.AlignCenter)
        self.label_textJosCercStanga.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_textJosCercStanga)


        self.horizontalLayout_2.addWidget(self.frame_cercStanga)

        self.frame_cercDreapta = QFrame(self.frame_16)
        self.frame_cercDreapta.setObjectName(u"frame_cercDreapta")
        self.frame_cercDreapta.setMinimumSize(QSize(250, 250))
        self.frame_cercDreapta.setMaximumSize(QSize(250, 250))
        self.frame_cercDreapta.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_cercDreapta.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercDreapta.setFrameShape(QFrame.StyledPanel)
        self.frame_cercDreapta.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_cercDreapta)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 50, 10, 50)
        self.label_numarCercDreapta = QLabel(self.frame_cercDreapta)
        self.label_numarCercDreapta.setObjectName(u"label_numarCercDreapta")
        self.label_numarCercDreapta.setFont(font4)
        self.label_numarCercDreapta.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta.setScaledContents(False)
        self.label_numarCercDreapta.setAlignment(Qt.AlignCenter)
        self.label_numarCercDreapta.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_numarCercDreapta)

        self.label_textSusCercDreapta = QLabel(self.frame_cercDreapta)
        self.label_textSusCercDreapta.setObjectName(u"label_textSusCercDreapta")
        self.label_textSusCercDreapta.setFont(font2)
        self.label_textSusCercDreapta.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercDreapta.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercDreapta.setTextFormat(Qt.AutoText)
        self.label_textSusCercDreapta.setScaledContents(False)
        self.label_textSusCercDreapta.setAlignment(Qt.AlignCenter)
        self.label_textSusCercDreapta.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_textSusCercDreapta)

        self.label_textJosCercDreapta = QLabel(self.frame_cercDreapta)
        self.label_textJosCercDreapta.setObjectName(u"label_textJosCercDreapta")
        self.label_textJosCercDreapta.setFont(font2)
        self.label_textJosCercDreapta.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercDreapta.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textJosCercDreapta.setTextFormat(Qt.AutoText)
        self.label_textJosCercDreapta.setScaledContents(False)
        self.label_textJosCercDreapta.setAlignment(Qt.AlignCenter)
        self.label_textJosCercDreapta.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_textJosCercDreapta)


        self.horizontalLayout_2.addWidget(self.frame_cercDreapta)

        self.frame_cercMijloc = QFrame(self.frame_16)
        self.frame_cercMijloc.setObjectName(u"frame_cercMijloc")
        self.frame_cercMijloc.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_cercMijloc.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc.setFrameShape(QFrame.StyledPanel)
        self.frame_cercMijloc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_cercMijloc)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 50, 10, 50)
        self.label_numarCercMijloc = QLabel(self.frame_cercMijloc)
        self.label_numarCercMijloc.setObjectName(u"label_numarCercMijloc")
        self.label_numarCercMijloc.setFont(font4)
        self.label_numarCercMijloc.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercMijloc.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc.setScaledContents(False)
        self.label_numarCercMijloc.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_numarCercMijloc)

        self.label_textSusCercMijloc = QLabel(self.frame_cercMijloc)
        self.label_textSusCercMijloc.setObjectName(u"label_textSusCercMijloc")
        self.label_textSusCercMijloc.setFont(font2)
        self.label_textSusCercMijloc.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc.setScaledContents(False)
        self.label_textSusCercMijloc.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_textSusCercMijloc)

        self.label_textJosCercMijloc = QLabel(self.frame_cercMijloc)
        self.label_textJosCercMijloc.setObjectName(u"label_textJosCercMijloc")
        self.label_textJosCercMijloc.setFont(font2)
        self.label_textJosCercMijloc.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercMijloc.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textJosCercMijloc.setTextFormat(Qt.AutoText)
        self.label_textJosCercMijloc.setScaledContents(False)
        self.label_textJosCercMijloc.setAlignment(Qt.AlignCenter)
        self.label_textJosCercMijloc.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_textJosCercMijloc)


        self.horizontalLayout_2.addWidget(self.frame_cercMijloc)


        self.verticalLayout_35.addWidget(self.frame_16)


        self.verticalLayout_7.addWidget(self.frame_content_home)

        self.frame_butoane_home = QFrame(self.page_home)
        self.frame_butoane_home.setObjectName(u"frame_butoane_home")
        self.frame_butoane_home.setMinimumSize(QSize(0, 50))
        self.frame_butoane_home.setMaximumSize(QSize(16777215, 50))
        self.frame_butoane_home.setFrameShape(QFrame.StyledPanel)
        self.frame_butoane_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_butoane_home)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_genereazaContract = QPushButton(self.frame_butoane_home)
        self.pushButton_genereazaContract.setObjectName(u"pushButton_genereazaContract")
        self.pushButton_genereazaContract.setMinimumSize(QSize(165, 28))
        self.pushButton_genereazaContract.setMaximumSize(QSize(165, 35))
        font5 = QFont()
        font5.setFamily(u"Roboto Medium")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        self.pushButton_genereazaContract.setFont(font5)
        self.pushButton_genereazaContract.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_genereazaContract.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_genereazaContract.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_genereazaContract)

        self.pushButton_cautaClient = QPushButton(self.frame_butoane_home)
        self.pushButton_cautaClient.setObjectName(u"pushButton_cautaClient")
        self.pushButton_cautaClient.setMinimumSize(QSize(165, 28))
        self.pushButton_cautaClient.setMaximumSize(QSize(165, 35))
        self.pushButton_cautaClient.setFont(font5)
        self.pushButton_cautaClient.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cautaClient.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_cautaClient.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_cautaClient)


        self.verticalLayout_7.addWidget(self.frame_butoane_home)

        self.stackedWidget.addWidget(self.page_home)
        self.page_genereazaContractDetaliiClient = QWidget()
        self.page_genereazaContractDetaliiClient.setObjectName(u"page_genereazaContractDetaliiClient")
        self.page_genereazaContractDetaliiClient.setMinimumSize(QSize(1024, 0))
        self.verticalLayout_26 = QVBoxLayout(self.page_genereazaContractDetaliiClient)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_83 = QFrame(self.page_genereazaContractDetaliiClient)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 500))
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.frame_30 = QFrame(self.frame_83)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(400, 500))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_cercMijloc_16 = QFrame(self.frame_30)
        self.frame_cercMijloc_16.setObjectName(u"frame_cercMijloc_16")
        self.frame_cercMijloc_16.setMinimumSize(QSize(250, 150))
        self.frame_cercMijloc_16.setMaximumSize(QSize(250, 150))
        self.frame_cercMijloc_16.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:75px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_16.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_cercMijloc_16)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(20, -1, 20, -1)
        self.label_textSusCercMijloc_48 = QLabel(self.frame_cercMijloc_16)
        self.label_textSusCercMijloc_48.setObjectName(u"label_textSusCercMijloc_48")
        font6 = QFont()
        font6.setFamily(u"Roboto")
        font6.setPointSize(12)
        self.label_textSusCercMijloc_48.setFont(font6)
        self.label_textSusCercMijloc_48.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_48.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_48.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_48.setScaledContents(False)
        self.label_textSusCercMijloc_48.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_48.setWordWrap(True)

        self.verticalLayout_49.addWidget(self.label_textSusCercMijloc_48)

        self.frame_84 = QFrame(self.frame_cercMijloc_16)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setStyleSheet(u"border:none")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.radioButton_3 = QRadioButton(self.frame_84)
        self.radioButton_3.setObjectName(u"radioButton_3")
        font7 = QFont()
        font7.setFamily(u"Roboto Light")
        font7.setPointSize(12)
        self.radioButton_3.setFont(font7)
        self.radioButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_3.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")

        self.horizontalLayout_81.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.frame_84)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font7)
        self.radioButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_4.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")

        self.horizontalLayout_81.addWidget(self.radioButton_4)


        self.verticalLayout_49.addWidget(self.frame_84)

        self.frame_85 = QFrame(self.frame_cercMijloc_16)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")

        self.verticalLayout_49.addWidget(self.frame_85)


        self.horizontalLayout_24.addWidget(self.frame_cercMijloc_16)


        self.horizontalLayout_107.addWidget(self.frame_30)

        self.frame_detaliiClient = QFrame(self.frame_83)
        self.frame_detaliiClient.setObjectName(u"frame_detaliiClient")
        self.frame_detaliiClient.setMinimumSize(QSize(500, 500))
        self.frame_detaliiClient.setMaximumSize(QSize(1024, 16777215))
        self.frame_detaliiClient.setFrameShape(QFrame.NoFrame)
        self.frame_detaliiClient.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_detaliiClient)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(20)
        self.label_dateClient = QLabel(self.frame_detaliiClient)
        self.label_dateClient.setObjectName(u"label_dateClient")
        self.label_dateClient.setMinimumSize(QSize(200, 30))
        self.label_dateClient.setMaximumSize(QSize(200, 30))
        font8 = QFont()
        font8.setFamily(u"Roboto Medium")
        font8.setPointSize(14)
        self.label_dateClient.setFont(font8)
        self.label_dateClient.setStyleSheet(u"color: rgba(255, 170, 0,0.7);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_dateClient)

        self.label_Nume = QLabel(self.frame_detaliiClient)
        self.label_Nume.setObjectName(u"label_Nume")
        self.label_Nume.setMinimumSize(QSize(120, 30))
        self.label_Nume.setMaximumSize(QSize(120, 30))
        font9 = QFont()
        font9.setFamily(u"Roboto Light")
        font9.setPointSize(14)
        self.label_Nume.setFont(font9)
        self.label_Nume.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Nume.setTextFormat(Qt.RichText)
        self.label_Nume.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_Nume)

        self.lineEdit_NumeClient = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_NumeClient.setObjectName(u"lineEdit_NumeClient")
        self.lineEdit_NumeClient.setMinimumSize(QSize(300, 20))
        self.lineEdit_NumeClient.setMaximumSize(QSize(300, 30))
        self.lineEdit_NumeClient.setFont(font7)
        self.lineEdit_NumeClient.setFrame(True)
        self.lineEdit_NumeClient.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_NumeClient.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_NumeClient)

        self.label_Prenume = QLabel(self.frame_detaliiClient)
        self.label_Prenume.setObjectName(u"label_Prenume")
        self.label_Prenume.setMinimumSize(QSize(120, 30))
        self.label_Prenume.setMaximumSize(QSize(120, 30))
        self.label_Prenume.setFont(font9)
        self.label_Prenume.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Prenume.setTextFormat(Qt.RichText)
        self.label_Prenume.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_Prenume)

        self.lineEdit_PrenumeClient = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_PrenumeClient.setObjectName(u"lineEdit_PrenumeClient")
        self.lineEdit_PrenumeClient.setMinimumSize(QSize(300, 20))
        self.lineEdit_PrenumeClient.setMaximumSize(QSize(300, 30))
        self.lineEdit_PrenumeClient.setFont(font7)
        self.lineEdit_PrenumeClient.setFrame(True)
        self.lineEdit_PrenumeClient.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_PrenumeClient)

        self.label_SerieCI = QLabel(self.frame_detaliiClient)
        self.label_SerieCI.setObjectName(u"label_SerieCI")
        self.label_SerieCI.setMinimumSize(QSize(120, 30))
        self.label_SerieCI.setMaximumSize(QSize(120, 30))
        self.label_SerieCI.setFont(font9)
        self.label_SerieCI.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_SerieCI.setTextFormat(Qt.RichText)
        self.label_SerieCI.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_SerieCI)

        self.lineEdit_SerieCI = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_SerieCI.setObjectName(u"lineEdit_SerieCI")
        self.lineEdit_SerieCI.setMinimumSize(QSize(300, 20))
        self.lineEdit_SerieCI.setMaximumSize(QSize(300, 30))
        self.lineEdit_SerieCI.setFont(font7)
        self.lineEdit_SerieCI.setMaxLength(2)
        self.lineEdit_SerieCI.setFrame(True)
        self.lineEdit_SerieCI.setClearButtonEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_SerieCI)

        self.label_NumarCI = QLabel(self.frame_detaliiClient)
        self.label_NumarCI.setObjectName(u"label_NumarCI")
        self.label_NumarCI.setMinimumSize(QSize(120, 30))
        self.label_NumarCI.setMaximumSize(QSize(120, 30))
        self.label_NumarCI.setFont(font9)
        self.label_NumarCI.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_NumarCI.setTextFormat(Qt.RichText)
        self.label_NumarCI.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_NumarCI)

        self.lineEdit_NumarCI = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_NumarCI.setObjectName(u"lineEdit_NumarCI")
        self.lineEdit_NumarCI.setMinimumSize(QSize(300, 20))
        self.lineEdit_NumarCI.setMaximumSize(QSize(300, 30))
        self.lineEdit_NumarCI.setFont(font7)
        self.lineEdit_NumarCI.setMaxLength(6)
        self.lineEdit_NumarCI.setFrame(True)
        self.lineEdit_NumarCI.setClearButtonEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_NumarCI)

        self.label_CNP = QLabel(self.frame_detaliiClient)
        self.label_CNP.setObjectName(u"label_CNP")
        self.label_CNP.setMinimumSize(QSize(120, 30))
        self.label_CNP.setMaximumSize(QSize(120, 30))
        self.label_CNP.setFont(font9)
        self.label_CNP.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_CNP.setTextFormat(Qt.RichText)
        self.label_CNP.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_CNP)

        self.lineEdit_CNP = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_CNP.setObjectName(u"lineEdit_CNP")
        self.lineEdit_CNP.setMinimumSize(QSize(300, 20))
        self.lineEdit_CNP.setMaximumSize(QSize(300, 30))
        self.lineEdit_CNP.setFont(font7)
        self.lineEdit_CNP.setMaxLength(13)
        self.lineEdit_CNP.setFrame(True)
        self.lineEdit_CNP.setClearButtonEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit_CNP)

        self.label_EliberatDe = QLabel(self.frame_detaliiClient)
        self.label_EliberatDe.setObjectName(u"label_EliberatDe")
        self.label_EliberatDe.setMinimumSize(QSize(120, 30))
        self.label_EliberatDe.setMaximumSize(QSize(120, 30))
        self.label_EliberatDe.setFont(font9)
        self.label_EliberatDe.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_EliberatDe.setTextFormat(Qt.RichText)
        self.label_EliberatDe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_EliberatDe)

        self.lineEdit_EliberatDe = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_EliberatDe.setObjectName(u"lineEdit_EliberatDe")
        self.lineEdit_EliberatDe.setMinimumSize(QSize(300, 20))
        self.lineEdit_EliberatDe.setMaximumSize(QSize(300, 30))
        self.lineEdit_EliberatDe.setFont(font7)
        self.lineEdit_EliberatDe.setFrame(True)
        self.lineEdit_EliberatDe.setClearButtonEnabled(False)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_EliberatDe)

        self.label_DataEliberarii = QLabel(self.frame_detaliiClient)
        self.label_DataEliberarii.setObjectName(u"label_DataEliberarii")
        self.label_DataEliberarii.setMinimumSize(QSize(120, 30))
        self.label_DataEliberarii.setMaximumSize(QSize(120, 30))
        self.label_DataEliberarii.setFont(font9)
        self.label_DataEliberarii.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_DataEliberarii.setTextFormat(Qt.RichText)
        self.label_DataEliberarii.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_DataEliberarii)

        self.dateEdit_dataEliberarii = QDateEdit(self.frame_detaliiClient)
        self.dateEdit_dataEliberarii.setObjectName(u"dateEdit_dataEliberarii")
        self.dateEdit_dataEliberarii.setMinimumSize(QSize(200, 20))
        self.dateEdit_dataEliberarii.setMaximumSize(QSize(200, 30))
        self.dateEdit_dataEliberarii.setFont(font7)
        self.dateEdit_dataEliberarii.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_dataEliberarii.setCalendarPopup(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.dateEdit_dataEliberarii)

        self.label_Adresa = QLabel(self.frame_detaliiClient)
        self.label_Adresa.setObjectName(u"label_Adresa")
        self.label_Adresa.setMinimumSize(QSize(120, 30))
        self.label_Adresa.setMaximumSize(QSize(120, 30))
        self.label_Adresa.setFont(font9)
        self.label_Adresa.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Adresa.setTextFormat(Qt.RichText)
        self.label_Adresa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_Adresa)

        self.lineEdit_Adresa = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_Adresa.setObjectName(u"lineEdit_Adresa")
        self.lineEdit_Adresa.setMinimumSize(QSize(300, 20))
        self.lineEdit_Adresa.setMaximumSize(QSize(300, 30))
        self.lineEdit_Adresa.setFont(font7)
        self.lineEdit_Adresa.setFrame(True)
        self.lineEdit_Adresa.setClearButtonEnabled(False)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_Adresa)

        self.label_Telefon = QLabel(self.frame_detaliiClient)
        self.label_Telefon.setObjectName(u"label_Telefon")
        self.label_Telefon.setMinimumSize(QSize(120, 30))
        self.label_Telefon.setMaximumSize(QSize(120, 30))
        self.label_Telefon.setFont(font9)
        self.label_Telefon.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Telefon.setTextFormat(Qt.RichText)
        self.label_Telefon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_Telefon)

        self.lineEdit_Telefon = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_Telefon.setObjectName(u"lineEdit_Telefon")
        self.lineEdit_Telefon.setMinimumSize(QSize(300, 20))
        self.lineEdit_Telefon.setMaximumSize(QSize(300, 30))
        self.lineEdit_Telefon.setFont(font7)
        self.lineEdit_Telefon.setFrame(True)
        self.lineEdit_Telefon.setClearButtonEnabled(False)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_Telefon)

        self.label_Email = QLabel(self.frame_detaliiClient)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setMinimumSize(QSize(120, 30))
        self.label_Email.setMaximumSize(QSize(120, 30))
        self.label_Email.setFont(font9)
        self.label_Email.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Email.setTextFormat(Qt.RichText)
        self.label_Email.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_Email)

        self.lineEdit_Email = QLineEdit(self.frame_detaliiClient)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setMinimumSize(QSize(300, 20))
        self.lineEdit_Email.setMaximumSize(QSize(300, 30))
        self.lineEdit_Email.setFont(font7)
        self.lineEdit_Email.setFrame(True)
        self.lineEdit_Email.setClearButtonEnabled(False)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_Email)


        self.horizontalLayout_107.addWidget(self.frame_detaliiClient)


        self.verticalLayout_26.addWidget(self.frame_83)

        self.frame_33 = QFrame(self.page_genereazaContractDetaliiClient)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 50))
        self.frame_33.setMaximumSize(QSize(16777215, 50))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_backToHome = QPushButton(self.frame_33)
        self.pushButton_backToHome.setObjectName(u"pushButton_backToHome")
        self.pushButton_backToHome.setMinimumSize(QSize(30, 30))
        self.pushButton_backToHome.setMaximumSize(QSize(30, 30))
        self.pushButton_backToHome.setFont(font5)
        self.pushButton_backToHome.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_backToHome.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_backToHome.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_backToHome)

        self.pushButton_backToHome_2 = QPushButton(self.frame_33)
        self.pushButton_backToHome_2.setObjectName(u"pushButton_backToHome_2")
        self.pushButton_backToHome_2.setMinimumSize(QSize(30, 30))
        self.pushButton_backToHome_2.setMaximumSize(QSize(30, 30))
        self.pushButton_backToHome_2.setFont(font5)
        self.pushButton_backToHome_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_backToHome_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_backToHome_2.setFlat(False)

        self.horizontalLayout_3.addWidget(self.pushButton_backToHome_2)


        self.verticalLayout_26.addWidget(self.frame_33)

        self.stackedWidget.addWidget(self.page_genereazaContractDetaliiClient)
        self.page_genereazaContractDetaliiProduse = QWidget()
        self.page_genereazaContractDetaliiProduse.setObjectName(u"page_genereazaContractDetaliiProduse")
        self.page_genereazaContractDetaliiProduse.setMinimumSize(QSize(1024, 0))
        self.verticalLayout_43 = QVBoxLayout(self.page_genereazaContractDetaliiProduse)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_14 = QFrame(self.page_genereazaContractDetaliiProduse)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(1024, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_detaliiClient_3 = QFrame(self.frame_14)
        self.frame_detaliiClient_3.setObjectName(u"frame_detaliiClient_3")
        self.frame_detaliiClient_3.setMinimumSize(QSize(1024, 0))
        self.frame_detaliiClient_3.setMaximumSize(QSize(1024, 16777215))
        self.frame_detaliiClient_3.setFrameShape(QFrame.NoFrame)
        self.frame_detaliiClient_3.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_detaliiClient_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(30)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_dateClient_3 = QLabel(self.frame_detaliiClient_3)
        self.label_dateClient_3.setObjectName(u"label_dateClient_3")
        self.label_dateClient_3.setMinimumSize(QSize(200, 30))
        self.label_dateClient_3.setMaximumSize(QSize(200, 30))
        self.label_dateClient_3.setFont(font8)
        self.label_dateClient_3.setStyleSheet(u"color: rgba(255, 170, 0,0.7);")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_dateClient_3)

        self.label_Nume_2 = QLabel(self.frame_detaliiClient_3)
        self.label_Nume_2.setObjectName(u"label_Nume_2")
        self.label_Nume_2.setMinimumSize(QSize(180, 30))
        self.label_Nume_2.setMaximumSize(QSize(120, 30))
        self.label_Nume_2.setFont(font9)
        self.label_Nume_2.setLayoutDirection(Qt.LeftToRight)
        self.label_Nume_2.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Nume_2.setTextFormat(Qt.RichText)
        self.label_Nume_2.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_Nume_2)

        self.lineEdit_ObservatiiProdus = QLineEdit(self.frame_detaliiClient_3)
        self.lineEdit_ObservatiiProdus.setObjectName(u"lineEdit_ObservatiiProdus")
        self.lineEdit_ObservatiiProdus.setMinimumSize(QSize(350, 20))
        self.lineEdit_ObservatiiProdus.setMaximumSize(QSize(350, 30))
        self.lineEdit_ObservatiiProdus.setFont(font7)
        self.lineEdit_ObservatiiProdus.setFrame(True)
        self.lineEdit_ObservatiiProdus.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_ObservatiiProdus)

        self.label_Prenume_3 = QLabel(self.frame_detaliiClient_3)
        self.label_Prenume_3.setObjectName(u"label_Prenume_3")
        self.label_Prenume_3.setMinimumSize(QSize(180, 30))
        self.label_Prenume_3.setMaximumSize(QSize(120, 30))
        self.label_Prenume_3.setFont(font9)
        self.label_Prenume_3.setLayoutDirection(Qt.LeftToRight)
        self.label_Prenume_3.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Prenume_3.setTextFormat(Qt.RichText)
        self.label_Prenume_3.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_Prenume_3)

        self.lineEdit_ValoareEvaluata = QLineEdit(self.frame_detaliiClient_3)
        self.lineEdit_ValoareEvaluata.setObjectName(u"lineEdit_ValoareEvaluata")
        self.lineEdit_ValoareEvaluata.setMinimumSize(QSize(350, 20))
        self.lineEdit_ValoareEvaluata.setMaximumSize(QSize(350, 30))
        self.lineEdit_ValoareEvaluata.setFont(font7)
        self.lineEdit_ValoareEvaluata.setMaxLength(9999)
        self.lineEdit_ValoareEvaluata.setFrame(True)
        self.lineEdit_ValoareEvaluata.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit_ValoareEvaluata)

        self.label_SerieCI_3 = QLabel(self.frame_detaliiClient_3)
        self.label_SerieCI_3.setObjectName(u"label_SerieCI_3")
        self.label_SerieCI_3.setMinimumSize(QSize(180, 30))
        self.label_SerieCI_3.setMaximumSize(QSize(120, 30))
        self.label_SerieCI_3.setFont(font9)
        self.label_SerieCI_3.setLayoutDirection(Qt.LeftToRight)
        self.label_SerieCI_3.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_SerieCI_3.setTextFormat(Qt.RichText)
        self.label_SerieCI_3.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_SerieCI_3)

        self.lineEdit_SumaImprumutata = QLineEdit(self.frame_detaliiClient_3)
        self.lineEdit_SumaImprumutata.setObjectName(u"lineEdit_SumaImprumutata")
        self.lineEdit_SumaImprumutata.setMinimumSize(QSize(350, 20))
        self.lineEdit_SumaImprumutata.setMaximumSize(QSize(350, 30))
        self.lineEdit_SumaImprumutata.setFont(font7)
        self.lineEdit_SumaImprumutata.setMaxLength(9999)
        self.lineEdit_SumaImprumutata.setFrame(True)
        self.lineEdit_SumaImprumutata.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.lineEdit_SumaImprumutata)

        self.label_NumarCI_3 = QLabel(self.frame_detaliiClient_3)
        self.label_NumarCI_3.setObjectName(u"label_NumarCI_3")
        self.label_NumarCI_3.setMinimumSize(QSize(180, 30))
        self.label_NumarCI_3.setMaximumSize(QSize(120, 30))
        self.label_NumarCI_3.setFont(font9)
        self.label_NumarCI_3.setLayoutDirection(Qt.LeftToRight)
        self.label_NumarCI_3.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_NumarCI_3.setTextFormat(Qt.RichText)
        self.label_NumarCI_3.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_NumarCI_3)

        self.lineEdit_ComisionLuna = QLineEdit(self.frame_detaliiClient_3)
        self.lineEdit_ComisionLuna.setObjectName(u"lineEdit_ComisionLuna")
        self.lineEdit_ComisionLuna.setMinimumSize(QSize(350, 20))
        self.lineEdit_ComisionLuna.setMaximumSize(QSize(350, 30))
        self.lineEdit_ComisionLuna.setFont(font7)
        self.lineEdit_ComisionLuna.setMaxLength(9999)
        self.lineEdit_ComisionLuna.setFrame(True)
        self.lineEdit_ComisionLuna.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.lineEdit_ComisionLuna)

        self.label_NumarCI_4 = QLabel(self.frame_detaliiClient_3)
        self.label_NumarCI_4.setObjectName(u"label_NumarCI_4")
        self.label_NumarCI_4.setMinimumSize(QSize(180, 30))
        self.label_NumarCI_4.setMaximumSize(QSize(120, 30))
        self.label_NumarCI_4.setFont(font9)
        self.label_NumarCI_4.setLayoutDirection(Qt.LeftToRight)
        self.label_NumarCI_4.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_NumarCI_4.setTextFormat(Qt.RichText)
        self.label_NumarCI_4.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_NumarCI_4)

        self.lineEdit_denumireProdus = QLineEdit(self.frame_detaliiClient_3)
        self.lineEdit_denumireProdus.setObjectName(u"lineEdit_denumireProdus")
        self.lineEdit_denumireProdus.setMinimumSize(QSize(350, 20))
        self.lineEdit_denumireProdus.setMaximumSize(QSize(350, 30))
        self.lineEdit_denumireProdus.setFont(font7)
        self.lineEdit_denumireProdus.setFrame(True)
        self.lineEdit_denumireProdus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_denumireProdus.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_denumireProdus)


        self.horizontalLayout_32.addWidget(self.frame_detaliiClient_3)


        self.verticalLayout_43.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page_genereazaContractDetaliiProduse)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.pushButton_adaugaProdus = QPushButton(self.frame_15)
        self.pushButton_adaugaProdus.setObjectName(u"pushButton_adaugaProdus")
        self.pushButton_adaugaProdus.setMinimumSize(QSize(165, 28))
        self.pushButton_adaugaProdus.setMaximumSize(QSize(165, 35))
        self.pushButton_adaugaProdus.setFont(font5)
        self.pushButton_adaugaProdus.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_adaugaProdus.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_adaugaProdus.setFlat(False)

        self.horizontalLayout_30.addWidget(self.pushButton_adaugaProdus)

        self.pushButton_finalizareContract = QPushButton(self.frame_15)
        self.pushButton_finalizareContract.setObjectName(u"pushButton_finalizareContract")
        self.pushButton_finalizareContract.setMinimumSize(QSize(165, 28))
        self.pushButton_finalizareContract.setMaximumSize(QSize(165, 35))
        self.pushButton_finalizareContract.setFont(font5)
        self.pushButton_finalizareContract.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareContract.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_finalizareContract.setFlat(False)

        self.horizontalLayout_30.addWidget(self.pushButton_finalizareContract)


        self.verticalLayout_43.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page_genereazaContractDetaliiProduse)
        self.page_cautaClient = QWidget()
        self.page_cautaClient.setObjectName(u"page_cautaClient")
        self.page_cautaClient.setMinimumSize(QSize(1024, 0))
        self.verticalLayout_6 = QVBoxLayout(self.page_cautaClient)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_11 = QFrame(self.page_cautaClient)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(1024, 300))
        self.frame_11.setMaximumSize(QSize(16777215, 300))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_cercMijloc_9 = QFrame(self.frame_11)
        self.frame_cercMijloc_9.setObjectName(u"frame_cercMijloc_9")
        self.frame_cercMijloc_9.setMinimumSize(QSize(300, 250))
        self.frame_cercMijloc_9.setMaximumSize(QSize(300, 250))
        self.frame_cercMijloc_9.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:100px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_9.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_cercMijloc_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, -1, 20, -1)
        self.label_textSusCercMijloc_9 = QLabel(self.frame_cercMijloc_9)
        self.label_textSusCercMijloc_9.setObjectName(u"label_textSusCercMijloc_9")
        self.label_textSusCercMijloc_9.setFont(font6)
        self.label_textSusCercMijloc_9.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_9.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_9.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_9.setScaledContents(False)
        self.label_textSusCercMijloc_9.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_9.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_textSusCercMijloc_9)

        self.frame_28 = QFrame(self.frame_cercMijloc_9)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border:none")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_numarContractDePrelungit_5 = QLabel(self.frame_28)
        self.label_numarContractDePrelungit_5.setObjectName(u"label_numarContractDePrelungit_5")
        self.label_numarContractDePrelungit_5.setMinimumSize(QSize(10, 30))
        self.label_numarContractDePrelungit_5.setMaximumSize(QSize(150, 30))
        self.label_numarContractDePrelungit_5.setFont(font9)
        self.label_numarContractDePrelungit_5.setStyleSheet(u"QLabel{\n"
"border:none;\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_numarContractDePrelungit_5.setTextFormat(Qt.RichText)
        self.label_numarContractDePrelungit_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_numarContractDePrelungit_5)

        self.radioButton_2 = QRadioButton(self.frame_28)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font7)
        self.radioButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_2.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")

        self.horizontalLayout_8.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.frame_28)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font7)
        self.radioButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")

        self.horizontalLayout_8.addWidget(self.radioButton)


        self.verticalLayout_11.addWidget(self.frame_28)

        self.stackedWidget_2 = QStackedWidget(self.frame_cercMijloc_9)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.stackedWidget_2.setStyleSheet(u"border: none;")
        self.page_cautaDupaNume = QWidget()
        self.page_cautaDupaNume.setObjectName(u"page_cautaDupaNume")
        self.horizontalLayout_26 = QHBoxLayout(self.page_cautaDupaNume)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lineEdit_CautaNume = QLineEdit(self.page_cautaDupaNume)
        self.lineEdit_CautaNume.setObjectName(u"lineEdit_CautaNume")
        self.lineEdit_CautaNume.setMinimumSize(QSize(0, 30))
        self.lineEdit_CautaNume.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_CautaNume.setFont(font7)
        self.lineEdit_CautaNume.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.lineEdit_CautaNume)

        self.lineEdit_CautaPrenume = QLineEdit(self.page_cautaDupaNume)
        self.lineEdit_CautaPrenume.setObjectName(u"lineEdit_CautaPrenume")
        self.lineEdit_CautaPrenume.setMinimumSize(QSize(0, 30))
        self.lineEdit_CautaPrenume.setMaximumSize(QSize(16777215, 30))
        self.lineEdit_CautaPrenume.setFont(font7)
        self.lineEdit_CautaPrenume.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_26.addWidget(self.lineEdit_CautaPrenume)

        self.stackedWidget_2.addWidget(self.page_cautaDupaNume)
        self.page_cautaDupaCnp = QWidget()
        self.page_cautaDupaCnp.setObjectName(u"page_cautaDupaCnp")
        self.horizontalLayout_23 = QHBoxLayout(self.page_cautaDupaCnp)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lineEdit_CautaCnp = QLineEdit(self.page_cautaDupaCnp)
        self.lineEdit_CautaCnp.setObjectName(u"lineEdit_CautaCnp")
        self.lineEdit_CautaCnp.setMinimumSize(QSize(200, 30))
        self.lineEdit_CautaCnp.setMaximumSize(QSize(200, 30))
        self.lineEdit_CautaCnp.setFont(font7)
        self.lineEdit_CautaCnp.setMaxLength(13)

        self.horizontalLayout_23.addWidget(self.lineEdit_CautaCnp)

        self.stackedWidget_2.addWidget(self.page_cautaDupaCnp)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)

        self.frame_38 = QFrame(self.frame_cercMijloc_9)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_finalizareContract_5 = QPushButton(self.frame_38)
        self.pushButton_finalizareContract_5.setObjectName(u"pushButton_finalizareContract_5")
        self.pushButton_finalizareContract_5.setMinimumSize(QSize(50, 30))
        self.pushButton_finalizareContract_5.setMaximumSize(QSize(50, 30))
        self.pushButton_finalizareContract_5.setFont(font5)
        self.pushButton_finalizareContract_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareContract_5.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../Amanet-Manager/assets/search-loupe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_finalizareContract_5.setIcon(icon)
        self.pushButton_finalizareContract_5.setFlat(False)

        self.horizontalLayout_10.addWidget(self.pushButton_finalizareContract_5)


        self.verticalLayout_11.addWidget(self.frame_38)


        self.horizontalLayout_7.addWidget(self.frame_cercMijloc_9)

        self.stackedWidget_3 = QStackedWidget(self.frame_11)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(260, 260))
        self.stackedWidget_3.setMaximumSize(QSize(260, 260))
        self.page_ClientGasit = QWidget()
        self.page_ClientGasit.setObjectName(u"page_ClientGasit")
        self.page_ClientGasit.setMinimumSize(QSize(3, 0))
        self.horizontalLayout_9 = QHBoxLayout(self.page_ClientGasit)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_cercMijloc_13 = QFrame(self.page_ClientGasit)
        self.frame_cercMijloc_13.setObjectName(u"frame_cercMijloc_13")
        self.frame_cercMijloc_13.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc_13.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc_13.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_13.setFrameShape(QFrame.StyledPanel)
        self.frame_cercMijloc_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_cercMijloc_13)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 50, 0, 50)
        self.label_numarCercMijloc_6 = QLabel(self.frame_cercMijloc_13)
        self.label_numarCercMijloc_6.setObjectName(u"label_numarCercMijloc_6")
        font10 = QFont()
        font10.setFamily(u"Roboto Thin")
        font10.setPointSize(60)
        self.label_numarCercMijloc_6.setFont(font10)
        self.label_numarCercMijloc_6.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_6.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercMijloc_6.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_6.setScaledContents(False)
        self.label_numarCercMijloc_6.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_6.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.label_numarCercMijloc_6)

        self.label_textSusCercMijloc_12 = QLabel(self.frame_cercMijloc_13)
        self.label_textSusCercMijloc_12.setObjectName(u"label_textSusCercMijloc_12")
        self.label_textSusCercMijloc_12.setFont(font6)
        self.label_textSusCercMijloc_12.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_12.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_12.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_12.setScaledContents(False)
        self.label_textSusCercMijloc_12.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_12.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.label_textSusCercMijloc_12)


        self.horizontalLayout_9.addWidget(self.frame_cercMijloc_13)

        self.stackedWidget_3.addWidget(self.page_ClientGasit)
        self.page_ClientNegasit = QWidget()
        self.page_ClientNegasit.setObjectName(u"page_ClientNegasit")
        self.horizontalLayout_13 = QHBoxLayout(self.page_ClientNegasit)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_cercMijloc_14 = QFrame(self.page_ClientNegasit)
        self.frame_cercMijloc_14.setObjectName(u"frame_cercMijloc_14")
        self.frame_cercMijloc_14.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc_14.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc_14.setStyleSheet(u"QFrame{\n"
"	border:5px solid  rgb(234, 107, 107);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_14.setFrameShape(QFrame.StyledPanel)
        self.frame_cercMijloc_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_cercMijloc_14)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 50, 0, 50)
        self.label_numarCercMijloc_8 = QLabel(self.frame_cercMijloc_14)
        self.label_numarCercMijloc_8.setObjectName(u"label_numarCercMijloc_8")
        self.label_numarCercMijloc_8.setFont(font10)
        self.label_numarCercMijloc_8.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_8.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercMijloc_8.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_8.setScaledContents(False)
        self.label_numarCercMijloc_8.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_8.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.label_numarCercMijloc_8)

        self.label_textSusCercMijloc_16 = QLabel(self.frame_cercMijloc_14)
        self.label_textSusCercMijloc_16.setObjectName(u"label_textSusCercMijloc_16")
        self.label_textSusCercMijloc_16.setFont(font6)
        self.label_textSusCercMijloc_16.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_16.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_16.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_16.setScaledContents(False)
        self.label_textSusCercMijloc_16.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_16.setWordWrap(True)

        self.verticalLayout_38.addWidget(self.label_textSusCercMijloc_16)


        self.horizontalLayout_13.addWidget(self.frame_cercMijloc_14)

        self.stackedWidget_3.addWidget(self.page_ClientNegasit)
        self.page_MaiMultiClientiGasiti = QWidget()
        self.page_MaiMultiClientiGasiti.setObjectName(u"page_MaiMultiClientiGasiti")
        self.horizontalLayout_14 = QHBoxLayout(self.page_MaiMultiClientiGasiti)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_cercMijloc_4 = QFrame(self.page_MaiMultiClientiGasiti)
        self.frame_cercMijloc_4.setObjectName(u"frame_cercMijloc_4")
        self.frame_cercMijloc_4.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc_4.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc_4.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(244, 163, 0);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_4.setFrameShape(QFrame.StyledPanel)
        self.frame_cercMijloc_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_cercMijloc_4)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 30, 10, 35)
        self.label_numarCercMijloc_4 = QLabel(self.frame_cercMijloc_4)
        self.label_numarCercMijloc_4.setObjectName(u"label_numarCercMijloc_4")
        self.label_numarCercMijloc_4.setMinimumSize(QSize(0, 65))
        self.label_numarCercMijloc_4.setMaximumSize(QSize(16777215, 65))
        self.label_numarCercMijloc_4.setFont(font10)
        self.label_numarCercMijloc_4.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_4.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);\n"
"")
        self.label_numarCercMijloc_4.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_4.setScaledContents(False)
        self.label_numarCercMijloc_4.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_4.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_numarCercMijloc_4)

        self.label_textSusCercMijloc_4 = QLabel(self.frame_cercMijloc_4)
        self.label_textSusCercMijloc_4.setObjectName(u"label_textSusCercMijloc_4")
        self.label_textSusCercMijloc_4.setMinimumSize(QSize(0, 50))
        self.label_textSusCercMijloc_4.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_4.setFont(font6)
        self.label_textSusCercMijloc_4.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_4.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_4.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_4.setScaledContents(False)
        self.label_textSusCercMijloc_4.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_4.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_textSusCercMijloc_4)

        self.label_textJosCercMijloc_4 = QLabel(self.frame_cercMijloc_4)
        self.label_textJosCercMijloc_4.setObjectName(u"label_textJosCercMijloc_4")
        self.label_textJosCercMijloc_4.setMinimumSize(QSize(0, 50))
        self.label_textJosCercMijloc_4.setMaximumSize(QSize(16777215, 50))
        self.label_textJosCercMijloc_4.setFont(font6)
        self.label_textJosCercMijloc_4.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercMijloc_4.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textJosCercMijloc_4.setTextFormat(Qt.AutoText)
        self.label_textJosCercMijloc_4.setScaledContents(False)
        self.label_textJosCercMijloc_4.setAlignment(Qt.AlignCenter)
        self.label_textJosCercMijloc_4.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_textJosCercMijloc_4)


        self.horizontalLayout_14.addWidget(self.frame_cercMijloc_4)

        self.stackedWidget_3.addWidget(self.page_MaiMultiClientiGasiti)
        self.page_Blank = QWidget()
        self.page_Blank.setObjectName(u"page_Blank")
        self.stackedWidget_3.addWidget(self.page_Blank)

        self.horizontalLayout_7.addWidget(self.stackedWidget_3)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.frame = QFrame(self.page_cautaClient)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tableWidget_4 = QTableWidget(self.frame)
        if (self.tableWidget_4.columnCount() < 9):
            self.tableWidget_4.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setMinimumSize(QSize(1000, 0))
        self.tableWidget_4.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_4.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_4.setFrameShape(QFrame.NoFrame)
        self.tableWidget_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_4.setAutoScrollMargin(0)
        self.tableWidget_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_4.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_4.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_4.setGridStyle(Qt.SolidLine)
        self.tableWidget_4.setSortingEnabled(True)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_4.verticalHeader().setVisible(False)

        self.horizontalLayout_15.addWidget(self.tableWidget_4)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_butoaneClientGasit_2 = QFrame(self.page_cautaClient)
        self.frame_butoaneClientGasit_2.setObjectName(u"frame_butoaneClientGasit_2")
        self.frame_butoaneClientGasit_2.setMinimumSize(QSize(1024, 50))
        self.frame_butoaneClientGasit_2.setMaximumSize(QSize(16777215, 50))
        self.frame_butoaneClientGasit_2.setFrameShape(QFrame.StyledPanel)
        self.frame_butoaneClientGasit_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_butoaneClientGasit_2)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.pushButton_backFromClientGasit = QPushButton(self.frame_butoaneClientGasit_2)
        self.pushButton_backFromClientGasit.setObjectName(u"pushButton_backFromClientGasit")
        self.pushButton_backFromClientGasit.setMinimumSize(QSize(30, 30))
        self.pushButton_backFromClientGasit.setMaximumSize(QSize(30, 30))
        self.pushButton_backFromClientGasit.setFont(font5)
        self.pushButton_backFromClientGasit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_backFromClientGasit.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_backFromClientGasit.setFlat(False)

        self.horizontalLayout_29.addWidget(self.pushButton_backFromClientGasit)

        self.pushButton_genereazaContractClientGasit = QPushButton(self.frame_butoaneClientGasit_2)
        self.pushButton_genereazaContractClientGasit.setObjectName(u"pushButton_genereazaContractClientGasit")
        self.pushButton_genereazaContractClientGasit.setMinimumSize(QSize(330, 28))
        self.pushButton_genereazaContractClientGasit.setMaximumSize(QSize(330, 35))
        self.pushButton_genereazaContractClientGasit.setFont(font5)
        self.pushButton_genereazaContractClientGasit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_genereazaContractClientGasit.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_genereazaContractClientGasit.setFlat(False)

        self.horizontalLayout_29.addWidget(self.pushButton_genereazaContractClientGasit)


        self.verticalLayout_6.addWidget(self.frame_butoaneClientGasit_2)

        self.stackedWidget.addWidget(self.page_cautaClient)
        self.page_contracteAproapeDeTermen = QWidget()
        self.page_contracteAproapeDeTermen.setObjectName(u"page_contracteAproapeDeTermen")
        self.page_contracteAproapeDeTermen.setMinimumSize(QSize(1200, 800))
        self.page_contracteAproapeDeTermen.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_45 = QHBoxLayout(self.page_contracteAproapeDeTermen)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.page_contracteAproapeDeTermen)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_32)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_32)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_cercMijloc_10 = QFrame(self.frame_12)
        self.frame_cercMijloc_10.setObjectName(u"frame_cercMijloc_10")
        self.frame_cercMijloc_10.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc_10.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc_10.setStyleSheet(u"QFrame{\n"
"	border:5px solid  rgb(234, 107, 107);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_10.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_cercMijloc_10)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_10 = QLabel(self.frame_cercMijloc_10)
        self.label_textSusCercMijloc_10.setObjectName(u"label_textSusCercMijloc_10")
        self.label_textSusCercMijloc_10.setMinimumSize(QSize(0, 30))
        self.label_textSusCercMijloc_10.setMaximumSize(QSize(16777215, 30))
        self.label_textSusCercMijloc_10.setFont(font6)
        self.label_textSusCercMijloc_10.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_10.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-top:10px;")
        self.label_textSusCercMijloc_10.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_10.setScaledContents(False)
        self.label_textSusCercMijloc_10.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_10.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_textSusCercMijloc_10)

        self.scrollArea = QScrollArea(self.frame_cercMijloc_10)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(220, 90))
        self.scrollArea.setStyleSheet(u"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	\n"
"	background-color: rgb(234, 107, 107);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" Q"
                        "ScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 325, 75))
        self.verticalLayout_30 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_numarCercMijloc_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_numarCercMijloc_7.setObjectName(u"label_numarCercMijloc_7")
        font11 = QFont()
        font11.setFamily(u"Roboto Thin")
        font11.setPointSize(30)
        self.label_numarCercMijloc_7.setFont(font11)
        self.label_numarCercMijloc_7.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_7.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);\n"
"padding-left:2px;\n"
"padding-right:2px;")
        self.label_numarCercMijloc_7.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_7.setScaledContents(False)
        self.label_numarCercMijloc_7.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_7.setWordWrap(False)

        self.verticalLayout_30.addWidget(self.label_numarCercMijloc_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea)

        self.label_textJosCercMijloc_9 = QLabel(self.frame_cercMijloc_10)
        self.label_textJosCercMijloc_9.setObjectName(u"label_textJosCercMijloc_9")
        self.label_textJosCercMijloc_9.setMinimumSize(QSize(0, 60))
        self.label_textJosCercMijloc_9.setMaximumSize(QSize(16777215, 60))
        self.label_textJosCercMijloc_9.setFont(font6)
        self.label_textJosCercMijloc_9.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercMijloc_9.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-bottom: 20px;")
        self.label_textJosCercMijloc_9.setTextFormat(Qt.AutoText)
        self.label_textJosCercMijloc_9.setScaledContents(False)
        self.label_textJosCercMijloc_9.setAlignment(Qt.AlignCenter)
        self.label_textJosCercMijloc_9.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_textJosCercMijloc_9)


        self.horizontalLayout_6.addWidget(self.frame_cercMijloc_10)

        self.frame_cercMijloc_6 = QFrame(self.frame_12)
        self.frame_cercMijloc_6.setObjectName(u"frame_cercMijloc_6")
        self.frame_cercMijloc_6.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc_6.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc_6.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(244, 163, 0);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_6.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_cercMijloc_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_textSusCercMijloc_6 = QLabel(self.frame_cercMijloc_6)
        self.label_textSusCercMijloc_6.setObjectName(u"label_textSusCercMijloc_6")
        self.label_textSusCercMijloc_6.setMinimumSize(QSize(0, 30))
        self.label_textSusCercMijloc_6.setMaximumSize(QSize(16777215, 30))
        self.label_textSusCercMijloc_6.setFont(font6)
        self.label_textSusCercMijloc_6.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_6.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-top:10px;")
        self.label_textSusCercMijloc_6.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_6.setScaledContents(False)
        self.label_textSusCercMijloc_6.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_6.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_textSusCercMijloc_6)

        self.scrollArea_2 = QScrollArea(self.frame_cercMijloc_6)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(220, 90))
        self.scrollArea_2.setStyleSheet(u"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	background-color: rgb(244, 163, 0);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBa"
                        "r::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 325, 75))
        self.verticalLayout_31 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_numarCercMijloc_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_numarCercMijloc_11.setObjectName(u"label_numarCercMijloc_11")
        self.label_numarCercMijloc_11.setFont(font11)
        self.label_numarCercMijloc_11.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_11.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);\n"
"padding-left:2px;\n"
"padding-right:2px;")
        self.label_numarCercMijloc_11.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_11.setScaledContents(False)
        self.label_numarCercMijloc_11.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_11.setWordWrap(False)

        self.verticalLayout_31.addWidget(self.label_numarCercMijloc_11)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.label_textJosCercMijloc_5 = QLabel(self.frame_cercMijloc_6)
        self.label_textJosCercMijloc_5.setObjectName(u"label_textJosCercMijloc_5")
        self.label_textJosCercMijloc_5.setMinimumSize(QSize(0, 60))
        self.label_textJosCercMijloc_5.setMaximumSize(QSize(16777215, 60))
        self.label_textJosCercMijloc_5.setFont(font6)
        self.label_textJosCercMijloc_5.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercMijloc_5.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-bottom: 20px;")
        self.label_textJosCercMijloc_5.setTextFormat(Qt.AutoText)
        self.label_textJosCercMijloc_5.setScaledContents(False)
        self.label_textJosCercMijloc_5.setAlignment(Qt.AlignCenter)
        self.label_textJosCercMijloc_5.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_textJosCercMijloc_5)


        self.horizontalLayout_6.addWidget(self.frame_cercMijloc_6)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_32)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_cercMijloc_11 = QFrame(self.frame_13)
        self.frame_cercMijloc_11.setObjectName(u"frame_cercMijloc_11")
        self.frame_cercMijloc_11.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc_11.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc_11.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(26, 155, 226);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_11.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_cercMijloc_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_textSusCercMijloc_11 = QLabel(self.frame_cercMijloc_11)
        self.label_textSusCercMijloc_11.setObjectName(u"label_textSusCercMijloc_11")
        self.label_textSusCercMijloc_11.setMinimumSize(QSize(0, 30))
        self.label_textSusCercMijloc_11.setMaximumSize(QSize(16777215, 30))
        self.label_textSusCercMijloc_11.setFont(font6)
        self.label_textSusCercMijloc_11.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_11.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-top:10px;")
        self.label_textSusCercMijloc_11.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_11.setScaledContents(False)
        self.label_textSusCercMijloc_11.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_11.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_textSusCercMijloc_11)

        self.scrollArea_3 = QScrollArea(self.frame_cercMijloc_11)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMaximumSize(QSize(220, 90))
        self.scrollArea_3.setStyleSheet(u"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	background-color: rgb(26, 155, 226);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollB"
                        "ar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 325, 75))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_numarCercMijloc_12 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_numarCercMijloc_12.setObjectName(u"label_numarCercMijloc_12")
        self.label_numarCercMijloc_12.setFont(font11)
        self.label_numarCercMijloc_12.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_12.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);\n"
"padding-left:2px;\n"
"padding-right:2px;")
        self.label_numarCercMijloc_12.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_12.setScaledContents(False)
        self.label_numarCercMijloc_12.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_12.setWordWrap(False)

        self.verticalLayout_32.addWidget(self.label_numarCercMijloc_12)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_14.addWidget(self.scrollArea_3)

        self.label_textJosCercMijloc_10 = QLabel(self.frame_cercMijloc_11)
        self.label_textJosCercMijloc_10.setObjectName(u"label_textJosCercMijloc_10")
        self.label_textJosCercMijloc_10.setMinimumSize(QSize(0, 60))
        self.label_textJosCercMijloc_10.setMaximumSize(QSize(16777215, 60))
        self.label_textJosCercMijloc_10.setFont(font6)
        self.label_textJosCercMijloc_10.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercMijloc_10.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-bottom: 20px;")
        self.label_textJosCercMijloc_10.setTextFormat(Qt.AutoText)
        self.label_textJosCercMijloc_10.setScaledContents(False)
        self.label_textJosCercMijloc_10.setAlignment(Qt.AlignCenter)
        self.label_textJosCercMijloc_10.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_textJosCercMijloc_10)


        self.horizontalLayout_12.addWidget(self.frame_cercMijloc_11)

        self.frame_cercMijloc_12 = QFrame(self.frame_13)
        self.frame_cercMijloc_12.setObjectName(u"frame_cercMijloc_12")
        self.frame_cercMijloc_12.setMinimumSize(QSize(250, 250))
        self.frame_cercMijloc_12.setMaximumSize(QSize(250, 250))
        self.frame_cercMijloc_12.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(60,231,195);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_12.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_cercMijloc_12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_textSusCercMijloc_14 = QLabel(self.frame_cercMijloc_12)
        self.label_textSusCercMijloc_14.setObjectName(u"label_textSusCercMijloc_14")
        self.label_textSusCercMijloc_14.setMinimumSize(QSize(0, 30))
        self.label_textSusCercMijloc_14.setMaximumSize(QSize(16777215, 30))
        self.label_textSusCercMijloc_14.setFont(font6)
        self.label_textSusCercMijloc_14.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_14.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-top:10px;")
        self.label_textSusCercMijloc_14.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_14.setScaledContents(False)
        self.label_textSusCercMijloc_14.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_14.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.label_textSusCercMijloc_14)

        self.scrollArea_4 = QScrollArea(self.frame_cercMijloc_12)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMaximumSize(QSize(220, 90))
        self.scrollArea_4.setStyleSheet(u"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	background-color: rgb(60, 231, 195);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollB"
                        "ar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 325, 75))
        self.verticalLayout_33 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_numarCercMijloc_13 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_numarCercMijloc_13.setObjectName(u"label_numarCercMijloc_13")
        self.label_numarCercMijloc_13.setFont(font11)
        self.label_numarCercMijloc_13.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_13.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);\n"
"padding-left:2px;\n"
"padding-right:2px;")
        self.label_numarCercMijloc_13.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_13.setScaledContents(False)
        self.label_numarCercMijloc_13.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_13.setWordWrap(False)

        self.verticalLayout_33.addWidget(self.label_numarCercMijloc_13)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_24.addWidget(self.scrollArea_4)

        self.label_textJosCercMijloc_11 = QLabel(self.frame_cercMijloc_12)
        self.label_textJosCercMijloc_11.setObjectName(u"label_textJosCercMijloc_11")
        self.label_textJosCercMijloc_11.setMinimumSize(QSize(0, 60))
        self.label_textJosCercMijloc_11.setMaximumSize(QSize(16777215, 60))
        self.label_textJosCercMijloc_11.setFont(font6)
        self.label_textJosCercMijloc_11.setLayoutDirection(Qt.LeftToRight)
        self.label_textJosCercMijloc_11.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);\n"
"padding-bottom: 20px;")
        self.label_textJosCercMijloc_11.setTextFormat(Qt.AutoText)
        self.label_textJosCercMijloc_11.setScaledContents(False)
        self.label_textJosCercMijloc_11.setAlignment(Qt.AlignCenter)
        self.label_textJosCercMijloc_11.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.label_textJosCercMijloc_11)


        self.horizontalLayout_12.addWidget(self.frame_cercMijloc_12)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_35 = QFrame(self.frame_32)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 0))
        self.frame_35.setMaximumSize(QSize(16777215, 16777215))
        self.frame_35.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_maiMultiClientiGasitiOK_2 = QPushButton(self.frame_35)
        self.pushButton_maiMultiClientiGasitiOK_2.setObjectName(u"pushButton_maiMultiClientiGasitiOK_2")
        self.pushButton_maiMultiClientiGasitiOK_2.setMinimumSize(QSize(30, 30))
        self.pushButton_maiMultiClientiGasitiOK_2.setMaximumSize(QSize(30, 30))
        self.pushButton_maiMultiClientiGasitiOK_2.setFont(font5)
        self.pushButton_maiMultiClientiGasitiOK_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_maiMultiClientiGasitiOK_2.setFlat(False)

        self.horizontalLayout_11.addWidget(self.pushButton_maiMultiClientiGasitiOK_2)


        self.verticalLayout_2.addWidget(self.frame_35)


        self.horizontalLayout_45.addWidget(self.frame_32)

        self.stackedWidget.addWidget(self.page_contracteAproapeDeTermen)
        self.page_contracteInTermen = QWidget()
        self.page_contracteInTermen.setObjectName(u"page_contracteInTermen")
        self.page_contracteInTermen.setMinimumSize(QSize(1024, 0))
        self.verticalLayout_16 = QVBoxLayout(self.page_contracteInTermen)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_contracteInTermen)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(1024, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_cercMijloc_8 = QFrame(self.frame_7)
        self.frame_cercMijloc_8.setObjectName(u"frame_cercMijloc_8")
        self.frame_cercMijloc_8.setMinimumSize(QSize(300, 50))
        self.frame_cercMijloc_8.setMaximumSize(QSize(300, 50))
        self.frame_cercMijloc_8.setStyleSheet(u"QFrame{\n"
"	border:3px solid rgb(60,231,195);\n"
"	border-radius:25px;\n"
"}\n"
"QFrame:hover{\n"
"	border:3px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_8.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_cercMijloc_8)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(10, 0, 10, 0)
        self.label_textSusCercMijloc_8 = QLabel(self.frame_cercMijloc_8)
        self.label_textSusCercMijloc_8.setObjectName(u"label_textSusCercMijloc_8")
        self.label_textSusCercMijloc_8.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_8.setFont(font6)
        self.label_textSusCercMijloc_8.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_8.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_8.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_8.setScaledContents(False)
        self.label_textSusCercMijloc_8.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_8.setWordWrap(True)

        self.horizontalLayout_33.addWidget(self.label_textSusCercMijloc_8)

        self.frame_8 = QFrame(self.frame_cercMijloc_8)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(110, 50))
        self.frame_8.setStyleSheet(u"border:none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_numarContractDePrelungit_4 = QLineEdit(self.frame_8)
        self.lineEdit_numarContractDePrelungit_4.setObjectName(u"lineEdit_numarContractDePrelungit_4")
        self.lineEdit_numarContractDePrelungit_4.setMinimumSize(QSize(100, 20))
        self.lineEdit_numarContractDePrelungit_4.setMaximumSize(QSize(100, 30))
        self.lineEdit_numarContractDePrelungit_4.setFont(font7)
        self.lineEdit_numarContractDePrelungit_4.setFrame(True)
        self.lineEdit_numarContractDePrelungit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_numarContractDePrelungit_4.setClearButtonEnabled(False)

        self.horizontalLayout_27.addWidget(self.lineEdit_numarContractDePrelungit_4)


        self.horizontalLayout_33.addWidget(self.frame_8)

        self.frame_37 = QFrame(self.frame_cercMijloc_8)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.pushButton_backToHome_5 = QPushButton(self.frame_37)
        self.pushButton_backToHome_5.setObjectName(u"pushButton_backToHome_5")
        self.pushButton_backToHome_5.setMinimumSize(QSize(30, 30))
        self.pushButton_backToHome_5.setMaximumSize(QSize(30, 30))
        self.pushButton_backToHome_5.setFont(font5)
        self.pushButton_backToHome_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_backToHome_5.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../myAmanet-Manager/env/assets/search-loupe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_backToHome_5.setIcon(icon1)
        self.pushButton_backToHome_5.setFlat(False)

        self.horizontalLayout_28.addWidget(self.pushButton_backToHome_5)


        self.horizontalLayout_33.addWidget(self.frame_37)


        self.verticalLayout_10.addWidget(self.frame_cercMijloc_8)

        self.stackedWidget_4 = QStackedWidget(self.frame_7)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.page_ContracteInTermen = QWidget()
        self.page_ContracteInTermen.setObjectName(u"page_ContracteInTermen")
        self.verticalLayout_5 = QVBoxLayout(self.page_ContracteInTermen)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_ContracteInTermen)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_2 = QPushButton(self.frame_2)
        self.pushButton_goHome_2.setObjectName(u"pushButton_goHome_2")
        self.pushButton_goHome_2.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_2.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_2.setFont(font5)
        self.pushButton_goHome_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_2.setFlat(False)

        self.horizontalLayout_16.addWidget(self.pushButton_goHome_2)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(1000, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_13 = QLabel(self.frame_4)
        self.label_textSusCercMijloc_13.setObjectName(u"label_textSusCercMijloc_13")
        self.label_textSusCercMijloc_13.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_13.setMaximumSize(QSize(1000, 20))
        font12 = QFont()
        font12.setFamily(u"Roboto")
        font12.setPointSize(14)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_textSusCercMijloc_13.setFont(font12)
        self.label_textSusCercMijloc_13.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_13.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_13.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_13.setScaledContents(False)
        self.label_textSusCercMijloc_13.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_13.setWordWrap(True)

        self.horizontalLayout_20.addWidget(self.label_textSusCercMijloc_13)


        self.horizontalLayout_16.addWidget(self.frame_4)

        self.pushButton_goHome_3 = QPushButton(self.frame_2)
        self.pushButton_goHome_3.setObjectName(u"pushButton_goHome_3")
        self.pushButton_goHome_3.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_3.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_3.setFont(font5)
        self.pushButton_goHome_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_3.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_3.setFlat(False)

        self.horizontalLayout_16.addWidget(self.pushButton_goHome_3)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_ContracteInTermen)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tableWidget_contracteInTermen = QTableWidget(self.frame_3)
        if (self.tableWidget_contracteInTermen.columnCount() < 10):
            self.tableWidget_contracteInTermen.setColumnCount(10)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contracteInTermen.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        self.tableWidget_contracteInTermen.setObjectName(u"tableWidget_contracteInTermen")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidget_contracteInTermen.sizePolicy().hasHeightForWidth())
        self.tableWidget_contracteInTermen.setSizePolicy(sizePolicy)
        self.tableWidget_contracteInTermen.setMinimumSize(QSize(1000, 0))
        self.tableWidget_contracteInTermen.setMaximumSize(QSize(1200, 600))
        self.tableWidget_contracteInTermen.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_contracteInTermen.setFrameShape(QFrame.NoFrame)
        self.tableWidget_contracteInTermen.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_contracteInTermen.setAutoScrollMargin(0)
        self.tableWidget_contracteInTermen.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_contracteInTermen.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_contracteInTermen.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_contracteInTermen.setGridStyle(Qt.SolidLine)
        self.tableWidget_contracteInTermen.setSortingEnabled(True)
        self.tableWidget_contracteInTermen.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_contracteInTermen.verticalHeader().setVisible(False)

        self.horizontalLayout_18.addWidget(self.tableWidget_contracteInTermen)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.stackedWidget_4.addWidget(self.page_ContracteInTermen)
        self.page_ContracteInAsteptare = QWidget()
        self.page_ContracteInAsteptare.setObjectName(u"page_ContracteInAsteptare")
        self.verticalLayout_12 = QVBoxLayout(self.page_ContracteInAsteptare)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_ContracteInAsteptare)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 50))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_4 = QPushButton(self.frame_9)
        self.pushButton_goHome_4.setObjectName(u"pushButton_goHome_4")
        self.pushButton_goHome_4.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_4.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_4.setFont(font5)
        self.pushButton_goHome_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_4.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_4.setFlat(False)

        self.horizontalLayout_22.addWidget(self.pushButton_goHome_4)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(1000, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_15 = QLabel(self.frame_10)
        self.label_textSusCercMijloc_15.setObjectName(u"label_textSusCercMijloc_15")
        self.label_textSusCercMijloc_15.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_15.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_15.setFont(font12)
        self.label_textSusCercMijloc_15.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_15.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_15.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_15.setScaledContents(False)
        self.label_textSusCercMijloc_15.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_15.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.label_textSusCercMijloc_15)


        self.horizontalLayout_22.addWidget(self.frame_10)

        self.pushButton_goHome_5 = QPushButton(self.frame_9)
        self.pushButton_goHome_5.setObjectName(u"pushButton_goHome_5")
        self.pushButton_goHome_5.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_5.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_5.setFont(font5)
        self.pushButton_goHome_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_5.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_5.setFlat(False)

        self.horizontalLayout_22.addWidget(self.pushButton_goHome_5)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.page_ContracteInAsteptare)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.tableWidget_contracteInAsteptare = QTableWidget(self.frame_5)
        if (self.tableWidget_contracteInAsteptare.columnCount() < 10):
            self.tableWidget_contracteInAsteptare.setColumnCount(10)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_contracteInAsteptare.setHorizontalHeaderItem(9, __qtablewidgetitem28)
        self.tableWidget_contracteInAsteptare.setObjectName(u"tableWidget_contracteInAsteptare")
        self.tableWidget_contracteInAsteptare.setMinimumSize(QSize(1000, 0))
        self.tableWidget_contracteInAsteptare.setMaximumSize(QSize(1200, 600))
        self.tableWidget_contracteInAsteptare.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_contracteInAsteptare.setFrameShape(QFrame.NoFrame)
        self.tableWidget_contracteInAsteptare.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_contracteInAsteptare.setAutoScrollMargin(0)
        self.tableWidget_contracteInAsteptare.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_contracteInAsteptare.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_contracteInAsteptare.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_contracteInAsteptare.setGridStyle(Qt.SolidLine)
        self.tableWidget_contracteInAsteptare.setSortingEnabled(True)
        self.tableWidget_contracteInAsteptare.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_contracteInAsteptare.verticalHeader().setVisible(False)

        self.horizontalLayout_21.addWidget(self.tableWidget_contracteInAsteptare)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.stackedWidget_4.addWidget(self.page_ContracteInAsteptare)
        self.page_ContracteExpirate = QWidget()
        self.page_ContracteExpirate.setObjectName(u"page_ContracteExpirate")
        self.verticalLayout_20 = QVBoxLayout(self.page_ContracteExpirate)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.page_ContracteExpirate)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 50))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_6 = QPushButton(self.frame_20)
        self.pushButton_goHome_6.setObjectName(u"pushButton_goHome_6")
        self.pushButton_goHome_6.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_6.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_6.setFont(font5)
        self.pushButton_goHome_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_6.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_6.setFlat(False)

        self.horizontalLayout_35.addWidget(self.pushButton_goHome_6)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(1000, 16777215))
        font13 = QFont()
        font13.setPointSize(14)
        font13.setBold(True)
        font13.setWeight(75)
        self.frame_21.setFont(font13)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_17 = QLabel(self.frame_21)
        self.label_textSusCercMijloc_17.setObjectName(u"label_textSusCercMijloc_17")
        self.label_textSusCercMijloc_17.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_17.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_17.setFont(font12)
        self.label_textSusCercMijloc_17.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_17.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_17.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_17.setScaledContents(False)
        self.label_textSusCercMijloc_17.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_17.setWordWrap(True)

        self.horizontalLayout_38.addWidget(self.label_textSusCercMijloc_17)


        self.horizontalLayout_35.addWidget(self.frame_21)

        self.pushButton_goHome_7 = QPushButton(self.frame_20)
        self.pushButton_goHome_7.setObjectName(u"pushButton_goHome_7")
        self.pushButton_goHome_7.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_7.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_7.setFont(font5)
        self.pushButton_goHome_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_7.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_7.setFlat(False)

        self.horizontalLayout_35.addWidget(self.pushButton_goHome_7)


        self.verticalLayout_20.addWidget(self.frame_20)

        self.frame_18 = QFrame(self.page_ContracteExpirate)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.tableWidget_contracteExpirate = QTableWidget(self.frame_18)
        if (self.tableWidget_contracteExpirate.columnCount() < 15):
            self.tableWidget_contracteExpirate.setColumnCount(15)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(6, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(7, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(8, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(9, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(10, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(11, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(12, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(13, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_contracteExpirate.setHorizontalHeaderItem(14, __qtablewidgetitem43)
        self.tableWidget_contracteExpirate.setObjectName(u"tableWidget_contracteExpirate")
        self.tableWidget_contracteExpirate.setMinimumSize(QSize(1000, 0))
        self.tableWidget_contracteExpirate.setMaximumSize(QSize(1200, 600))
        self.tableWidget_contracteExpirate.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_contracteExpirate.setFrameShape(QFrame.NoFrame)
        self.tableWidget_contracteExpirate.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_contracteExpirate.setAutoScrollMargin(0)
        self.tableWidget_contracteExpirate.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_contracteExpirate.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_contracteExpirate.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_contracteExpirate.setGridStyle(Qt.SolidLine)
        self.tableWidget_contracteExpirate.setSortingEnabled(True)
        self.tableWidget_contracteExpirate.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_contracteExpirate.verticalHeader().setVisible(False)

        self.horizontalLayout_31.addWidget(self.tableWidget_contracteExpirate)


        self.verticalLayout_20.addWidget(self.frame_18)

        self.stackedWidget_4.addWidget(self.page_ContracteExpirate)
        self.page_ContracteIncheiate = QWidget()
        self.page_ContracteIncheiate.setObjectName(u"page_ContracteIncheiate")
        self.verticalLayout_21 = QVBoxLayout(self.page_ContracteIncheiate)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.page_ContracteIncheiate)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(16777215, 50))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_8 = QPushButton(self.frame_23)
        self.pushButton_goHome_8.setObjectName(u"pushButton_goHome_8")
        self.pushButton_goHome_8.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_8.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_8.setFont(font5)
        self.pushButton_goHome_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_8.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_8.setFlat(False)

        self.horizontalLayout_40.addWidget(self.pushButton_goHome_8)

        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(1000, 16777215))
        self.frame_24.setFont(font13)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_18 = QLabel(self.frame_24)
        self.label_textSusCercMijloc_18.setObjectName(u"label_textSusCercMijloc_18")
        self.label_textSusCercMijloc_18.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_18.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_18.setFont(font12)
        self.label_textSusCercMijloc_18.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_18.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_18.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_18.setScaledContents(False)
        self.label_textSusCercMijloc_18.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_18.setWordWrap(True)

        self.horizontalLayout_41.addWidget(self.label_textSusCercMijloc_18)


        self.horizontalLayout_40.addWidget(self.frame_24)

        self.pushButton_goHome_9 = QPushButton(self.frame_23)
        self.pushButton_goHome_9.setObjectName(u"pushButton_goHome_9")
        self.pushButton_goHome_9.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_9.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_9.setFont(font5)
        self.pushButton_goHome_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_9.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_9.setFlat(False)

        self.horizontalLayout_40.addWidget(self.pushButton_goHome_9)


        self.verticalLayout_21.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.page_ContracteIncheiate)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.tableWidget_contracteIncheiate = QTableWidget(self.frame_22)
        if (self.tableWidget_contracteIncheiate.columnCount() < 17):
            self.tableWidget_contracteIncheiate.setColumnCount(17)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(6, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(7, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(8, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(9, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(10, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(11, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(12, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(13, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(14, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(15, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_contracteIncheiate.setHorizontalHeaderItem(16, __qtablewidgetitem60)
        self.tableWidget_contracteIncheiate.setObjectName(u"tableWidget_contracteIncheiate")
        self.tableWidget_contracteIncheiate.setMinimumSize(QSize(1000, 0))
        self.tableWidget_contracteIncheiate.setMaximumSize(QSize(1200, 600))
        self.tableWidget_contracteIncheiate.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_contracteIncheiate.setFrameShape(QFrame.NoFrame)
        self.tableWidget_contracteIncheiate.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_contracteIncheiate.setAutoScrollMargin(0)
        self.tableWidget_contracteIncheiate.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_contracteIncheiate.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_contracteIncheiate.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_contracteIncheiate.setGridStyle(Qt.SolidLine)
        self.tableWidget_contracteIncheiate.setSortingEnabled(True)
        self.tableWidget_contracteIncheiate.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_contracteIncheiate.verticalHeader().setVisible(False)

        self.horizontalLayout_39.addWidget(self.tableWidget_contracteIncheiate)


        self.verticalLayout_21.addWidget(self.frame_22)

        self.stackedWidget_4.addWidget(self.page_ContracteIncheiate)
        self.page_ContractePrelungite = QWidget()
        self.page_ContractePrelungite.setObjectName(u"page_ContractePrelungite")
        self.verticalLayout_27 = QVBoxLayout(self.page_ContractePrelungite)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_ContractePrelungite)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_15 = QPushButton(self.frame_6)
        self.pushButton_goHome_15.setObjectName(u"pushButton_goHome_15")
        self.pushButton_goHome_15.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_15.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_15.setFont(font5)
        self.pushButton_goHome_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_15.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_15.setFlat(False)

        self.horizontalLayout_59.addWidget(self.pushButton_goHome_15)

        self.frame_55 = QFrame(self.frame_6)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(1000, 16777215))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_26 = QLabel(self.frame_55)
        self.label_textSusCercMijloc_26.setObjectName(u"label_textSusCercMijloc_26")
        self.label_textSusCercMijloc_26.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_26.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_26.setFont(font12)
        self.label_textSusCercMijloc_26.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_26.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_26.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_26.setScaledContents(False)
        self.label_textSusCercMijloc_26.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_26.setWordWrap(True)

        self.horizontalLayout_60.addWidget(self.label_textSusCercMijloc_26)


        self.horizontalLayout_59.addWidget(self.frame_55)

        self.pushButton_goHome_16 = QPushButton(self.frame_6)
        self.pushButton_goHome_16.setObjectName(u"pushButton_goHome_16")
        self.pushButton_goHome_16.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_16.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_16.setFont(font5)
        self.pushButton_goHome_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_16.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_16.setFlat(False)

        self.horizontalLayout_59.addWidget(self.pushButton_goHome_16)


        self.verticalLayout_27.addWidget(self.frame_6)

        self.frame_56 = QFrame(self.page_ContractePrelungite)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.tableWidget_contractePrelungite = QTableWidget(self.frame_56)
        if (self.tableWidget_contractePrelungite.columnCount() < 15):
            self.tableWidget_contractePrelungite.setColumnCount(15)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(3, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(5, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(6, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(7, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(8, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(9, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(10, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(11, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(12, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(13, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_contractePrelungite.setHorizontalHeaderItem(14, __qtablewidgetitem75)
        self.tableWidget_contractePrelungite.setObjectName(u"tableWidget_contractePrelungite")
        self.tableWidget_contractePrelungite.setMinimumSize(QSize(1000, 0))
        self.tableWidget_contractePrelungite.setMaximumSize(QSize(1200, 600))
        self.tableWidget_contractePrelungite.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_contractePrelungite.setFrameShape(QFrame.NoFrame)
        self.tableWidget_contractePrelungite.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_contractePrelungite.setAutoScrollMargin(0)
        self.tableWidget_contractePrelungite.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_contractePrelungite.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_contractePrelungite.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_contractePrelungite.setGridStyle(Qt.SolidLine)
        self.tableWidget_contractePrelungite.setSortingEnabled(True)
        self.tableWidget_contractePrelungite.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_contractePrelungite.verticalHeader().setVisible(False)

        self.horizontalLayout_61.addWidget(self.tableWidget_contractePrelungite)


        self.verticalLayout_27.addWidget(self.frame_56)

        self.stackedWidget_4.addWidget(self.page_ContractePrelungite)
        self.page_PrevizualizareContract = QWidget()
        self.page_PrevizualizareContract.setObjectName(u"page_PrevizualizareContract")
        self.verticalLayout_47 = QVBoxLayout(self.page_PrevizualizareContract)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_68 = QFrame(self.page_PrevizualizareContract)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.frame_25 = QFrame(self.frame_68)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(200, 0))
        self.frame_25.setMaximumSize(QSize(400, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_textSusCercMijloc_19 = QLabel(self.frame_25)
        self.label_textSusCercMijloc_19.setObjectName(u"label_textSusCercMijloc_19")
        self.label_textSusCercMijloc_19.setMaximumSize(QSize(16777215, 50))
        font14 = QFont()
        font14.setFamily(u"Roboto Light")
        font14.setPointSize(16)
        self.label_textSusCercMijloc_19.setFont(font14)
        self.label_textSusCercMijloc_19.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_19.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_19.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_19.setScaledContents(False)
        self.label_textSusCercMijloc_19.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_19.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.label_textSusCercMijloc_19)

        self.label_numarCercDreapta_2 = QLabel(self.frame_25)
        self.label_numarCercDreapta_2.setObjectName(u"label_numarCercDreapta_2")
        font15 = QFont()
        font15.setFamily(u"Roboto Light")
        font15.setPointSize(20)
        self.label_numarCercDreapta_2.setFont(font15)
        self.label_numarCercDreapta_2.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_2.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_2.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_2.setScaledContents(False)
        self.label_numarCercDreapta_2.setAlignment(Qt.AlignCenter)
        self.label_numarCercDreapta_2.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.label_numarCercDreapta_2)

        self.label_textSusCercMijloc_20 = QLabel(self.frame_25)
        self.label_textSusCercMijloc_20.setObjectName(u"label_textSusCercMijloc_20")
        self.label_textSusCercMijloc_20.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_20.setFont(font14)
        self.label_textSusCercMijloc_20.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_20.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_20.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_20.setScaledContents(False)
        self.label_textSusCercMijloc_20.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_20.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.label_textSusCercMijloc_20)

        self.label_numarCercDreapta_3 = QLabel(self.frame_25)
        self.label_numarCercDreapta_3.setObjectName(u"label_numarCercDreapta_3")
        self.label_numarCercDreapta_3.setFont(font15)
        self.label_numarCercDreapta_3.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_3.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_3.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_3.setScaledContents(False)
        self.label_numarCercDreapta_3.setAlignment(Qt.AlignCenter)
        self.label_numarCercDreapta_3.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.label_numarCercDreapta_3)


        self.horizontalLayout_72.addWidget(self.frame_25)

        self.frame_66 = QFrame(self.frame_68)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(200, 0))
        self.frame_66.setMaximumSize(QSize(700, 16777215))
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_textSusCercMijloc_44 = QLabel(self.frame_66)
        self.label_textSusCercMijloc_44.setObjectName(u"label_textSusCercMijloc_44")
        self.label_textSusCercMijloc_44.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_44.setFont(font14)
        self.label_textSusCercMijloc_44.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_44.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_44.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_44.setScaledContents(False)
        self.label_textSusCercMijloc_44.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_44.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.label_textSusCercMijloc_44)

        self.label_numarCercDreapta_6 = QLabel(self.frame_66)
        self.label_numarCercDreapta_6.setObjectName(u"label_numarCercDreapta_6")
        self.label_numarCercDreapta_6.setFont(font15)
        self.label_numarCercDreapta_6.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_6.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_6.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_6.setScaledContents(False)
        self.label_numarCercDreapta_6.setAlignment(Qt.AlignCenter)
        self.label_numarCercDreapta_6.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.label_numarCercDreapta_6)

        self.label_textSusCercMijloc_45 = QLabel(self.frame_66)
        self.label_textSusCercMijloc_45.setObjectName(u"label_textSusCercMijloc_45")
        self.label_textSusCercMijloc_45.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_45.setFont(font14)
        self.label_textSusCercMijloc_45.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_45.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_45.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_45.setScaledContents(False)
        self.label_textSusCercMijloc_45.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_45.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.label_textSusCercMijloc_45)

        self.label_numarCercDreapta_5 = QLabel(self.frame_66)
        self.label_numarCercDreapta_5.setObjectName(u"label_numarCercDreapta_5")
        self.label_numarCercDreapta_5.setFont(font15)
        self.label_numarCercDreapta_5.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_5.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_5.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_5.setScaledContents(False)
        self.label_numarCercDreapta_5.setAlignment(Qt.AlignCenter)
        self.label_numarCercDreapta_5.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.label_numarCercDreapta_5)

        self.label_textSusCercMijloc_46 = QLabel(self.frame_66)
        self.label_textSusCercMijloc_46.setObjectName(u"label_textSusCercMijloc_46")
        self.label_textSusCercMijloc_46.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_46.setFont(font14)
        self.label_textSusCercMijloc_46.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_46.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_46.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_46.setScaledContents(False)
        self.label_textSusCercMijloc_46.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_46.setWordWrap(True)

        self.horizontalLayout_43.addWidget(self.label_textSusCercMijloc_46)


        self.horizontalLayout_72.addWidget(self.frame_66)


        self.verticalLayout_47.addWidget(self.frame_68)

        self.frame_67 = QFrame(self.page_PrevizualizareContract)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.frame_31 = QFrame(self.frame_67)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.frame_43 = QFrame(self.frame_31)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_43)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(45, 125, 0, 0)
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(250, 250))
        self.frame_44.setMaximumSize(QSize(250, 250))
        self.frame_44.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(244, 163, 0);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_44)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 20, 0, 0)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(16777215, 100))
        self.frame_45.setStyleSheet(u"border:none;")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(15, -1, -1, -1)
        self.label_textSusCercMijloc_23 = QLabel(self.frame_45)
        self.label_textSusCercMijloc_23.setObjectName(u"label_textSusCercMijloc_23")
        self.label_textSusCercMijloc_23.setMaximumSize(QSize(16777215, 100))
        self.label_textSusCercMijloc_23.setFont(font7)
        self.label_textSusCercMijloc_23.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_23.setStyleSheet(u"border:none;\n"
"color: rgb(244, 163, 0);")
        self.label_textSusCercMijloc_23.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_23.setScaledContents(False)
        self.label_textSusCercMijloc_23.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_23.setWordWrap(True)

        self.horizontalLayout_48.addWidget(self.label_textSusCercMijloc_23)


        self.verticalLayout_25.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(250, 0))
        self.frame_46.setMaximumSize(QSize(250, 30))
        self.frame_46.setStyleSheet(u"border:none;")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_numarContractDePrelungit_7 = QLineEdit(self.frame_46)
        self.lineEdit_numarContractDePrelungit_7.setObjectName(u"lineEdit_numarContractDePrelungit_7")
        self.lineEdit_numarContractDePrelungit_7.setMinimumSize(QSize(100, 20))
        self.lineEdit_numarContractDePrelungit_7.setMaximumSize(QSize(100, 30))
        self.lineEdit_numarContractDePrelungit_7.setFont(font7)
        self.lineEdit_numarContractDePrelungit_7.setFrame(True)
        self.lineEdit_numarContractDePrelungit_7.setAlignment(Qt.AlignCenter)
        self.lineEdit_numarContractDePrelungit_7.setClearButtonEnabled(False)

        self.horizontalLayout_49.addWidget(self.lineEdit_numarContractDePrelungit_7)


        self.verticalLayout_25.addWidget(self.frame_46)

        self.frame_48 = QFrame(self.frame_44)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(250, 0))
        self.frame_48.setMaximumSize(QSize(250, 16777215))
        self.frame_48.setStyleSheet(u"border:none;")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_10 = QPushButton(self.frame_48)
        self.pushButton_goHome_10.setObjectName(u"pushButton_goHome_10")
        self.pushButton_goHome_10.setMinimumSize(QSize(100, 30))
        self.pushButton_goHome_10.setMaximumSize(QSize(100, 30))
        self.pushButton_goHome_10.setFont(font5)
        self.pushButton_goHome_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_10.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_10.setFlat(False)

        self.horizontalLayout_52.addWidget(self.pushButton_goHome_10)


        self.verticalLayout_25.addWidget(self.frame_48)


        self.verticalLayout_40.addWidget(self.frame_44)

        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(16777215, 100))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_47)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 50, 0)
        self.label_textSusCercMijloc_40 = QLabel(self.frame_47)
        self.label_textSusCercMijloc_40.setObjectName(u"label_textSusCercMijloc_40")
        self.label_textSusCercMijloc_40.setMinimumSize(QSize(0, 50))
        self.label_textSusCercMijloc_40.setMaximumSize(QSize(16777215, 60))
        self.label_textSusCercMijloc_40.setFont(font9)
        self.label_textSusCercMijloc_40.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_40.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_40.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_40.setScaledContents(False)
        self.label_textSusCercMijloc_40.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_40.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_textSusCercMijloc_40)

        self.label_numarCercDreapta_21 = QLabel(self.frame_47)
        self.label_numarCercDreapta_21.setObjectName(u"label_numarCercDreapta_21")
        self.label_numarCercDreapta_21.setMinimumSize(QSize(0, 34))
        self.label_numarCercDreapta_21.setMaximumSize(QSize(16777215, 34))
        self.label_numarCercDreapta_21.setFont(font9)
        self.label_numarCercDreapta_21.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_21.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_21.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_21.setScaledContents(False)
        self.label_numarCercDreapta_21.setAlignment(Qt.AlignCenter)
        self.label_numarCercDreapta_21.setWordWrap(True)

        self.verticalLayout_28.addWidget(self.label_numarCercDreapta_21)


        self.verticalLayout_40.addWidget(self.frame_47)


        self.horizontalLayout_50.addWidget(self.frame_43)


        self.horizontalLayout_71.addWidget(self.frame_31)

        self.frame_26 = QFrame(self.frame_67)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(430, 0))
        self.frame_26.setMaximumSize(QSize(430, 16777215))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_26)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setLayoutDirection(Qt.LeftToRight)
        self.frame_27.setStyleSheet(u"QFrame{\n"
"border: 2px solid #3CE7C3;\n"
"border-radius: 20px;\n"
"}")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Plain)
        self.formLayout_3 = QFormLayout(self.frame_27)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_textSusCercMijloc_37 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_37.setObjectName(u"label_textSusCercMijloc_37")
        self.label_textSusCercMijloc_37.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_37.setFont(font9)
        self.label_textSusCercMijloc_37.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_37.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_37.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_37.setScaledContents(False)
        self.label_textSusCercMijloc_37.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_37.setWordWrap(True)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_textSusCercMijloc_37)

        self.label_numarCercDreapta_4 = QLabel(self.frame_27)
        self.label_numarCercDreapta_4.setObjectName(u"label_numarCercDreapta_4")
        self.label_numarCercDreapta_4.setFont(font9)
        self.label_numarCercDreapta_4.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_4.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_4.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_4.setScaledContents(False)
        self.label_numarCercDreapta_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_4.setWordWrap(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.label_numarCercDreapta_4)

        self.label_textSusCercMijloc_36 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_36.setObjectName(u"label_textSusCercMijloc_36")
        self.label_textSusCercMijloc_36.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_36.setFont(font9)
        self.label_textSusCercMijloc_36.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_36.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_36.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_36.setScaledContents(False)
        self.label_textSusCercMijloc_36.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_36.setWordWrap(True)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_textSusCercMijloc_36)

        self.label_numarCercDreapta_17 = QLabel(self.frame_27)
        self.label_numarCercDreapta_17.setObjectName(u"label_numarCercDreapta_17")
        self.label_numarCercDreapta_17.setFont(font9)
        self.label_numarCercDreapta_17.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_17.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_17.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_17.setScaledContents(False)
        self.label_numarCercDreapta_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_17.setWordWrap(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.label_numarCercDreapta_17)

        self.label_textSusCercMijloc_38 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_38.setObjectName(u"label_textSusCercMijloc_38")
        self.label_textSusCercMijloc_38.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_38.setFont(font9)
        self.label_textSusCercMijloc_38.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_38.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_38.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_38.setScaledContents(False)
        self.label_textSusCercMijloc_38.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_38.setWordWrap(True)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_textSusCercMijloc_38)

        self.label_numarCercDreapta_20 = QLabel(self.frame_27)
        self.label_numarCercDreapta_20.setObjectName(u"label_numarCercDreapta_20")
        self.label_numarCercDreapta_20.setFont(font9)
        self.label_numarCercDreapta_20.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_20.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_20.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_20.setScaledContents(False)
        self.label_numarCercDreapta_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_20.setWordWrap(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.label_numarCercDreapta_20)

        self.label_textSusCercMijloc_34 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_34.setObjectName(u"label_textSusCercMijloc_34")
        self.label_textSusCercMijloc_34.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_34.setFont(font9)
        self.label_textSusCercMijloc_34.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_34.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_34.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_34.setScaledContents(False)
        self.label_textSusCercMijloc_34.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_34.setWordWrap(True)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_textSusCercMijloc_34)

        self.label_numarCercDreapta_19 = QLabel(self.frame_27)
        self.label_numarCercDreapta_19.setObjectName(u"label_numarCercDreapta_19")
        self.label_numarCercDreapta_19.setFont(font9)
        self.label_numarCercDreapta_19.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_19.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_19.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_19.setScaledContents(False)
        self.label_numarCercDreapta_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_19.setWordWrap(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.label_numarCercDreapta_19)

        self.label_textSusCercMijloc_33 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_33.setObjectName(u"label_textSusCercMijloc_33")
        self.label_textSusCercMijloc_33.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_33.setFont(font9)
        self.label_textSusCercMijloc_33.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_33.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_33.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_33.setScaledContents(False)
        self.label_textSusCercMijloc_33.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_33.setWordWrap(True)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_textSusCercMijloc_33)

        self.label_numarCercDreapta_16 = QLabel(self.frame_27)
        self.label_numarCercDreapta_16.setObjectName(u"label_numarCercDreapta_16")
        self.label_numarCercDreapta_16.setFont(font9)
        self.label_numarCercDreapta_16.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_16.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_16.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_16.setScaledContents(False)
        self.label_numarCercDreapta_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_16.setWordWrap(True)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.label_numarCercDreapta_16)

        self.label_textSusCercMijloc_39 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_39.setObjectName(u"label_textSusCercMijloc_39")
        self.label_textSusCercMijloc_39.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_39.setFont(font9)
        self.label_textSusCercMijloc_39.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_39.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_39.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_39.setScaledContents(False)
        self.label_textSusCercMijloc_39.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_39.setWordWrap(True)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_textSusCercMijloc_39)

        self.label_numarCercDreapta_18 = QLabel(self.frame_27)
        self.label_numarCercDreapta_18.setObjectName(u"label_numarCercDreapta_18")
        self.label_numarCercDreapta_18.setFont(font9)
        self.label_numarCercDreapta_18.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_18.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_18.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_18.setScaledContents(False)
        self.label_numarCercDreapta_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_18.setWordWrap(True)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.label_numarCercDreapta_18)

        self.label_textSusCercMijloc_35 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_35.setObjectName(u"label_textSusCercMijloc_35")
        self.label_textSusCercMijloc_35.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_35.setFont(font9)
        self.label_textSusCercMijloc_35.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_35.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_35.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_35.setScaledContents(False)
        self.label_textSusCercMijloc_35.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_35.setWordWrap(True)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_textSusCercMijloc_35)

        self.label_numarCercDreapta_11 = QLabel(self.frame_27)
        self.label_numarCercDreapta_11.setObjectName(u"label_numarCercDreapta_11")
        self.label_numarCercDreapta_11.setFont(font9)
        self.label_numarCercDreapta_11.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_11.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_11.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_11.setScaledContents(False)
        self.label_numarCercDreapta_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_11.setWordWrap(True)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.label_numarCercDreapta_11)

        self.label_textSusCercMijloc_21 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_21.setObjectName(u"label_textSusCercMijloc_21")
        self.label_textSusCercMijloc_21.setMinimumSize(QSize(0, 50))
        self.label_textSusCercMijloc_21.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_21.setFont(font9)
        self.label_textSusCercMijloc_21.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_21.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_21.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_21.setScaledContents(False)
        self.label_textSusCercMijloc_21.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_21.setWordWrap(True)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_textSusCercMijloc_21)

        self.scrollArea_5 = QScrollArea(self.frame_27)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setMinimumSize(QSize(0, 50))
        self.scrollArea_5.setMaximumSize(QSize(220, 50))
        self.scrollArea_5.setFont(font7)
        self.scrollArea_5.setStyleSheet(u"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScroll"
                        "Bar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 354, 35))
        self.scrollAreaWidgetContents_5.setMaximumSize(QSize(16777215, 90))
        self.scrollAreaWidgetContents_5.setStyleSheet(u"border:none;")
        self.verticalLayout_36 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_numarCercMijloc_9 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_numarCercMijloc_9.setObjectName(u"label_numarCercMijloc_9")
        self.label_numarCercMijloc_9.setFont(font14)
        self.label_numarCercMijloc_9.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_9.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);\n"
"padding-left:2px;\n"
"padding-right:2px;")
        self.label_numarCercMijloc_9.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_9.setScaledContents(False)
        self.label_numarCercMijloc_9.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_9.setWordWrap(False)

        self.verticalLayout_36.addWidget(self.label_numarCercMijloc_9)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.scrollArea_5)

        self.label_textSusCercMijloc_28 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_28.setObjectName(u"label_textSusCercMijloc_28")
        self.label_textSusCercMijloc_28.setMinimumSize(QSize(0, 50))
        self.label_textSusCercMijloc_28.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_28.setFont(font9)
        self.label_textSusCercMijloc_28.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_28.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_28.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_28.setScaledContents(False)
        self.label_textSusCercMijloc_28.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_28.setWordWrap(True)

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_textSusCercMijloc_28)

        self.scrollArea_6 = QScrollArea(self.frame_27)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 50))
        self.scrollArea_6.setMaximumSize(QSize(220, 50))
        self.scrollArea_6.setFont(font7)
        self.scrollArea_6.setStyleSheet(u"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScroll"
                        "Bar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.scrollArea_6.setFrameShape(QFrame.NoFrame)
        self.scrollArea_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 384, 35))
        self.scrollAreaWidgetContents_6.setMaximumSize(QSize(16777215, 90))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"border:none;")
        self.verticalLayout_39 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_numarCercMijloc_10 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_numarCercMijloc_10.setObjectName(u"label_numarCercMijloc_10")
        self.label_numarCercMijloc_10.setFont(font14)
        self.label_numarCercMijloc_10.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercMijloc_10.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);\n"
"padding-left:2px;\n"
"padding-right:2px;")
        self.label_numarCercMijloc_10.setTextFormat(Qt.AutoText)
        self.label_numarCercMijloc_10.setScaledContents(False)
        self.label_numarCercMijloc_10.setAlignment(Qt.AlignCenter)
        self.label_numarCercMijloc_10.setWordWrap(False)

        self.verticalLayout_39.addWidget(self.label_numarCercMijloc_10)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.scrollArea_6)

        self.label_textSusCercMijloc_29 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_29.setObjectName(u"label_textSusCercMijloc_29")
        self.label_textSusCercMijloc_29.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_29.setFont(font9)
        self.label_textSusCercMijloc_29.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_29.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_29.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_29.setScaledContents(False)
        self.label_textSusCercMijloc_29.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_29.setWordWrap(True)

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.label_textSusCercMijloc_29)

        self.label_numarCercDreapta_12 = QLabel(self.frame_27)
        self.label_numarCercDreapta_12.setObjectName(u"label_numarCercDreapta_12")
        self.label_numarCercDreapta_12.setFont(font9)
        self.label_numarCercDreapta_12.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_12.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_12.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_12.setScaledContents(False)
        self.label_numarCercDreapta_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_12.setWordWrap(True)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.label_numarCercDreapta_12)

        self.label_textSusCercMijloc_30 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_30.setObjectName(u"label_textSusCercMijloc_30")
        self.label_textSusCercMijloc_30.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_30.setFont(font9)
        self.label_textSusCercMijloc_30.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_30.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_30.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_30.setScaledContents(False)
        self.label_textSusCercMijloc_30.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_30.setWordWrap(True)

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.label_textSusCercMijloc_30)

        self.label_numarCercDreapta_13 = QLabel(self.frame_27)
        self.label_numarCercDreapta_13.setObjectName(u"label_numarCercDreapta_13")
        self.label_numarCercDreapta_13.setFont(font9)
        self.label_numarCercDreapta_13.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_13.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_13.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_13.setScaledContents(False)
        self.label_numarCercDreapta_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_13.setWordWrap(True)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.label_numarCercDreapta_13)

        self.label_textSusCercMijloc_41 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_41.setObjectName(u"label_textSusCercMijloc_41")
        self.label_textSusCercMijloc_41.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_41.setFont(font9)
        self.label_textSusCercMijloc_41.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_41.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_41.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_41.setScaledContents(False)
        self.label_textSusCercMijloc_41.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_41.setWordWrap(True)

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.label_textSusCercMijloc_41)

        self.label_numarCercDreapta_22 = QLabel(self.frame_27)
        self.label_numarCercDreapta_22.setObjectName(u"label_numarCercDreapta_22")
        self.label_numarCercDreapta_22.setFont(font9)
        self.label_numarCercDreapta_22.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_22.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_22.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_22.setScaledContents(False)
        self.label_numarCercDreapta_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_22.setWordWrap(True)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.label_numarCercDreapta_22)

        self.label_textSusCercMijloc_31 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_31.setObjectName(u"label_textSusCercMijloc_31")
        self.label_textSusCercMijloc_31.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_31.setFont(font9)
        self.label_textSusCercMijloc_31.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_31.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_31.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_31.setScaledContents(False)
        self.label_textSusCercMijloc_31.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_31.setWordWrap(True)

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.label_textSusCercMijloc_31)

        self.label_numarCercDreapta_14 = QLabel(self.frame_27)
        self.label_numarCercDreapta_14.setObjectName(u"label_numarCercDreapta_14")
        self.label_numarCercDreapta_14.setFont(font9)
        self.label_numarCercDreapta_14.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_14.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_14.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_14.setScaledContents(False)
        self.label_numarCercDreapta_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_14.setWordWrap(True)

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.label_numarCercDreapta_14)

        self.label_textSusCercMijloc_32 = QLabel(self.frame_27)
        self.label_textSusCercMijloc_32.setObjectName(u"label_textSusCercMijloc_32")
        self.label_textSusCercMijloc_32.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_32.setFont(font9)
        self.label_textSusCercMijloc_32.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_32.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_32.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_32.setScaledContents(False)
        self.label_textSusCercMijloc_32.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_32.setWordWrap(True)

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.label_textSusCercMijloc_32)

        self.label_numarCercDreapta_15 = QLabel(self.frame_27)
        self.label_numarCercDreapta_15.setObjectName(u"label_numarCercDreapta_15")
        self.label_numarCercDreapta_15.setFont(font9)
        self.label_numarCercDreapta_15.setLayoutDirection(Qt.LeftToRight)
        self.label_numarCercDreapta_15.setStyleSheet(u"border:none;\n"
"color:rgb(220,220,220);")
        self.label_numarCercDreapta_15.setTextFormat(Qt.AutoText)
        self.label_numarCercDreapta_15.setScaledContents(False)
        self.label_numarCercDreapta_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_numarCercDreapta_15.setWordWrap(True)

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.label_numarCercDreapta_15)


        self.verticalLayout_22.addWidget(self.frame_27)


        self.horizontalLayout_71.addWidget(self.frame_26)

        self.frame_34 = QFrame(self.frame_67)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(250, 250))
        self.frame_36.setMaximumSize(QSize(250, 250))
        self.frame_36.setStyleSheet(u"QFrame{\n"
"	border:5px solid rgb(244, 163, 0);\n"
"	border-radius:125px;\n"
"}\n"
"QFrame:hover{\n"
"	border:5px solid rgb(105,95,148);\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_36)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.frame_36)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 100))
        self.frame_41.setStyleSheet(u"border:none;")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(30, -1, 30, -1)
        self.label_textSusCercMijloc_22 = QLabel(self.frame_41)
        self.label_textSusCercMijloc_22.setObjectName(u"label_textSusCercMijloc_22")
        self.label_textSusCercMijloc_22.setMaximumSize(QSize(16777215, 100))
        self.label_textSusCercMijloc_22.setFont(font7)
        self.label_textSusCercMijloc_22.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_22.setStyleSheet(u"border:none;\n"
"color: rgb(244, 163, 0);")
        self.label_textSusCercMijloc_22.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_22.setScaledContents(False)
        self.label_textSusCercMijloc_22.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_22.setWordWrap(True)

        self.horizontalLayout_47.addWidget(self.label_textSusCercMijloc_22)


        self.verticalLayout_23.addWidget(self.frame_41)

        self.frame_39 = QFrame(self.frame_36)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(250, 0))
        self.frame_39.setMaximumSize(QSize(250, 30))
        self.frame_39.setStyleSheet(u"border:none;")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_numarContractDePrelungit_6 = QLineEdit(self.frame_39)
        self.lineEdit_numarContractDePrelungit_6.setObjectName(u"lineEdit_numarContractDePrelungit_6")
        self.lineEdit_numarContractDePrelungit_6.setMinimumSize(QSize(100, 20))
        self.lineEdit_numarContractDePrelungit_6.setMaximumSize(QSize(100, 30))
        self.lineEdit_numarContractDePrelungit_6.setFont(font7)
        self.lineEdit_numarContractDePrelungit_6.setFrame(True)
        self.lineEdit_numarContractDePrelungit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_numarContractDePrelungit_6.setClearButtonEnabled(False)

        self.horizontalLayout_46.addWidget(self.lineEdit_numarContractDePrelungit_6)


        self.verticalLayout_23.addWidget(self.frame_39)


        self.horizontalLayout_51.addWidget(self.frame_36)


        self.horizontalLayout_71.addWidget(self.frame_34)


        self.verticalLayout_47.addWidget(self.frame_67)

        self.stackedWidget_4.addWidget(self.page_PrevizualizareContract)

        self.verticalLayout_10.addWidget(self.stackedWidget_4)


        self.verticalLayout_16.addWidget(self.frame_7)

        self.frame_42 = QFrame(self.page_contracteInTermen)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.pushButton_goHome = QPushButton(self.frame_42)
        self.pushButton_goHome.setObjectName(u"pushButton_goHome")
        self.pushButton_goHome.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome.setFont(font5)
        self.pushButton_goHome.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome.setFlat(False)

        self.horizontalLayout_34.addWidget(self.pushButton_goHome)

        self.pushButton_incheieContract_6 = QPushButton(self.frame_42)
        self.pushButton_incheieContract_6.setObjectName(u"pushButton_incheieContract_6")
        self.pushButton_incheieContract_6.setMinimumSize(QSize(165, 28))
        self.pushButton_incheieContract_6.setMaximumSize(QSize(165, 35))
        self.pushButton_incheieContract_6.setFont(font5)
        self.pushButton_incheieContract_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_incheieContract_6.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_incheieContract_6.setFlat(False)

        self.horizontalLayout_34.addWidget(self.pushButton_incheieContract_6)

        self.pushButton_incheieContract_8 = QPushButton(self.frame_42)
        self.pushButton_incheieContract_8.setObjectName(u"pushButton_incheieContract_8")
        self.pushButton_incheieContract_8.setMinimumSize(QSize(165, 28))
        self.pushButton_incheieContract_8.setMaximumSize(QSize(165, 35))
        self.pushButton_incheieContract_8.setFont(font5)
        self.pushButton_incheieContract_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_incheieContract_8.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_incheieContract_8.setFlat(False)

        self.horizontalLayout_34.addWidget(self.pushButton_incheieContract_8)

        self.pushButton_incheieContract_7 = QPushButton(self.frame_42)
        self.pushButton_incheieContract_7.setObjectName(u"pushButton_incheieContract_7")
        self.pushButton_incheieContract_7.setMinimumSize(QSize(165, 28))
        self.pushButton_incheieContract_7.setMaximumSize(QSize(165, 35))
        self.pushButton_incheieContract_7.setFont(font5)
        self.pushButton_incheieContract_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_incheieContract_7.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_incheieContract_7.setFlat(False)

        self.horizontalLayout_34.addWidget(self.pushButton_incheieContract_7)

        self.pushButton_finalizareIncheiereContract = QPushButton(self.frame_42)
        self.pushButton_finalizareIncheiereContract.setObjectName(u"pushButton_finalizareIncheiereContract")
        self.pushButton_finalizareIncheiereContract.setMinimumSize(QSize(165, 28))
        self.pushButton_finalizareIncheiereContract.setMaximumSize(QSize(165, 35))
        self.pushButton_finalizareIncheiereContract.setFont(font5)
        self.pushButton_finalizareIncheiereContract.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareIncheiereContract.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_finalizareIncheiereContract.setFlat(False)

        self.horizontalLayout_34.addWidget(self.pushButton_finalizareIncheiereContract)

        self.pushButton_lichideazaContractCuTermenDepasit = QPushButton(self.frame_42)
        self.pushButton_lichideazaContractCuTermenDepasit.setObjectName(u"pushButton_lichideazaContractCuTermenDepasit")
        self.pushButton_lichideazaContractCuTermenDepasit.setMinimumSize(QSize(320, 28))
        self.pushButton_lichideazaContractCuTermenDepasit.setMaximumSize(QSize(320, 35))
        self.pushButton_lichideazaContractCuTermenDepasit.setFont(font5)
        self.pushButton_lichideazaContractCuTermenDepasit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_lichideazaContractCuTermenDepasit.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_lichideazaContractCuTermenDepasit.setFlat(False)

        self.horizontalLayout_34.addWidget(self.pushButton_lichideazaContractCuTermenDepasit)


        self.verticalLayout_16.addWidget(self.frame_42)

        self.stackedWidget.addWidget(self.page_contracteInTermen)
        self.page_produseInAmanet = QWidget()
        self.page_produseInAmanet.setObjectName(u"page_produseInAmanet")
        self.page_produseInAmanet.setMinimumSize(QSize(1024, 0))
        self.horizontalLayout_57 = QHBoxLayout(self.page_produseInAmanet)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.frame_19 = QFrame(self.page_produseInAmanet)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(1024, 0))
        self.frame_19.setMaximumSize(QSize(16777215, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_19)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_cercMijloc_15 = QFrame(self.frame_19)
        self.frame_cercMijloc_15.setObjectName(u"frame_cercMijloc_15")
        self.frame_cercMijloc_15.setMinimumSize(QSize(300, 50))
        self.frame_cercMijloc_15.setMaximumSize(QSize(300, 50))
        self.frame_cercMijloc_15.setStyleSheet(u"QFrame{\n"
"	border:3px solid rgb(60,231,195);\n"
"	border-radius:25px;\n"
"}\n"
"QFrame:hover{\n"
"	border:3px solid rgb(105,95,148);\n"
"}")
        self.frame_cercMijloc_15.setFrameShape(QFrame.NoFrame)
        self.frame_cercMijloc_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_cercMijloc_15)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(10, 0, 10, 0)
        self.label_textSusCercMijloc_47 = QLabel(self.frame_cercMijloc_15)
        self.label_textSusCercMijloc_47.setObjectName(u"label_textSusCercMijloc_47")
        self.label_textSusCercMijloc_47.setMaximumSize(QSize(16777215, 50))
        self.label_textSusCercMijloc_47.setFont(font6)
        self.label_textSusCercMijloc_47.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_47.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_47.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_47.setScaledContents(False)
        self.label_textSusCercMijloc_47.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_47.setWordWrap(True)

        self.horizontalLayout_44.addWidget(self.label_textSusCercMijloc_47)

        self.frame_29 = QFrame(self.frame_cercMijloc_15)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(110, 50))
        self.frame_29.setStyleSheet(u"border:none;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_numarContractDePrelungit_5 = QLineEdit(self.frame_29)
        self.lineEdit_numarContractDePrelungit_5.setObjectName(u"lineEdit_numarContractDePrelungit_5")
        self.lineEdit_numarContractDePrelungit_5.setMinimumSize(QSize(100, 20))
        self.lineEdit_numarContractDePrelungit_5.setMaximumSize(QSize(100, 30))
        self.lineEdit_numarContractDePrelungit_5.setFont(font7)
        self.lineEdit_numarContractDePrelungit_5.setFrame(True)
        self.lineEdit_numarContractDePrelungit_5.setAlignment(Qt.AlignCenter)
        self.lineEdit_numarContractDePrelungit_5.setClearButtonEnabled(False)

        self.horizontalLayout_73.addWidget(self.lineEdit_numarContractDePrelungit_5)


        self.horizontalLayout_44.addWidget(self.frame_29)

        self.frame_69 = QFrame(self.frame_cercMijloc_15)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.pushButton_backToHome_6 = QPushButton(self.frame_69)
        self.pushButton_backToHome_6.setObjectName(u"pushButton_backToHome_6")
        self.pushButton_backToHome_6.setMinimumSize(QSize(30, 30))
        self.pushButton_backToHome_6.setMaximumSize(QSize(30, 30))
        self.pushButton_backToHome_6.setFont(font5)
        self.pushButton_backToHome_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_backToHome_6.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_backToHome_6.setIcon(icon1)
        self.pushButton_backToHome_6.setFlat(False)

        self.horizontalLayout_74.addWidget(self.pushButton_backToHome_6)


        self.horizontalLayout_44.addWidget(self.frame_69)


        self.verticalLayout_41.addWidget(self.frame_cercMijloc_15)

        self.stackedWidget_5 = QStackedWidget(self.frame_19)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.page_produseInTermen = QWidget()
        self.page_produseInTermen.setObjectName(u"page_produseInTermen")
        self.verticalLayout_37 = QVBoxLayout(self.page_produseInTermen)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.page_produseInTermen)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(16777215, 50))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 20, 0, 0)
        self.pushButton_goHome_11 = QPushButton(self.frame_49)
        self.pushButton_goHome_11.setObjectName(u"pushButton_goHome_11")
        self.pushButton_goHome_11.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_11.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_11.setFont(font5)
        self.pushButton_goHome_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_11.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_11.setFlat(False)

        self.horizontalLayout_53.addWidget(self.pushButton_goHome_11)

        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(1000, 16777215))
        self.frame_50.setFont(font13)
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_24 = QLabel(self.frame_50)
        self.label_textSusCercMijloc_24.setObjectName(u"label_textSusCercMijloc_24")
        self.label_textSusCercMijloc_24.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_24.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_24.setFont(font12)
        self.label_textSusCercMijloc_24.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_24.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_24.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_24.setScaledContents(False)
        self.label_textSusCercMijloc_24.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_24.setWordWrap(True)

        self.horizontalLayout_54.addWidget(self.label_textSusCercMijloc_24)


        self.horizontalLayout_53.addWidget(self.frame_50)

        self.pushButton_goHome_12 = QPushButton(self.frame_49)
        self.pushButton_goHome_12.setObjectName(u"pushButton_goHome_12")
        self.pushButton_goHome_12.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_12.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_12.setFont(font5)
        self.pushButton_goHome_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_12.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_12.setFlat(False)

        self.horizontalLayout_53.addWidget(self.pushButton_goHome_12)


        self.verticalLayout_37.addWidget(self.frame_49)

        self.frame_51 = QFrame(self.page_produseInTermen)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 20, 0, 0)
        self.tableWidget_produseInTermen = QTableWidget(self.frame_51)
        if (self.tableWidget_produseInTermen.columnCount() < 8):
            self.tableWidget_produseInTermen.setColumnCount(8)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(2, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(3, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(4, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(5, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(6, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_produseInTermen.setHorizontalHeaderItem(7, __qtablewidgetitem83)
        self.tableWidget_produseInTermen.setObjectName(u"tableWidget_produseInTermen")
        self.tableWidget_produseInTermen.setMinimumSize(QSize(1000, 0))
        self.tableWidget_produseInTermen.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_produseInTermen.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseInTermen.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseInTermen.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseInTermen.setAutoScrollMargin(0)
        self.tableWidget_produseInTermen.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_produseInTermen.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseInTermen.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseInTermen.setSortingEnabled(True)
        self.tableWidget_produseInTermen.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseInTermen.verticalHeader().setVisible(False)

        self.horizontalLayout_36.addWidget(self.tableWidget_produseInTermen)


        self.verticalLayout_37.addWidget(self.frame_51)

        self.stackedWidget_5.addWidget(self.page_produseInTermen)
        self.page_produseInAsteptare = QWidget()
        self.page_produseInAsteptare.setObjectName(u"page_produseInAsteptare")
        self.verticalLayout_42 = QVBoxLayout(self.page_produseInAsteptare)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_53 = QFrame(self.page_produseInAsteptare)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(16777215, 50))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 20, 0, 0)
        self.pushButton_goHome_13 = QPushButton(self.frame_53)
        self.pushButton_goHome_13.setObjectName(u"pushButton_goHome_13")
        self.pushButton_goHome_13.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_13.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_13.setFont(font5)
        self.pushButton_goHome_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_13.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_13.setFlat(False)

        self.horizontalLayout_55.addWidget(self.pushButton_goHome_13)

        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(1000, 16777215))
        self.frame_54.setFont(font13)
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_25 = QLabel(self.frame_54)
        self.label_textSusCercMijloc_25.setObjectName(u"label_textSusCercMijloc_25")
        self.label_textSusCercMijloc_25.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_25.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_25.setFont(font12)
        self.label_textSusCercMijloc_25.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_25.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_25.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_25.setScaledContents(False)
        self.label_textSusCercMijloc_25.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_25.setWordWrap(True)

        self.horizontalLayout_56.addWidget(self.label_textSusCercMijloc_25)


        self.horizontalLayout_55.addWidget(self.frame_54)

        self.pushButton_goHome_14 = QPushButton(self.frame_53)
        self.pushButton_goHome_14.setObjectName(u"pushButton_goHome_14")
        self.pushButton_goHome_14.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_14.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_14.setFont(font5)
        self.pushButton_goHome_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_14.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_14.setFlat(False)

        self.horizontalLayout_55.addWidget(self.pushButton_goHome_14)


        self.verticalLayout_42.addWidget(self.frame_53)

        self.frame_52 = QFrame(self.page_produseInAsteptare)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 20, 0, 0)
        self.tableWidget_produseInAsteptare = QTableWidget(self.frame_52)
        if (self.tableWidget_produseInAsteptare.columnCount() < 13):
            self.tableWidget_produseInAsteptare.setColumnCount(13)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(2, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(3, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(4, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(5, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(6, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(7, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(8, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(9, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(10, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(11, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_produseInAsteptare.setHorizontalHeaderItem(12, __qtablewidgetitem96)
        self.tableWidget_produseInAsteptare.setObjectName(u"tableWidget_produseInAsteptare")
        self.tableWidget_produseInAsteptare.setMinimumSize(QSize(1000, 0))
        self.tableWidget_produseInAsteptare.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_produseInAsteptare.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseInAsteptare.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseInAsteptare.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseInAsteptare.setAutoScrollMargin(0)
        self.tableWidget_produseInAsteptare.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_produseInAsteptare.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseInAsteptare.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseInAsteptare.setSortingEnabled(True)
        self.tableWidget_produseInAsteptare.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseInAsteptare.verticalHeader().setVisible(False)

        self.horizontalLayout_58.addWidget(self.tableWidget_produseInAsteptare)


        self.verticalLayout_42.addWidget(self.frame_52)

        self.stackedWidget_5.addWidget(self.page_produseInAsteptare)
        self.page_produsePrelungite = QWidget()
        self.page_produsePrelungite.setObjectName(u"page_produsePrelungite")
        self.verticalLayout_44 = QVBoxLayout(self.page_produsePrelungite)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.page_produsePrelungite)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 50))
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 20, 0, 0)
        self.pushButton_goHome_17 = QPushButton(self.frame_57)
        self.pushButton_goHome_17.setObjectName(u"pushButton_goHome_17")
        self.pushButton_goHome_17.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_17.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_17.setFont(font5)
        self.pushButton_goHome_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_17.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_17.setFlat(False)

        self.horizontalLayout_62.addWidget(self.pushButton_goHome_17)

        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(1000, 16777215))
        self.frame_58.setFont(font13)
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_27 = QLabel(self.frame_58)
        self.label_textSusCercMijloc_27.setObjectName(u"label_textSusCercMijloc_27")
        self.label_textSusCercMijloc_27.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_27.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_27.setFont(font12)
        self.label_textSusCercMijloc_27.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_27.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_27.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_27.setScaledContents(False)
        self.label_textSusCercMijloc_27.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_27.setWordWrap(True)

        self.horizontalLayout_63.addWidget(self.label_textSusCercMijloc_27)


        self.horizontalLayout_62.addWidget(self.frame_58)

        self.pushButton_goHome_18 = QPushButton(self.frame_57)
        self.pushButton_goHome_18.setObjectName(u"pushButton_goHome_18")
        self.pushButton_goHome_18.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_18.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_18.setFont(font5)
        self.pushButton_goHome_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_18.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_18.setFlat(False)

        self.horizontalLayout_62.addWidget(self.pushButton_goHome_18)


        self.verticalLayout_44.addWidget(self.frame_57)

        self.frame_59 = QFrame(self.page_produsePrelungite)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 20, 0, 0)
        self.tableWidget_produsePrelungite = QTableWidget(self.frame_59)
        if (self.tableWidget_produsePrelungite.columnCount() < 13):
            self.tableWidget_produsePrelungite.setColumnCount(13)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(0, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(1, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(2, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(4, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(5, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(6, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(7, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(8, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(9, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(10, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(11, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_produsePrelungite.setHorizontalHeaderItem(12, __qtablewidgetitem109)
        self.tableWidget_produsePrelungite.setObjectName(u"tableWidget_produsePrelungite")
        self.tableWidget_produsePrelungite.setMinimumSize(QSize(1000, 0))
        self.tableWidget_produsePrelungite.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_produsePrelungite.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produsePrelungite.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produsePrelungite.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produsePrelungite.setAutoScrollMargin(0)
        self.tableWidget_produsePrelungite.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_produsePrelungite.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produsePrelungite.setGridStyle(Qt.SolidLine)
        self.tableWidget_produsePrelungite.setSortingEnabled(True)
        self.tableWidget_produsePrelungite.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produsePrelungite.verticalHeader().setVisible(False)

        self.horizontalLayout_64.addWidget(self.tableWidget_produsePrelungite)


        self.verticalLayout_44.addWidget(self.frame_59)

        self.stackedWidget_5.addWidget(self.page_produsePrelungite)
        self.page_produseExpirate = QWidget()
        self.page_produseExpirate.setObjectName(u"page_produseExpirate")
        self.verticalLayout_45 = QVBoxLayout(self.page_produseExpirate)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.page_produseExpirate)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(16777215, 50))
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 20, 0, 0)
        self.pushButton_goHome_19 = QPushButton(self.frame_60)
        self.pushButton_goHome_19.setObjectName(u"pushButton_goHome_19")
        self.pushButton_goHome_19.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_19.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_19.setFont(font5)
        self.pushButton_goHome_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_19.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_19.setFlat(False)

        self.horizontalLayout_65.addWidget(self.pushButton_goHome_19)

        self.frame_61 = QFrame(self.frame_60)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMaximumSize(QSize(1000, 16777215))
        self.frame_61.setFont(font13)
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_42 = QLabel(self.frame_61)
        self.label_textSusCercMijloc_42.setObjectName(u"label_textSusCercMijloc_42")
        self.label_textSusCercMijloc_42.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_42.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_42.setFont(font12)
        self.label_textSusCercMijloc_42.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_42.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_42.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_42.setScaledContents(False)
        self.label_textSusCercMijloc_42.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_42.setWordWrap(True)

        self.horizontalLayout_66.addWidget(self.label_textSusCercMijloc_42)


        self.horizontalLayout_65.addWidget(self.frame_61)

        self.pushButton_goHome_20 = QPushButton(self.frame_60)
        self.pushButton_goHome_20.setObjectName(u"pushButton_goHome_20")
        self.pushButton_goHome_20.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_20.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_20.setFont(font5)
        self.pushButton_goHome_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_20.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_20.setFlat(False)

        self.horizontalLayout_65.addWidget(self.pushButton_goHome_20)


        self.verticalLayout_45.addWidget(self.frame_60)

        self.frame_62 = QFrame(self.page_produseExpirate)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 20, 0, 0)
        self.tableWidget_produseExpirate = QTableWidget(self.frame_62)
        if (self.tableWidget_produseExpirate.columnCount() < 13):
            self.tableWidget_produseExpirate.setColumnCount(13)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(0, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(1, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(2, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(3, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(4, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(5, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(6, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(7, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(8, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(9, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(10, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(11, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_produseExpirate.setHorizontalHeaderItem(12, __qtablewidgetitem122)
        self.tableWidget_produseExpirate.setObjectName(u"tableWidget_produseExpirate")
        self.tableWidget_produseExpirate.setMinimumSize(QSize(1000, 0))
        self.tableWidget_produseExpirate.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_produseExpirate.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseExpirate.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseExpirate.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseExpirate.setAutoScrollMargin(0)
        self.tableWidget_produseExpirate.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_produseExpirate.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseExpirate.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseExpirate.setSortingEnabled(True)
        self.tableWidget_produseExpirate.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseExpirate.verticalHeader().setVisible(False)

        self.horizontalLayout_67.addWidget(self.tableWidget_produseExpirate)


        self.verticalLayout_45.addWidget(self.frame_62)

        self.stackedWidget_5.addWidget(self.page_produseExpirate)
        self.page_produseLichidateClient = QWidget()
        self.page_produseLichidateClient.setObjectName(u"page_produseLichidateClient")
        self.verticalLayout_46 = QVBoxLayout(self.page_produseLichidateClient)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(self.page_produseLichidateClient)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMaximumSize(QSize(16777215, 50))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 20, 0, 0)
        self.pushButton_goHome_21 = QPushButton(self.frame_64)
        self.pushButton_goHome_21.setObjectName(u"pushButton_goHome_21")
        self.pushButton_goHome_21.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_21.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_21.setFont(font5)
        self.pushButton_goHome_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_21.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_21.setFlat(False)

        self.horizontalLayout_69.addWidget(self.pushButton_goHome_21)

        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMaximumSize(QSize(1000, 16777215))
        self.frame_65.setFont(font13)
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_43 = QLabel(self.frame_65)
        self.label_textSusCercMijloc_43.setObjectName(u"label_textSusCercMijloc_43")
        self.label_textSusCercMijloc_43.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_43.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_43.setFont(font12)
        self.label_textSusCercMijloc_43.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_43.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_43.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_43.setScaledContents(False)
        self.label_textSusCercMijloc_43.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_43.setWordWrap(True)

        self.horizontalLayout_70.addWidget(self.label_textSusCercMijloc_43)


        self.horizontalLayout_69.addWidget(self.frame_65)

        self.pushButton_goHome_22 = QPushButton(self.frame_64)
        self.pushButton_goHome_22.setObjectName(u"pushButton_goHome_22")
        self.pushButton_goHome_22.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_22.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_22.setFont(font5)
        self.pushButton_goHome_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_22.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_22.setFlat(False)

        self.horizontalLayout_69.addWidget(self.pushButton_goHome_22)


        self.verticalLayout_46.addWidget(self.frame_64)

        self.frame_63 = QFrame(self.page_produseLichidateClient)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 20, 0, 0)
        self.tableWidget_produseLichidateClient = QTableWidget(self.frame_63)
        if (self.tableWidget_produseLichidateClient.columnCount() < 14):
            self.tableWidget_produseLichidateClient.setColumnCount(14)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(0, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(1, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(2, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(3, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(4, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(5, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(6, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(7, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(8, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(9, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(10, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(11, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(12, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient.setHorizontalHeaderItem(13, __qtablewidgetitem136)
        self.tableWidget_produseLichidateClient.setObjectName(u"tableWidget_produseLichidateClient")
        self.tableWidget_produseLichidateClient.setMinimumSize(QSize(1000, 0))
        self.tableWidget_produseLichidateClient.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_produseLichidateClient.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseLichidateClient.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseLichidateClient.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseLichidateClient.setAutoScrollMargin(0)
        self.tableWidget_produseLichidateClient.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_produseLichidateClient.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseLichidateClient.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseLichidateClient.setSortingEnabled(True)
        self.tableWidget_produseLichidateClient.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseLichidateClient.verticalHeader().setVisible(False)

        self.horizontalLayout_68.addWidget(self.tableWidget_produseLichidateClient)


        self.verticalLayout_46.addWidget(self.frame_63)

        self.stackedWidget_5.addWidget(self.page_produseLichidateClient)

        self.verticalLayout_41.addWidget(self.stackedWidget_5)

        self.frame_40 = QFrame(self.frame_19)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(1200, 50))
        self.frame_40.setMaximumSize(QSize(300, 50))
        self.frame_40.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_maiMultiClientiGasitiOK_4 = QPushButton(self.frame_40)
        self.pushButton_maiMultiClientiGasitiOK_4.setObjectName(u"pushButton_maiMultiClientiGasitiOK_4")
        self.pushButton_maiMultiClientiGasitiOK_4.setMinimumSize(QSize(30, 30))
        self.pushButton_maiMultiClientiGasitiOK_4.setMaximumSize(QSize(30, 30))
        self.pushButton_maiMultiClientiGasitiOK_4.setFont(font5)
        self.pushButton_maiMultiClientiGasitiOK_4.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_maiMultiClientiGasitiOK_4.setFlat(False)

        self.horizontalLayout_37.addWidget(self.pushButton_maiMultiClientiGasitiOK_4)


        self.verticalLayout_41.addWidget(self.frame_40)


        self.horizontalLayout_57.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.page_produseInAmanet)
        self.page_gestiuneDeVanzari = QWidget()
        self.page_gestiuneDeVanzari.setObjectName(u"page_gestiuneDeVanzari")
        self.horizontalLayout_88 = QHBoxLayout(self.page_gestiuneDeVanzari)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.frame_71 = QFrame(self.page_gestiuneDeVanzari)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(1200, 0))
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_6 = QStackedWidget(self.frame_71)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.stackedWidget_6.setMinimumSize(QSize(1200, 0))
        self.page_produseFurnizori = QWidget()
        self.page_produseFurnizori.setObjectName(u"page_produseFurnizori")
        self.verticalLayout_50 = QVBoxLayout(self.page_produseFurnizori)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.page_produseFurnizori)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(1200, 60))
        self.frame_74.setMaximumSize(QSize(16777215, 60))
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_74)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_27 = QPushButton(self.frame_74)
        self.pushButton_goHome_27.setObjectName(u"pushButton_goHome_27")
        self.pushButton_goHome_27.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_27.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_27.setFont(font5)
        self.pushButton_goHome_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_27.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_27.setFlat(False)

        self.horizontalLayout_77.addWidget(self.pushButton_goHome_27)

        self.frame_75 = QFrame(self.frame_74)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMaximumSize(QSize(1000, 16777215))
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_75)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_49 = QLabel(self.frame_75)
        self.label_textSusCercMijloc_49.setObjectName(u"label_textSusCercMijloc_49")
        self.label_textSusCercMijloc_49.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_49.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_49.setFont(font12)
        self.label_textSusCercMijloc_49.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_49.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_49.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_49.setScaledContents(False)
        self.label_textSusCercMijloc_49.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_49.setWordWrap(True)

        self.horizontalLayout_78.addWidget(self.label_textSusCercMijloc_49)


        self.horizontalLayout_77.addWidget(self.frame_75)

        self.pushButton_goHome_28 = QPushButton(self.frame_74)
        self.pushButton_goHome_28.setObjectName(u"pushButton_goHome_28")
        self.pushButton_goHome_28.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_28.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_28.setFont(font5)
        self.pushButton_goHome_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_28.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_28.setFlat(False)

        self.horizontalLayout_77.addWidget(self.pushButton_goHome_28)


        self.verticalLayout_50.addWidget(self.frame_74)

        self.frame_82 = QFrame(self.page_produseFurnizori)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(1200, 0))
        self.frame_82.setMaximumSize(QSize(1024, 16777215))
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.frame_detaliiAdaugareProduseFurnizor = QFrame(self.frame_82)
        self.frame_detaliiAdaugareProduseFurnizor.setObjectName(u"frame_detaliiAdaugareProduseFurnizor")
        self.frame_detaliiAdaugareProduseFurnizor.setMinimumSize(QSize(800, 0))
        self.frame_detaliiAdaugareProduseFurnizor.setMaximumSize(QSize(500, 16777215))
        self.frame_detaliiAdaugareProduseFurnizor.setFrameShape(QFrame.NoFrame)
        self.frame_detaliiAdaugareProduseFurnizor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_detaliiAdaugareProduseFurnizor)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_88 = QFrame(self.frame_detaliiAdaugareProduseFurnizor)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(800, 40))
        self.frame_88.setMaximumSize(QSize(16777215, 40))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_84.setSpacing(8)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_dateClient_6 = QLabel(self.frame_88)
        self.label_dateClient_6.setObjectName(u"label_dateClient_6")
        self.label_dateClient_6.setMinimumSize(QSize(200, 30))
        self.label_dateClient_6.setMaximumSize(QSize(220, 30))
        self.label_dateClient_6.setFont(font8)
        self.label_dateClient_6.setStyleSheet(u"color: rgba(255, 170, 0,0.7);")
        self.label_dateClient_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_84.addWidget(self.label_dateClient_6)


        self.verticalLayout_51.addWidget(self.frame_88)

        self.frame_107 = QFrame(self.frame_detaliiAdaugareProduseFurnizor)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMinimumSize(QSize(800, 50))
        self.frame_107.setMaximumSize(QSize(16777215, 50))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.pushButton_goHome_31 = QPushButton(self.frame_107)
        self.pushButton_goHome_31.setObjectName(u"pushButton_goHome_31")
        self.pushButton_goHome_31.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_31.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_31.setFont(font5)
        self.pushButton_goHome_31.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_31.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_31.setFlat(False)

        self.horizontalLayout_85.addWidget(self.pushButton_goHome_31)


        self.verticalLayout_51.addWidget(self.frame_107)

        self.tableWidget_produseLichidateClient_8 = QTableWidget(self.frame_detaliiAdaugareProduseFurnizor)
        if (self.tableWidget_produseLichidateClient_8.columnCount() < 6):
            self.tableWidget_produseLichidateClient_8.setColumnCount(6)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_8.setHorizontalHeaderItem(0, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_8.setHorizontalHeaderItem(1, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_8.setHorizontalHeaderItem(2, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_8.setHorizontalHeaderItem(3, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_8.setHorizontalHeaderItem(4, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_8.setHorizontalHeaderItem(5, __qtablewidgetitem142)
        self.tableWidget_produseLichidateClient_8.setObjectName(u"tableWidget_produseLichidateClient_8")
        self.tableWidget_produseLichidateClient_8.setMinimumSize(QSize(200, 350))
        self.tableWidget_produseLichidateClient_8.setMaximumSize(QSize(16777215, 350))
        self.tableWidget_produseLichidateClient_8.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseLichidateClient_8.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseLichidateClient_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseLichidateClient_8.setAutoScrollMargin(0)
        self.tableWidget_produseLichidateClient_8.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget_produseLichidateClient_8.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseLichidateClient_8.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseLichidateClient_8.setSortingEnabled(True)
        self.tableWidget_produseLichidateClient_8.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseLichidateClient_8.verticalHeader().setVisible(False)

        self.verticalLayout_51.addWidget(self.tableWidget_produseLichidateClient_8)

        self.frame_112 = QFrame(self.frame_detaliiAdaugareProduseFurnizor)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(800, 100))
        self.frame_112.setMaximumSize(QSize(16777215, 100))
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.formLayout_7 = QFormLayout(self.frame_112)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_NumarCI_9 = QLabel(self.frame_112)
        self.label_NumarCI_9.setObjectName(u"label_NumarCI_9")
        self.label_NumarCI_9.setMinimumSize(QSize(180, 30))
        self.label_NumarCI_9.setMaximumSize(QSize(180, 30))
        self.label_NumarCI_9.setFont(font9)
        self.label_NumarCI_9.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_NumarCI_9.setTextFormat(Qt.RichText)
        self.label_NumarCI_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_NumarCI_9)

        self.lineEdit_PrenumeClient_7 = QLineEdit(self.frame_112)
        self.lineEdit_PrenumeClient_7.setObjectName(u"lineEdit_PrenumeClient_7")
        self.lineEdit_PrenumeClient_7.setMinimumSize(QSize(50, 20))
        self.lineEdit_PrenumeClient_7.setMaximumSize(QSize(50, 30))
        self.lineEdit_PrenumeClient_7.setFont(font7)
        self.lineEdit_PrenumeClient_7.setFrame(True)
        self.lineEdit_PrenumeClient_7.setClearButtonEnabled(False)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lineEdit_PrenumeClient_7)

        self.label_NumarCI_10 = QLabel(self.frame_112)
        self.label_NumarCI_10.setObjectName(u"label_NumarCI_10")
        self.label_NumarCI_10.setMinimumSize(QSize(180, 30))
        self.label_NumarCI_10.setMaximumSize(QSize(180, 30))
        self.label_NumarCI_10.setFont(font9)
        self.label_NumarCI_10.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_NumarCI_10.setTextFormat(Qt.RichText)
        self.label_NumarCI_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_NumarCI_10)

        self.lineEdit_SerieCI_5 = QLineEdit(self.frame_112)
        self.lineEdit_SerieCI_5.setObjectName(u"lineEdit_SerieCI_5")
        self.lineEdit_SerieCI_5.setMinimumSize(QSize(250, 20))
        self.lineEdit_SerieCI_5.setMaximumSize(QSize(250, 30))
        self.lineEdit_SerieCI_5.setFont(font7)
        self.lineEdit_SerieCI_5.setMaxLength(123)
        self.lineEdit_SerieCI_5.setFrame(True)
        self.lineEdit_SerieCI_5.setClearButtonEnabled(False)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.lineEdit_SerieCI_5)


        self.verticalLayout_51.addWidget(self.frame_112)

        self.frame_89 = QFrame(self.frame_detaliiAdaugareProduseFurnizor)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMinimumSize(QSize(800, 50))
        self.frame_89.setMaximumSize(QSize(16777215, 50))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.pushButton_finalizareIncheiereContract_5 = QPushButton(self.frame_89)
        self.pushButton_finalizareIncheiereContract_5.setObjectName(u"pushButton_finalizareIncheiereContract_5")
        self.pushButton_finalizareIncheiereContract_5.setMinimumSize(QSize(165, 28))
        self.pushButton_finalizareIncheiereContract_5.setMaximumSize(QSize(165, 35))
        self.pushButton_finalizareIncheiereContract_5.setFont(font5)
        self.pushButton_finalizareIncheiereContract_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareIncheiereContract_5.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_finalizareIncheiereContract_5.setFlat(False)

        self.horizontalLayout_87.addWidget(self.pushButton_finalizareIncheiereContract_5)


        self.verticalLayout_51.addWidget(self.frame_89)


        self.horizontalLayout_82.addWidget(self.frame_detaliiAdaugareProduseFurnizor)

        self.tableWidget_produseLichidateClient_3 = QTableWidget(self.frame_82)
        if (self.tableWidget_produseLichidateClient_3.columnCount() < 4):
            self.tableWidget_produseLichidateClient_3.setColumnCount(4)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_3.setHorizontalHeaderItem(0, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_3.setHorizontalHeaderItem(1, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_3.setHorizontalHeaderItem(2, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_3.setHorizontalHeaderItem(3, __qtablewidgetitem146)
        self.tableWidget_produseLichidateClient_3.setObjectName(u"tableWidget_produseLichidateClient_3")
        self.tableWidget_produseLichidateClient_3.setMinimumSize(QSize(200, 0))
        self.tableWidget_produseLichidateClient_3.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_produseLichidateClient_3.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseLichidateClient_3.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseLichidateClient_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseLichidateClient_3.setAutoScrollMargin(0)
        self.tableWidget_produseLichidateClient_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_produseLichidateClient_3.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseLichidateClient_3.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseLichidateClient_3.setSortingEnabled(True)
        self.tableWidget_produseLichidateClient_3.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseLichidateClient_3.verticalHeader().setVisible(False)

        self.horizontalLayout_82.addWidget(self.tableWidget_produseLichidateClient_3)


        self.verticalLayout_50.addWidget(self.frame_82)

        self.frame_70 = QFrame(self.page_produseFurnizori)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(1200, 50))
        self.frame_70.setMaximumSize(QSize(16777215, 50))
        self.frame_70.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_23 = QPushButton(self.frame_70)
        self.pushButton_goHome_23.setObjectName(u"pushButton_goHome_23")
        self.pushButton_goHome_23.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_23.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_23.setFont(font5)
        self.pushButton_goHome_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_23.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_23.setFlat(False)

        self.horizontalLayout_75.addWidget(self.pushButton_goHome_23)

        self.pushButton_finalizareIncheiereContract_2 = QPushButton(self.frame_70)
        self.pushButton_finalizareIncheiereContract_2.setObjectName(u"pushButton_finalizareIncheiereContract_2")
        self.pushButton_finalizareIncheiereContract_2.setMinimumSize(QSize(165, 28))
        self.pushButton_finalizareIncheiereContract_2.setMaximumSize(QSize(165, 35))
        self.pushButton_finalizareIncheiereContract_2.setFont(font5)
        self.pushButton_finalizareIncheiereContract_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareIncheiereContract_2.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_finalizareIncheiereContract_2.setFlat(False)

        self.horizontalLayout_75.addWidget(self.pushButton_finalizareIncheiereContract_2)


        self.verticalLayout_50.addWidget(self.frame_70)

        self.stackedWidget_6.addWidget(self.page_produseFurnizori)
        self.page_produseAmanet = QWidget()
        self.page_produseAmanet.setObjectName(u"page_produseAmanet")
        self.verticalLayout_54 = QVBoxLayout(self.page_produseAmanet)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.page_produseAmanet)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(1200, 60))
        self.frame_76.setMaximumSize(QSize(16777215, 60))
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_32 = QPushButton(self.frame_76)
        self.pushButton_goHome_32.setObjectName(u"pushButton_goHome_32")
        self.pushButton_goHome_32.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_32.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_32.setFont(font5)
        self.pushButton_goHome_32.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_32.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_32.setFlat(False)

        self.horizontalLayout_96.addWidget(self.pushButton_goHome_32)

        self.frame_90 = QFrame(self.frame_76)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(1000, 16777215))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_51 = QLabel(self.frame_90)
        self.label_textSusCercMijloc_51.setObjectName(u"label_textSusCercMijloc_51")
        self.label_textSusCercMijloc_51.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_51.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_51.setFont(font12)
        self.label_textSusCercMijloc_51.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_51.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_51.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_51.setScaledContents(False)
        self.label_textSusCercMijloc_51.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_51.setWordWrap(True)

        self.horizontalLayout_97.addWidget(self.label_textSusCercMijloc_51)


        self.horizontalLayout_96.addWidget(self.frame_90)

        self.pushButton_goHome_33 = QPushButton(self.frame_76)
        self.pushButton_goHome_33.setObjectName(u"pushButton_goHome_33")
        self.pushButton_goHome_33.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_33.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_33.setFont(font5)
        self.pushButton_goHome_33.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_33.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_33.setFlat(False)

        self.horizontalLayout_96.addWidget(self.pushButton_goHome_33)


        self.verticalLayout_54.addWidget(self.frame_76)

        self.frame_98 = QFrame(self.page_produseAmanet)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(1200, 0))
        self.frame_98.setMaximumSize(QSize(1024, 16777215))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.frame_detaliiAdaugareProduseFurnizor_3 = QFrame(self.frame_98)
        self.frame_detaliiAdaugareProduseFurnizor_3.setObjectName(u"frame_detaliiAdaugareProduseFurnizor_3")
        self.frame_detaliiAdaugareProduseFurnizor_3.setMinimumSize(QSize(700, 0))
        self.frame_detaliiAdaugareProduseFurnizor_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_detaliiAdaugareProduseFurnizor_3.setFrameShape(QFrame.NoFrame)
        self.frame_detaliiAdaugareProduseFurnizor_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_detaliiAdaugareProduseFurnizor_3)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 5, 100)
        self.frame_103 = QFrame(self.frame_detaliiAdaugareProduseFurnizor_3)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(300, 40))
        self.frame_103.setMaximumSize(QSize(16777215, 40))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_86.setSpacing(8)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_dateClient_7 = QLabel(self.frame_103)
        self.label_dateClient_7.setObjectName(u"label_dateClient_7")
        self.label_dateClient_7.setMinimumSize(QSize(200, 30))
        self.label_dateClient_7.setMaximumSize(QSize(1200, 30))
        self.label_dateClient_7.setFont(font8)
        self.label_dateClient_7.setStyleSheet(u"color: rgba(255, 170, 0,0.7);")
        self.label_dateClient_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_86.addWidget(self.label_dateClient_7)


        self.verticalLayout_48.addWidget(self.frame_103)

        self.frame_73 = QFrame(self.frame_detaliiAdaugareProduseFurnizor_3)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(0, 300))
        self.frame_73.setMaximumSize(QSize(16777215, 300))
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_produseLichidateClient_6 = QTableWidget(self.frame_73)
        if (self.tableWidget_produseLichidateClient_6.columnCount() < 6):
            self.tableWidget_produseLichidateClient_6.setColumnCount(6)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_6.setHorizontalHeaderItem(0, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_6.setHorizontalHeaderItem(1, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_6.setHorizontalHeaderItem(2, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_6.setHorizontalHeaderItem(3, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_6.setHorizontalHeaderItem(4, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_6.setHorizontalHeaderItem(5, __qtablewidgetitem152)
        self.tableWidget_produseLichidateClient_6.setObjectName(u"tableWidget_produseLichidateClient_6")
        self.tableWidget_produseLichidateClient_6.setMinimumSize(QSize(500, 300))
        self.tableWidget_produseLichidateClient_6.setMaximumSize(QSize(1200, 300))
        self.tableWidget_produseLichidateClient_6.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseLichidateClient_6.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseLichidateClient_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseLichidateClient_6.setAutoScrollMargin(0)
        self.tableWidget_produseLichidateClient_6.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget_produseLichidateClient_6.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseLichidateClient_6.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseLichidateClient_6.setSortingEnabled(True)
        self.tableWidget_produseLichidateClient_6.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseLichidateClient_6.verticalHeader().setVisible(False)

        self.horizontalLayout_76.addWidget(self.tableWidget_produseLichidateClient_6)


        self.verticalLayout_48.addWidget(self.frame_73)

        self.frame_105 = QFrame(self.frame_detaliiAdaugareProduseFurnizor_3)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(700, 0))
        self.frame_105.setMaximumSize(QSize(16777215, 80))
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_105)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.pushButton_finalizareIncheiereContract_8 = QPushButton(self.frame_105)
        self.pushButton_finalizareIncheiereContract_8.setObjectName(u"pushButton_finalizareIncheiereContract_8")
        self.pushButton_finalizareIncheiereContract_8.setMinimumSize(QSize(165, 28))
        self.pushButton_finalizareIncheiereContract_8.setMaximumSize(QSize(165, 35))
        self.pushButton_finalizareIncheiereContract_8.setFont(font5)
        self.pushButton_finalizareIncheiereContract_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareIncheiereContract_8.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_finalizareIncheiereContract_8.setFlat(False)

        self.horizontalLayout_102.addWidget(self.pushButton_finalizareIncheiereContract_8)


        self.verticalLayout_48.addWidget(self.frame_105)


        self.horizontalLayout_98.addWidget(self.frame_detaliiAdaugareProduseFurnizor_3)

        self.tableWidget_produseLichidateClient_5 = QTableWidget(self.frame_98)
        if (self.tableWidget_produseLichidateClient_5.columnCount() < 2):
            self.tableWidget_produseLichidateClient_5.setColumnCount(2)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_5.setHorizontalHeaderItem(0, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_produseLichidateClient_5.setHorizontalHeaderItem(1, __qtablewidgetitem154)
        self.tableWidget_produseLichidateClient_5.setObjectName(u"tableWidget_produseLichidateClient_5")
        self.tableWidget_produseLichidateClient_5.setMinimumSize(QSize(200, 0))
        self.tableWidget_produseLichidateClient_5.setMaximumSize(QSize(1200, 16777215))
        self.tableWidget_produseLichidateClient_5.setStyleSheet(u"QTableWidget{\n"
"	color: rgb(220, 220, 220);\n"
"	background-color:transparent;\n"
"	border: 5px solid rgb(105, 95, 148);\n"
"}\n"
"QHeaderView::section { color:rgb(220,220,220); background-color: rgb(105, 95, 148); font-size:14px;}\n"
"\n"
"QScrollArea{border:none;padding-left:15px;background-color:transparent;}\n"
"QScrollBar:horizontal\n"
" {\n"
"     height: 15px;\n"
"     margin: 3px 15px 3px 15px;\n"
"     border: 1px transparent #2A2929;\n"
"     border-radius: 4px;\n"
"     background-color: rgba(0,0,0,0.3);    /* #2A2929; */\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal\n"
" {\n"
"	 background-color: rgb(105, 95, 148);\n"
"     min-width: 5px;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal\n"
" {\n"
"     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"     width: 10px;\n"
"     height: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
" {\n"
""
                        "     margin: 0px 3px 0px 3px;\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
" {\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"     height: 10px;\n"
"     width: 10px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
" {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"")
        self.tableWidget_produseLichidateClient_5.setFrameShape(QFrame.NoFrame)
        self.tableWidget_produseLichidateClient_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_produseLichidateClient_5.setAutoScrollMargin(0)
        self.tableWidget_produseLichidateClient_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_produseLichidateClient_5.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_produseLichidateClient_5.setGridStyle(Qt.SolidLine)
        self.tableWidget_produseLichidateClient_5.setSortingEnabled(True)
        self.tableWidget_produseLichidateClient_5.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_produseLichidateClient_5.verticalHeader().setVisible(False)

        self.horizontalLayout_98.addWidget(self.tableWidget_produseLichidateClient_5)


        self.verticalLayout_54.addWidget(self.frame_98)

        self.frame_72 = QFrame(self.page_produseAmanet)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(1200, 50))
        self.frame_72.setMaximumSize(QSize(16777215, 50))
        self.frame_72.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_25 = QPushButton(self.frame_72)
        self.pushButton_goHome_25.setObjectName(u"pushButton_goHome_25")
        self.pushButton_goHome_25.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_25.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_25.setFont(font5)
        self.pushButton_goHome_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_25.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_25.setFlat(False)

        self.horizontalLayout_95.addWidget(self.pushButton_goHome_25)

        self.pushButton_finalizareIncheiereContract_7 = QPushButton(self.frame_72)
        self.pushButton_finalizareIncheiereContract_7.setObjectName(u"pushButton_finalizareIncheiereContract_7")
        self.pushButton_finalizareIncheiereContract_7.setMinimumSize(QSize(165, 28))
        self.pushButton_finalizareIncheiereContract_7.setMaximumSize(QSize(165, 35))
        self.pushButton_finalizareIncheiereContract_7.setFont(font5)
        self.pushButton_finalizareIncheiereContract_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareIncheiereContract_7.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_finalizareIncheiereContract_7.setFlat(False)

        self.horizontalLayout_95.addWidget(self.pushButton_finalizareIncheiereContract_7)


        self.verticalLayout_54.addWidget(self.frame_72)

        self.stackedWidget_6.addWidget(self.page_produseAmanet)
        self.page_vanzareProduse = QWidget()
        self.page_vanzareProduse.setObjectName(u"page_vanzareProduse")
        self.verticalLayout_56 = QVBoxLayout(self.page_vanzareProduse)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_102 = QFrame(self.page_vanzareProduse)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(1200, 60))
        self.frame_102.setMaximumSize(QSize(16777215, 60))
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_104.setSpacing(0)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_102)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMaximumSize(QSize(1000, 16777215))
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_105.setSpacing(0)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.horizontalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_textSusCercMijloc_52 = QLabel(self.frame_104)
        self.label_textSusCercMijloc_52.setObjectName(u"label_textSusCercMijloc_52")
        self.label_textSusCercMijloc_52.setMinimumSize(QSize(10, 0))
        self.label_textSusCercMijloc_52.setMaximumSize(QSize(1000, 20))
        self.label_textSusCercMijloc_52.setFont(font12)
        self.label_textSusCercMijloc_52.setLayoutDirection(Qt.LeftToRight)
        self.label_textSusCercMijloc_52.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.label_textSusCercMijloc_52.setTextFormat(Qt.AutoText)
        self.label_textSusCercMijloc_52.setScaledContents(False)
        self.label_textSusCercMijloc_52.setAlignment(Qt.AlignCenter)
        self.label_textSusCercMijloc_52.setWordWrap(True)

        self.horizontalLayout_105.addWidget(self.label_textSusCercMijloc_52)


        self.horizontalLayout_104.addWidget(self.frame_104)


        self.verticalLayout_56.addWidget(self.frame_102)

        self.frame_80 = QFrame(self.page_vanzareProduse)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.frame_78 = QFrame(self.frame_80)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(550, 0))
        self.frame_78.setMaximumSize(QSize(550, 16777215))
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_78)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_81 = QFrame(self.frame_78)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 50))
        self.frame_81.setMaximumSize(QSize(16777215, 50))
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_dateClient_15 = QLabel(self.frame_81)
        self.label_dateClient_15.setObjectName(u"label_dateClient_15")
        self.label_dateClient_15.setMinimumSize(QSize(550, 30))
        self.label_dateClient_15.setMaximumSize(QSize(550, 30))
        self.label_dateClient_15.setFont(font8)
        self.label_dateClient_15.setStyleSheet(u"color: rgba(255, 170, 0,0.7);")
        self.label_dateClient_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_99.addWidget(self.label_dateClient_15)


        self.verticalLayout_53.addWidget(self.frame_81)

        self.frame_99 = QFrame(self.frame_78)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(550, 0))
        self.frame_99.setMaximumSize(QSize(550, 550))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.frame_99)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_Nume_6 = QLabel(self.frame_99)
        self.label_Nume_6.setObjectName(u"label_Nume_6")
        self.label_Nume_6.setMinimumSize(QSize(180, 30))
        self.label_Nume_6.setMaximumSize(QSize(180, 30))
        self.label_Nume_6.setFont(font9)
        self.label_Nume_6.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Nume_6.setTextFormat(Qt.RichText)
        self.label_Nume_6.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_Nume_6)

        self.lineEdit_NumeClient_5 = QLineEdit(self.frame_99)
        self.lineEdit_NumeClient_5.setObjectName(u"lineEdit_NumeClient_5")
        self.lineEdit_NumeClient_5.setMinimumSize(QSize(300, 20))
        self.lineEdit_NumeClient_5.setMaximumSize(QSize(300, 30))
        self.lineEdit_NumeClient_5.setFont(font7)
        self.lineEdit_NumeClient_5.setFrame(True)
        self.lineEdit_NumeClient_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_NumeClient_5.setClearButtonEnabled(False)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.lineEdit_NumeClient_5)

        self.label_Nume_7 = QLabel(self.frame_99)
        self.label_Nume_7.setObjectName(u"label_Nume_7")
        self.label_Nume_7.setMinimumSize(QSize(180, 30))
        self.label_Nume_7.setMaximumSize(QSize(180, 30))
        self.label_Nume_7.setFont(font9)
        self.label_Nume_7.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Nume_7.setTextFormat(Qt.RichText)
        self.label_Nume_7.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_Nume_7)

        self.lineEdit_NumeClient_6 = QLineEdit(self.frame_99)
        self.lineEdit_NumeClient_6.setObjectName(u"lineEdit_NumeClient_6")
        self.lineEdit_NumeClient_6.setMinimumSize(QSize(300, 20))
        self.lineEdit_NumeClient_6.setMaximumSize(QSize(300, 30))
        self.lineEdit_NumeClient_6.setFont(font7)
        self.lineEdit_NumeClient_6.setFrame(True)
        self.lineEdit_NumeClient_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_NumeClient_6.setClearButtonEnabled(False)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.lineEdit_NumeClient_6)

        self.label_SerieCI_6 = QLabel(self.frame_99)
        self.label_SerieCI_6.setObjectName(u"label_SerieCI_6")
        self.label_SerieCI_6.setMinimumSize(QSize(180, 30))
        self.label_SerieCI_6.setMaximumSize(QSize(180, 30))
        self.label_SerieCI_6.setFont(font9)
        self.label_SerieCI_6.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_SerieCI_6.setTextFormat(Qt.RichText)
        self.label_SerieCI_6.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_SerieCI_6)

        self.label_SerieCI_7 = QLabel(self.frame_99)
        self.label_SerieCI_7.setObjectName(u"label_SerieCI_7")
        self.label_SerieCI_7.setMinimumSize(QSize(180, 30))
        self.label_SerieCI_7.setMaximumSize(QSize(180, 30))
        self.label_SerieCI_7.setFont(font9)
        self.label_SerieCI_7.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_SerieCI_7.setTextFormat(Qt.RichText)
        self.label_SerieCI_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.label_SerieCI_7)

        self.label_NumarCI_7 = QLabel(self.frame_99)
        self.label_NumarCI_7.setObjectName(u"label_NumarCI_7")
        self.label_NumarCI_7.setMinimumSize(QSize(180, 30))
        self.label_NumarCI_7.setMaximumSize(QSize(180, 30))
        self.label_NumarCI_7.setFont(font9)
        self.label_NumarCI_7.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_NumarCI_7.setTextFormat(Qt.RichText)
        self.label_NumarCI_7.setAlignment(Qt.AlignCenter)

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_NumarCI_7)

        self.lineEdit_PrenumeClient_5 = QLineEdit(self.frame_99)
        self.lineEdit_PrenumeClient_5.setObjectName(u"lineEdit_PrenumeClient_5")
        self.lineEdit_PrenumeClient_5.setMinimumSize(QSize(50, 20))
        self.lineEdit_PrenumeClient_5.setMaximumSize(QSize(50, 30))
        self.lineEdit_PrenumeClient_5.setFont(font7)
        self.lineEdit_PrenumeClient_5.setFrame(True)
        self.lineEdit_PrenumeClient_5.setClearButtonEnabled(False)

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.lineEdit_PrenumeClient_5)


        self.verticalLayout_53.addWidget(self.frame_99)

        self.frame_108 = QFrame(self.frame_78)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(550, 80))
        self.frame_108.setMaximumSize(QSize(550, 80))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")

        self.verticalLayout_53.addWidget(self.frame_108)


        self.horizontalLayout_101.addWidget(self.frame_78)

        self.frame_79 = QFrame(self.frame_80)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(550, 0))
        self.frame_79.setMaximumSize(QSize(550, 16777215))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_79)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.frame_100 = QFrame(self.frame_79)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(0, 50))
        self.frame_100.setMaximumSize(QSize(16777215, 50))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.label_dateClient_16 = QLabel(self.frame_100)
        self.label_dateClient_16.setObjectName(u"label_dateClient_16")
        self.label_dateClient_16.setMinimumSize(QSize(550, 30))
        self.label_dateClient_16.setMaximumSize(QSize(550, 30))
        self.label_dateClient_16.setFont(font8)
        self.label_dateClient_16.setStyleSheet(u"color: rgba(255, 170, 0,0.7);")
        self.label_dateClient_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_100.addWidget(self.label_dateClient_16)


        self.verticalLayout_55.addWidget(self.frame_100)

        self.frame_detaliiClient_2 = QFrame(self.frame_79)
        self.frame_detaliiClient_2.setObjectName(u"frame_detaliiClient_2")
        self.frame_detaliiClient_2.setMinimumSize(QSize(550, 550))
        self.frame_detaliiClient_2.setMaximumSize(QSize(550, 550))
        self.frame_detaliiClient_2.setFrameShape(QFrame.NoFrame)
        self.frame_detaliiClient_2.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_detaliiClient_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_CNP_3 = QLabel(self.frame_detaliiClient_2)
        self.label_CNP_3.setObjectName(u"label_CNP_3")
        self.label_CNP_3.setMinimumSize(QSize(180, 30))
        self.label_CNP_3.setMaximumSize(QSize(180, 30))
        self.label_CNP_3.setFont(font9)
        self.label_CNP_3.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_CNP_3.setTextFormat(Qt.RichText)
        self.label_CNP_3.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_CNP_3)

        self.lineEdit_CNP_3 = QLineEdit(self.frame_detaliiClient_2)
        self.lineEdit_CNP_3.setObjectName(u"lineEdit_CNP_3")
        self.lineEdit_CNP_3.setMinimumSize(QSize(300, 20))
        self.lineEdit_CNP_3.setMaximumSize(QSize(300, 30))
        self.lineEdit_CNP_3.setFont(font7)
        self.lineEdit_CNP_3.setMaxLength(30)
        self.lineEdit_CNP_3.setFrame(True)
        self.lineEdit_CNP_3.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.lineEdit_CNP_3)

        self.lineEdit_CNP_2 = QLineEdit(self.frame_detaliiClient_2)
        self.lineEdit_CNP_2.setObjectName(u"lineEdit_CNP_2")
        self.lineEdit_CNP_2.setMinimumSize(QSize(300, 20))
        self.lineEdit_CNP_2.setMaximumSize(QSize(300, 30))
        self.lineEdit_CNP_2.setFont(font7)
        self.lineEdit_CNP_2.setMaxLength(30)
        self.lineEdit_CNP_2.setFrame(True)
        self.lineEdit_CNP_2.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.lineEdit_CNP_2)

        self.label_CNP_2 = QLabel(self.frame_detaliiClient_2)
        self.label_CNP_2.setObjectName(u"label_CNP_2")
        self.label_CNP_2.setMinimumSize(QSize(180, 30))
        self.label_CNP_2.setMaximumSize(QSize(180, 30))
        self.label_CNP_2.setFont(font9)
        self.label_CNP_2.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_CNP_2.setTextFormat(Qt.RichText)
        self.label_CNP_2.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.label_CNP_2)

        self.lineEdit_NumeClient_2 = QLineEdit(self.frame_detaliiClient_2)
        self.lineEdit_NumeClient_2.setObjectName(u"lineEdit_NumeClient_2")
        self.lineEdit_NumeClient_2.setMinimumSize(QSize(300, 20))
        self.lineEdit_NumeClient_2.setMaximumSize(QSize(300, 30))
        self.lineEdit_NumeClient_2.setFont(font7)
        self.lineEdit_NumeClient_2.setFrame(True)
        self.lineEdit_NumeClient_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_NumeClient_2.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.lineEdit_NumeClient_2)

        self.lineEdit_Adresa_2 = QLineEdit(self.frame_detaliiClient_2)
        self.lineEdit_Adresa_2.setObjectName(u"lineEdit_Adresa_2")
        self.lineEdit_Adresa_2.setMinimumSize(QSize(300, 20))
        self.lineEdit_Adresa_2.setMaximumSize(QSize(300, 30))
        self.lineEdit_Adresa_2.setFont(font7)
        self.lineEdit_Adresa_2.setFrame(True)
        self.lineEdit_Adresa_2.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.lineEdit_Adresa_2)

        self.label_Adresa_2 = QLabel(self.frame_detaliiClient_2)
        self.label_Adresa_2.setObjectName(u"label_Adresa_2")
        self.label_Adresa_2.setMinimumSize(QSize(180, 30))
        self.label_Adresa_2.setMaximumSize(QSize(180, 30))
        self.label_Adresa_2.setFont(font9)
        self.label_Adresa_2.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Adresa_2.setTextFormat(Qt.RichText)
        self.label_Adresa_2.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_Adresa_2)

        self.label_Telefon_2 = QLabel(self.frame_detaliiClient_2)
        self.label_Telefon_2.setObjectName(u"label_Telefon_2")
        self.label_Telefon_2.setMinimumSize(QSize(180, 30))
        self.label_Telefon_2.setMaximumSize(QSize(180, 30))
        self.label_Telefon_2.setFont(font9)
        self.label_Telefon_2.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Telefon_2.setTextFormat(Qt.RichText)
        self.label_Telefon_2.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_Telefon_2)

        self.lineEdit_Telefon_2 = QLineEdit(self.frame_detaliiClient_2)
        self.lineEdit_Telefon_2.setObjectName(u"lineEdit_Telefon_2")
        self.lineEdit_Telefon_2.setMinimumSize(QSize(300, 20))
        self.lineEdit_Telefon_2.setMaximumSize(QSize(300, 30))
        self.lineEdit_Telefon_2.setFont(font7)
        self.lineEdit_Telefon_2.setFrame(True)
        self.lineEdit_Telefon_2.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.lineEdit_Telefon_2)

        self.label_Email_2 = QLabel(self.frame_detaliiClient_2)
        self.label_Email_2.setObjectName(u"label_Email_2")
        self.label_Email_2.setMinimumSize(QSize(180, 30))
        self.label_Email_2.setMaximumSize(QSize(180, 30))
        self.label_Email_2.setFont(font9)
        self.label_Email_2.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Email_2.setTextFormat(Qt.RichText)
        self.label_Email_2.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_Email_2)

        self.lineEdit_Email_2 = QLineEdit(self.frame_detaliiClient_2)
        self.lineEdit_Email_2.setObjectName(u"lineEdit_Email_2")
        self.lineEdit_Email_2.setMinimumSize(QSize(300, 20))
        self.lineEdit_Email_2.setMaximumSize(QSize(300, 30))
        self.lineEdit_Email_2.setFont(font7)
        self.lineEdit_Email_2.setFrame(True)
        self.lineEdit_Email_2.setClearButtonEnabled(False)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.lineEdit_Email_2)

        self.label_Nume_3 = QLabel(self.frame_detaliiClient_2)
        self.label_Nume_3.setObjectName(u"label_Nume_3")
        self.label_Nume_3.setMinimumSize(QSize(180, 30))
        self.label_Nume_3.setMaximumSize(QSize(180, 30))
        self.label_Nume_3.setFont(font9)
        self.label_Nume_3.setStyleSheet(u"QLabel{\n"
"color: rgb(220,220,220);\n"
"}")
        self.label_Nume_3.setTextFormat(Qt.RichText)
        self.label_Nume_3.setAlignment(Qt.AlignCenter)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_Nume_3)


        self.verticalLayout_55.addWidget(self.frame_detaliiClient_2)


        self.horizontalLayout_101.addWidget(self.frame_79)


        self.verticalLayout_56.addWidget(self.frame_80)

        self.frame_101 = QFrame(self.page_vanzareProduse)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMinimumSize(QSize(1200, 50))
        self.frame_101.setMaximumSize(QSize(16777215, 50))
        self.frame_101.setStyleSheet(u"border:none;\n"
"color:rgb(60,231,195);")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_103.setSpacing(0)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.pushButton_goHome_26 = QPushButton(self.frame_101)
        self.pushButton_goHome_26.setObjectName(u"pushButton_goHome_26")
        self.pushButton_goHome_26.setMinimumSize(QSize(30, 30))
        self.pushButton_goHome_26.setMaximumSize(QSize(30, 30))
        self.pushButton_goHome_26.setFont(font5)
        self.pushButton_goHome_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_goHome_26.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_goHome_26.setFlat(False)

        self.horizontalLayout_103.addWidget(self.pushButton_goHome_26)

        self.pushButton_finalizareIncheiereContract_10 = QPushButton(self.frame_101)
        self.pushButton_finalizareIncheiereContract_10.setObjectName(u"pushButton_finalizareIncheiereContract_10")
        self.pushButton_finalizareIncheiereContract_10.setMinimumSize(QSize(165, 28))
        self.pushButton_finalizareIncheiereContract_10.setMaximumSize(QSize(165, 35))
        self.pushButton_finalizareIncheiereContract_10.setFont(font5)
        self.pushButton_finalizareIncheiereContract_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finalizareIncheiereContract_10.setStyleSheet(u"QPushButton{\n"
"	color:rgb(220,220,220);\n"
"	background-color:  rgb(105,95,148);\n"
"	border:none;\n"
"	padding-top:2px;\n"
"	padding-bottom:2px;\n"
"	border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color: rgba(255, 170, 0,0.8);\n"
"}\n"
"QPushButton:pressed{\n"
"	color:rgb(220, 220, 220);\n"
"	background-color:rgb(105,95,148);\n"
"}")
        self.pushButton_finalizareIncheiereContract_10.setFlat(False)

        self.horizontalLayout_103.addWidget(self.pushButton_finalizareIncheiereContract_10)


        self.verticalLayout_56.addWidget(self.frame_101)

        self.stackedWidget_6.addWidget(self.page_vanzareProduse)

        self.horizontalLayout_83.addWidget(self.stackedWidget_6)


        self.horizontalLayout_88.addWidget(self.frame_71)

        self.stackedWidget.addWidget(self.page_gestiuneDeVanzari)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.drop_shadow_layout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMinimumSize(QSize(30, 0))
        self.credits_bar.setMaximumSize(QSize(16777212, 30))
        self.credits_bar.setStyleSheet(u"background-color:none;")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font16 = QFont()
        font16.setFamily(u"Roboto Light")
        font16.setPointSize(8)
        self.label_credits.setFont(font16)
        self.label_credits.setStyleSheet(u"color:rgb(128,102,168);")
        self.label_credits.setTextFormat(Qt.PlainText)

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_5.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding:5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_grip)


        self.drop_shadow_layout.addWidget(self.credits_bar)


        self.verticalLayout_9.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(2)
        self.stackedWidget_5.setCurrentIndex(3)
        self.stackedWidget_6.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"EASY PAWN SHOP - Amanet Manager  ", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
        self.label_numarCercMijloc_2.setText(QCoreApplication.translate("MainWindow", u"Gestiune", None))
        self.label_textSusCercMijloc_2.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.label_textJosCercMijloc_2.setText(QCoreApplication.translate("MainWindow", u"vanzari", None))
        self.label.setText("")
        self.label_numarCercStanga.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_textSusCercStanga.setText(QCoreApplication.translate("MainWindow", u"Contracte aproape", None))
        self.label_textJosCercStanga.setText(QCoreApplication.translate("MainWindow", u"de termenul final", None))
        self.label_numarCercDreapta.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_textSusCercDreapta.setText(QCoreApplication.translate("MainWindow", u"Contracte in", None))
        self.label_textJosCercDreapta.setText(QCoreApplication.translate("MainWindow", u"termen", None))
        self.label_numarCercMijloc.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_textSusCercMijloc.setText(QCoreApplication.translate("MainWindow", u"Produse in", None))
        self.label_textJosCercMijloc.setText(QCoreApplication.translate("MainWindow", u"amanet", None))
        self.pushButton_genereazaContract.setText(QCoreApplication.translate("MainWindow", u"Genereaza contract", None))
        self.pushButton_cautaClient.setText(QCoreApplication.translate("MainWindow", u"Cauta client", None))
        self.label_textSusCercMijloc_48.setText(QCoreApplication.translate("MainWindow", u"Tip contract", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Vanzare", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Amanet", None))
        self.label_dateClient.setText(QCoreApplication.translate("MainWindow", u"Introduceti date client:", None))
        self.label_Nume.setText(QCoreApplication.translate("MainWindow", u"Nume", None))
        self.lineEdit_NumeClient.setPlaceholderText("")
        self.label_Prenume.setText(QCoreApplication.translate("MainWindow", u"Prenume", None))
        self.lineEdit_PrenumeClient.setPlaceholderText("")
        self.label_SerieCI.setText(QCoreApplication.translate("MainWindow", u"Serie C.I", None))
        self.lineEdit_SerieCI.setPlaceholderText("")
        self.label_NumarCI.setText(QCoreApplication.translate("MainWindow", u"Numar C.I", None))
        self.lineEdit_NumarCI.setPlaceholderText("")
        self.label_CNP.setText(QCoreApplication.translate("MainWindow", u"CNP", None))
        self.lineEdit_CNP.setPlaceholderText("")
        self.label_EliberatDe.setText(QCoreApplication.translate("MainWindow", u"Eliberat de", None))
        self.lineEdit_EliberatDe.setPlaceholderText("")
        self.label_DataEliberarii.setText(QCoreApplication.translate("MainWindow", u"Data eliberarii", None))
        self.label_Adresa.setText(QCoreApplication.translate("MainWindow", u"Adresa", None))
        self.lineEdit_Adresa.setPlaceholderText("")
        self.label_Telefon.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.lineEdit_Telefon.setPlaceholderText("")
        self.label_Email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_Email.setPlaceholderText("")
        self.pushButton_backToHome.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_backToHome_2.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_dateClient_3.setText(QCoreApplication.translate("MainWindow", u"Introduceti date produs:", None))
        self.label_Nume_2.setText(QCoreApplication.translate("MainWindow", u"Denumire obiect", None))
        self.lineEdit_ObservatiiProdus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: codat/display cu zgarieturi/urme uzura", None))
        self.label_Prenume_3.setText(QCoreApplication.translate("MainWindow", u"Observatii", None))
        self.lineEdit_ValoareEvaluata.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: 550", None))
        self.label_SerieCI_3.setText(QCoreApplication.translate("MainWindow", u"Valoare evaluata", None))
        self.lineEdit_SumaImprumutata.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: 550", None))
        self.label_NumarCI_3.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None))
        self.lineEdit_ComisionLuna.setText("")
        self.lineEdit_ComisionLuna.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: 100", None))
        self.label_NumarCI_4.setText(QCoreApplication.translate("MainWindow", u"Comision/luna", None))
        self.lineEdit_denumireProdus.setInputMask("")
        self.lineEdit_denumireProdus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: iPhone 12 Pro MAX IMEI: 987654321123", None))
        self.pushButton_adaugaProdus.setText(QCoreApplication.translate("MainWindow", u"Inca un produs", None))
        self.pushButton_finalizareContract.setText(QCoreApplication.translate("MainWindow", u"Genereaza contract", None))
        self.label_textSusCercMijloc_9.setText(QCoreApplication.translate("MainWindow", u"Cauta client", None))
        self.label_numarContractDePrelungit_5.setText(QCoreApplication.translate("MainWindow", u"Cauta dupa", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Nume", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"CNP", None))
        self.lineEdit_CautaNume.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nume", None))
        self.lineEdit_CautaPrenume.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prenume", None))
        self.lineEdit_CautaCnp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNP", None))
        self.pushButton_finalizareContract_5.setText("")
        self.label_numarCercMijloc_6.setText(QCoreApplication.translate("MainWindow", u"YES", None))
        self.label_textSusCercMijloc_12.setText(QCoreApplication.translate("MainWindow", u"Clientu a fost gasit", None))
        self.label_numarCercMijloc_8.setText(QCoreApplication.translate("MainWindow", u"OUPS", None))
        self.label_textSusCercMijloc_16.setText(QCoreApplication.translate("MainWindow", u"Clientul nu a fost gasit", None))
        self.label_numarCercMijloc_4.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_textSusCercMijloc_4.setText(QCoreApplication.translate("MainWindow", u"Clienti au fost gasiti cu acest nume", None))
        self.label_textJosCercMijloc_4.setText(QCoreApplication.translate("MainWindow", u"Pentru a gasi persoana potrivita cauta dupa CNP", None))
        ___qtablewidgetitem = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nume", None));
        ___qtablewidgetitem1 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prenume", None));
        ___qtablewidgetitem2 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CNP", None));
        ___qtablewidgetitem3 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Serie C.I", None));
        ___qtablewidgetitem4 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Numar C.I", None));
        ___qtablewidgetitem5 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Adresa", None));
        ___qtablewidgetitem6 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem7 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Contracte", None));
        self.pushButton_backFromClientGasit.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_genereazaContractClientGasit.setText(QCoreApplication.translate("MainWindow", u"Genereaza contract nou pentru acest client", None))
        self.label_textSusCercMijloc_10.setText(QCoreApplication.translate("MainWindow", u"Contractele:", None))
        self.label_numarCercMijloc_7.setText(QCoreApplication.translate("MainWindow", u"100,32,12,123,213,", None))
        self.label_textJosCercMijloc_9.setText(QCoreApplication.translate("MainWindow", u"expira azi", None))
        self.label_textSusCercMijloc_6.setText(QCoreApplication.translate("MainWindow", u"Contractele:", None))
        self.label_numarCercMijloc_11.setText(QCoreApplication.translate("MainWindow", u"100,32,12,123,213,", None))
        self.label_textJosCercMijloc_5.setText(QCoreApplication.translate("MainWindow", u"expira maine", None))
        self.label_textSusCercMijloc_11.setText(QCoreApplication.translate("MainWindow", u"Contractele:", None))
        self.label_numarCercMijloc_12.setText(QCoreApplication.translate("MainWindow", u"100,32,12,123,213,", None))
        self.label_textJosCercMijloc_10.setText(QCoreApplication.translate("MainWindow", u"expira peste 2 zile", None))
        self.label_textSusCercMijloc_14.setText(QCoreApplication.translate("MainWindow", u"Contractele:", None))
        self.label_numarCercMijloc_13.setText(QCoreApplication.translate("MainWindow", u"100,32,12,123,213,", None))
        self.label_textJosCercMijloc_11.setText(QCoreApplication.translate("MainWindow", u"expira peste 3 zile", None))
        self.pushButton_maiMultiClientiGasitiOK_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_textSusCercMijloc_8.setText(QCoreApplication.translate("MainWindow", u"Numar contract:", None))
        self.lineEdit_numarContractDePrelungit_4.setPlaceholderText("")
        self.pushButton_backToHome_5.setText("")
        self.pushButton_goHome_2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_13.setText(QCoreApplication.translate("MainWindow", u"Urmatoarele contracte sunt in termen:", None))
        self.pushButton_goHome_3.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem9 = self.tableWidget_contracteInTermen.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem10 = self.tableWidget_contracteInTermen.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nume ", None));
        ___qtablewidgetitem11 = self.tableWidget_contracteInTermen.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Prenume", None));
        ___qtablewidgetitem12 = self.tableWidget_contracteInTermen.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem13 = self.tableWidget_contracteInTermen.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem14 = self.tableWidget_contracteInTermen.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem15 = self.tableWidget_contracteInTermen.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem16 = self.tableWidget_contracteInTermen.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem17 = self.tableWidget_contracteInTermen.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem18 = self.tableWidget_contracteInTermen.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        self.pushButton_goHome_4.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_15.setText(QCoreApplication.translate("MainWindow", u"Urmatoarele contracte sunt in perioada de asteptare (5 zile dupa expirare):", None))
        self.pushButton_goHome_5.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem19 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem20 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Nume ", None));
        ___qtablewidgetitem21 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Prenume", None));
        ___qtablewidgetitem22 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem23 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem24 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem25 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem26 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem27 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem28 = self.tableWidget_contracteInAsteptare.horizontalHeaderItem(9)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        self.pushButton_goHome_6.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_17.setText(QCoreApplication.translate("MainWindow", u"Urmatoarele contracte sunt expirate:", None))
        self.pushButton_goHome_7.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem29 = self.tableWidget_contracteExpirate.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem30 = self.tableWidget_contracteExpirate.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Nume ", None));
        ___qtablewidgetitem31 = self.tableWidget_contracteExpirate.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Prenume", None));
        ___qtablewidgetitem32 = self.tableWidget_contracteExpirate.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem33 = self.tableWidget_contracteExpirate.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem34 = self.tableWidget_contracteExpirate.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem35 = self.tableWidget_contracteExpirate.horizontalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem36 = self.tableWidget_contracteExpirate.horizontalHeaderItem(7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem37 = self.tableWidget_contracteExpirate.horizontalHeaderItem(8)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem38 = self.tableWidget_contracteExpirate.horizontalHeaderItem(9)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem39 = self.tableWidget_contracteExpirate.horizontalHeaderItem(10)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Data expirare initiala", None));
        ___qtablewidgetitem40 = self.tableWidget_contracteExpirate.horizontalHeaderItem(11)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Data prelungire", None));
        ___qtablewidgetitem41 = self.tableWidget_contracteExpirate.horizontalHeaderItem(12)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Nr. zile prelungite", None));
        ___qtablewidgetitem42 = self.tableWidget_contracteExpirate.horizontalHeaderItem(13)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Comision prelungire", None));
        ___qtablewidgetitem43 = self.tableWidget_contracteExpirate.horizontalHeaderItem(14)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Total de restituit dupa prelungire", None));
        self.pushButton_goHome_8.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_18.setText(QCoreApplication.translate("MainWindow", u"Urmatoarele contracte au fost incheiate:", None))
        self.pushButton_goHome_9.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem44 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem45 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Nume ", None));
        ___qtablewidgetitem46 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Prenume", None));
        ___qtablewidgetitem47 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem48 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem49 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem50 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(6)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem51 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(7)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem52 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(8)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem53 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(9)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem54 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(10)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Data expirare initiala", None));
        ___qtablewidgetitem55 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(11)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Data prelungire", None));
        ___qtablewidgetitem56 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(12)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Nr zile prelungite", None));
        ___qtablewidgetitem57 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(13)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Comision prelungire", None));
        ___qtablewidgetitem58 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(14)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Total de restituit dupa prelungire", None));
        ___qtablewidgetitem59 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(15)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Data lichidare", None));
        ___qtablewidgetitem60 = self.tableWidget_contracteIncheiate.horizontalHeaderItem(16)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Lichidat de", None));
        self.pushButton_goHome_15.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_26.setText(QCoreApplication.translate("MainWindow", u"Urmatoarele contracte au fost prelungite:", None))
        self.pushButton_goHome_16.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem61 = self.tableWidget_contractePrelungite.horizontalHeaderItem(0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem62 = self.tableWidget_contractePrelungite.horizontalHeaderItem(1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Nume ", None));
        ___qtablewidgetitem63 = self.tableWidget_contractePrelungite.horizontalHeaderItem(2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Prenume", None));
        ___qtablewidgetitem64 = self.tableWidget_contractePrelungite.horizontalHeaderItem(3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Telefon", None));
        ___qtablewidgetitem65 = self.tableWidget_contractePrelungite.horizontalHeaderItem(4)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem66 = self.tableWidget_contractePrelungite.horizontalHeaderItem(5)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem67 = self.tableWidget_contractePrelungite.horizontalHeaderItem(6)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem68 = self.tableWidget_contractePrelungite.horizontalHeaderItem(7)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem69 = self.tableWidget_contractePrelungite.horizontalHeaderItem(8)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem70 = self.tableWidget_contractePrelungite.horizontalHeaderItem(9)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem71 = self.tableWidget_contractePrelungite.horizontalHeaderItem(10)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Data expirare initiala", None));
        ___qtablewidgetitem72 = self.tableWidget_contractePrelungite.horizontalHeaderItem(11)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Data prelungire", None));
        ___qtablewidgetitem73 = self.tableWidget_contractePrelungite.horizontalHeaderItem(12)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Nr. zile prelungite", None));
        ___qtablewidgetitem74 = self.tableWidget_contractePrelungite.horizontalHeaderItem(13)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Comision prelungire", None));
        ___qtablewidgetitem75 = self.tableWidget_contractePrelungite.horizontalHeaderItem(14)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Total de restituit dupa prelungire", None));
        self.label_textSusCercMijloc_19.setText(QCoreApplication.translate("MainWindow", u"Contractul nr. ", None))
        self.label_numarCercDreapta_2.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_textSusCercMijloc_20.setText(QCoreApplication.translate("MainWindow", u"din ", None))
        self.label_numarCercDreapta_3.setText(QCoreApplication.translate("MainWindow", u"1.01.2021", None))
        self.label_textSusCercMijloc_44.setText(QCoreApplication.translate("MainWindow", u"Prelungit in data de: ", None))
        self.label_numarCercDreapta_6.setText(QCoreApplication.translate("MainWindow", u"10.02.1999", None))
        self.label_textSusCercMijloc_45.setText(QCoreApplication.translate("MainWindow", u"pana pe:", None))
        self.label_numarCercDreapta_5.setText(QCoreApplication.translate("MainWindow", u"10.01.1999", None))
        self.label_textSusCercMijloc_46.setText(QCoreApplication.translate("MainWindow", u"( 30 zile)", None))
        self.label_textSusCercMijloc_23.setText(QCoreApplication.translate("MainWindow", u"Pentru cate zile doresti sa prelungesi contractul?", None))
        self.lineEdit_numarContractDePrelungit_7.setPlaceholderText("")
        self.pushButton_goHome_10.setText(QCoreApplication.translate("MainWindow", u"Calculeaza", None))
        self.label_textSusCercMijloc_40.setText(QCoreApplication.translate("MainWindow", u"Comisionul de plata dupa 20 de zile va fi:", None))
        self.label_numarCercDreapta_21.setText(QCoreApplication.translate("MainWindow", u"4002", None))
        self.label_textSusCercMijloc_37.setText(QCoreApplication.translate("MainWindow", u"Nume:", None))
        self.label_numarCercDreapta_4.setText(QCoreApplication.translate("MainWindow", u"Butura", None))
        self.label_textSusCercMijloc_36.setText(QCoreApplication.translate("MainWindow", u"Prenume:", None))
        self.label_numarCercDreapta_17.setText(QCoreApplication.translate("MainWindow", u"Stefan", None))
        self.label_textSusCercMijloc_38.setText(QCoreApplication.translate("MainWindow", u"CNP:", None))
        self.label_numarCercDreapta_20.setText(QCoreApplication.translate("MainWindow", u"1930724270052", None))
        self.label_textSusCercMijloc_34.setText(QCoreApplication.translate("MainWindow", u"Serie C.I:", None))
        self.label_numarCercDreapta_19.setText(QCoreApplication.translate("MainWindow", u"NT", None))
        self.label_textSusCercMijloc_33.setText(QCoreApplication.translate("MainWindow", u"Numar C.I:", None))
        self.label_numarCercDreapta_16.setText(QCoreApplication.translate("MainWindow", u"994348", None))
        self.label_textSusCercMijloc_39.setText(QCoreApplication.translate("MainWindow", u"Telefon:", None))
        self.label_numarCercDreapta_18.setText(QCoreApplication.translate("MainWindow", u"0751530375", None))
        self.label_textSusCercMijloc_35.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_numarCercDreapta_11.setText(QCoreApplication.translate("MainWindow", u"stefan.butura@gmail.com", None))
        self.label_textSusCercMijloc_21.setText(QCoreApplication.translate("MainWindow", u"Produse:", None))
        self.label_numarCercMijloc_9.setText(QCoreApplication.translate("MainWindow", u"iPhone 12 pro, Samsung galaxy, nokia", None))
        self.label_textSusCercMijloc_28.setText(QCoreApplication.translate("MainWindow", u"Observatii:", None))
        self.label_numarCercMijloc_10.setText(QCoreApplication.translate("MainWindow", u"descriere produs1, descriere produs2,etc", None))
        self.label_textSusCercMijloc_29.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata:", None))
        self.label_numarCercDreapta_12.setText(QCoreApplication.translate("MainWindow", u"2000", None))
        self.label_textSusCercMijloc_30.setText(QCoreApplication.translate("MainWindow", u"Comision/luna:", None))
        self.label_numarCercDreapta_13.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label_textSusCercMijloc_41.setText(QCoreApplication.translate("MainWindow", u"Comision curent:", None))
        self.label_numarCercDreapta_22.setText(QCoreApplication.translate("MainWindow", u"Comision curent:", None))
        self.label_textSusCercMijloc_31.setText(QCoreApplication.translate("MainWindow", u"Penalizari:", None))
        self.label_numarCercDreapta_14.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.label_textSusCercMijloc_32.setText(QCoreApplication.translate("MainWindow", u"Total de achitat:", None))
        self.label_numarCercDreapta_15.setText(QCoreApplication.translate("MainWindow", u"4002", None))
        self.label_textSusCercMijloc_22.setText(QCoreApplication.translate("MainWindow", u"Inainte de a prelungi contractul elibereaza bonul fiscal si introdu numarul bonului", None))
        self.lineEdit_numarContractDePrelungit_6.setPlaceholderText("")
        self.pushButton_goHome.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_incheieContract_6.setText(QCoreApplication.translate("MainWindow", u"Prelungeste contract", None))
        self.pushButton_incheieContract_8.setText(QCoreApplication.translate("MainWindow", u"Prelungeste contract", None))
        self.pushButton_incheieContract_7.setText(QCoreApplication.translate("MainWindow", u"Incheie contract", None))
        self.pushButton_finalizareIncheiereContract.setText(QCoreApplication.translate("MainWindow", u"Incheie contract", None))
        self.pushButton_lichideazaContractCuTermenDepasit.setText(QCoreApplication.translate("MainWindow", u"Lichideaza contract cu termen depasit", None))
        self.label_textSusCercMijloc_47.setText(QCoreApplication.translate("MainWindow", u"Numar contract:", None))
        self.lineEdit_numarContractDePrelungit_5.setPlaceholderText("")
        self.pushButton_backToHome_6.setText("")
        self.pushButton_goHome_11.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_24.setText(QCoreApplication.translate("MainWindow", u"Lista cu produsele din amanet care se afla in termen:", None))
        self.pushButton_goHome_12.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem76 = self.tableWidget_produseInTermen.horizontalHeaderItem(0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem77 = self.tableWidget_produseInTermen.horizontalHeaderItem(1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Observatii", None));
        ___qtablewidgetitem78 = self.tableWidget_produseInTermen.horizontalHeaderItem(2)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem79 = self.tableWidget_produseInTermen.horizontalHeaderItem(3)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem80 = self.tableWidget_produseInTermen.horizontalHeaderItem(4)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem81 = self.tableWidget_produseInTermen.horizontalHeaderItem(5)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem82 = self.tableWidget_produseInTermen.horizontalHeaderItem(6)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem83 = self.tableWidget_produseInTermen.horizontalHeaderItem(7)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        self.pushButton_goHome_13.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_25.setText(QCoreApplication.translate("MainWindow", u"Lista cu produsele din amanet care se afla in asteptare(5 zile de la expirare):", None))
        self.pushButton_goHome_14.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem84 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(0)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem85 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(1)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Observatii", None));
        ___qtablewidgetitem86 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(2)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem87 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(3)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem88 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(4)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem89 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(5)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem90 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(6)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem91 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(7)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem92 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(8)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Data expirare initiala", None));
        ___qtablewidgetitem93 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(9)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Data prelungire", None));
        ___qtablewidgetitem94 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(10)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Nr. zile prelungite", None));
        ___qtablewidgetitem95 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(11)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Comision prelungire", None));
        ___qtablewidgetitem96 = self.tableWidget_produseInAsteptare.horizontalHeaderItem(12)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Total de restituit dupa prelungire", None));
        self.pushButton_goHome_17.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_27.setText(QCoreApplication.translate("MainWindow", u"Lista cu produsele din amanet care au fost prelungite:", None))
        self.pushButton_goHome_18.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem97 = self.tableWidget_produsePrelungite.horizontalHeaderItem(0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem98 = self.tableWidget_produsePrelungite.horizontalHeaderItem(1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Observatii", None));
        ___qtablewidgetitem99 = self.tableWidget_produsePrelungite.horizontalHeaderItem(2)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem100 = self.tableWidget_produsePrelungite.horizontalHeaderItem(3)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem101 = self.tableWidget_produsePrelungite.horizontalHeaderItem(4)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem102 = self.tableWidget_produsePrelungite.horizontalHeaderItem(5)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem103 = self.tableWidget_produsePrelungite.horizontalHeaderItem(6)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem104 = self.tableWidget_produsePrelungite.horizontalHeaderItem(7)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem105 = self.tableWidget_produsePrelungite.horizontalHeaderItem(8)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Data expirare initiala", None));
        ___qtablewidgetitem106 = self.tableWidget_produsePrelungite.horizontalHeaderItem(9)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Data prelungire", None));
        ___qtablewidgetitem107 = self.tableWidget_produsePrelungite.horizontalHeaderItem(10)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Nr. zile prelungite", None));
        ___qtablewidgetitem108 = self.tableWidget_produsePrelungite.horizontalHeaderItem(11)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Comision prelungire", None));
        ___qtablewidgetitem109 = self.tableWidget_produsePrelungite.horizontalHeaderItem(12)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Total de restituit dupa prelungire", None));
        self.pushButton_goHome_19.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_42.setText(QCoreApplication.translate("MainWindow", u"Lista cu produsele din amanet cu termenul expirat:", None))
        self.pushButton_goHome_20.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem110 = self.tableWidget_produseExpirate.horizontalHeaderItem(0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem111 = self.tableWidget_produseExpirate.horizontalHeaderItem(1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"Observatii", None));
        ___qtablewidgetitem112 = self.tableWidget_produseExpirate.horizontalHeaderItem(2)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem113 = self.tableWidget_produseExpirate.horizontalHeaderItem(3)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem114 = self.tableWidget_produseExpirate.horizontalHeaderItem(4)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem115 = self.tableWidget_produseExpirate.horizontalHeaderItem(5)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem116 = self.tableWidget_produseExpirate.horizontalHeaderItem(6)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem117 = self.tableWidget_produseExpirate.horizontalHeaderItem(7)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem118 = self.tableWidget_produseExpirate.horizontalHeaderItem(8)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Data expirare initiala", None));
        ___qtablewidgetitem119 = self.tableWidget_produseExpirate.horizontalHeaderItem(9)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"Data prelungire", None));
        ___qtablewidgetitem120 = self.tableWidget_produseExpirate.horizontalHeaderItem(10)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Nr. zile prelungite", None));
        ___qtablewidgetitem121 = self.tableWidget_produseExpirate.horizontalHeaderItem(11)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"Comision prelungire", None));
        ___qtablewidgetitem122 = self.tableWidget_produseExpirate.horizontalHeaderItem(12)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Total de restituit dupa prelungire", None));
        self.pushButton_goHome_21.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_43.setText(QCoreApplication.translate("MainWindow", u"Lista cu produsele din amanet restituite clientilor:", None))
        self.pushButton_goHome_22.setText(QCoreApplication.translate("MainWindow", u">", None))
        ___qtablewidgetitem123 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(0)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem124 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(1)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"Observatii", None));
        ___qtablewidgetitem125 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(2)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Nr. contract", None));
        ___qtablewidgetitem126 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(3)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"Data intrare", None));
        ___qtablewidgetitem127 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(4)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"Data expirare", None));
        ___qtablewidgetitem128 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(5)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem129 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(6)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"Comision", None));
        ___qtablewidgetitem130 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(7)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem131 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(8)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"Data expirare initiala", None));
        ___qtablewidgetitem132 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(9)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"Data prelungire", None));
        ___qtablewidgetitem133 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(10)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"Nr. zile prelungite", None));
        ___qtablewidgetitem134 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(11)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"Comision prelungire", None));
        ___qtablewidgetitem135 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(12)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"Total de restituit dupa prelungire", None));
        ___qtablewidgetitem136 = self.tableWidget_produseLichidateClient.horizontalHeaderItem(13)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"Data lichidare", None));
        self.pushButton_maiMultiClientiGasitiOK_4.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_goHome_27.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_49.setText(QCoreApplication.translate("MainWindow", u"Produse de la furnizor", None))
        self.pushButton_goHome_28.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_dateClient_6.setText(QCoreApplication.translate("MainWindow", u"Introduceti date produs:", None))
        self.pushButton_goHome_31.setText(QCoreApplication.translate("MainWindow", u"+", None))
        ___qtablewidgetitem137 = self.tableWidget_produseLichidateClient_8.horizontalHeaderItem(0)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem138 = self.tableWidget_produseLichidateClient_8.horizontalHeaderItem(1)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"Cod produs", None));
        ___qtablewidgetitem139 = self.tableWidget_produseLichidateClient_8.horizontalHeaderItem(2)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"Cantitate factura", None));
        ___qtablewidgetitem140 = self.tableWidget_produseLichidateClient_8.horizontalHeaderItem(3)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"Cantitate primita", None));
        ___qtablewidgetitem141 = self.tableWidget_produseLichidateClient_8.horizontalHeaderItem(4)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"Pret la achizitie", None));
        ___qtablewidgetitem142 = self.tableWidget_produseLichidateClient_8.horizontalHeaderItem(5)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"Pret la vanzare", None));
        self.label_NumarCI_9.setText(QCoreApplication.translate("MainWindow", u"Numar factura", None))
        self.lineEdit_PrenumeClient_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_NumarCI_10.setText(QCoreApplication.translate("MainWindow", u"Nume furnizor", None))
        self.lineEdit_SerieCI_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"fiph12", None))
        self.pushButton_finalizareIncheiereContract_5.setText(QCoreApplication.translate("MainWindow", u"Finalizare", None))
        ___qtablewidgetitem143 = self.tableWidget_produseLichidateClient_3.horizontalHeaderItem(0)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem144 = self.tableWidget_produseLichidateClient_3.horizontalHeaderItem(1)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"Cod produs", None));
        ___qtablewidgetitem145 = self.tableWidget_produseLichidateClient_3.horizontalHeaderItem(2)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"Pret", None));
        ___qtablewidgetitem146 = self.tableWidget_produseLichidateClient_3.horizontalHeaderItem(3)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"Stoc", None));
        self.pushButton_goHome_23.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_finalizareIncheiereContract_2.setText(QCoreApplication.translate("MainWindow", u"Vinde produs", None))
        self.pushButton_goHome_32.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.label_textSusCercMijloc_51.setText(QCoreApplication.translate("MainWindow", u"Produse provenite din amanet", None))
        self.pushButton_goHome_33.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_dateClient_7.setText(QCoreApplication.translate("MainWindow", u"Introduceti pretul de vanzare pentru fiecare produs din tabelul de mai jos:", None))
        ___qtablewidgetitem147 = self.tableWidget_produseLichidateClient_6.horizontalHeaderItem(0)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"Nr contract", None));
        ___qtablewidgetitem148 = self.tableWidget_produseLichidateClient_6.horizontalHeaderItem(1)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem149 = self.tableWidget_produseLichidateClient_6.horizontalHeaderItem(2)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"Observatii", None));
        ___qtablewidgetitem150 = self.tableWidget_produseLichidateClient_6.horizontalHeaderItem(3)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"Suma imprumutata", None));
        ___qtablewidgetitem151 = self.tableWidget_produseLichidateClient_6.horizontalHeaderItem(4)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"Total de restituit", None));
        ___qtablewidgetitem152 = self.tableWidget_produseLichidateClient_6.horizontalHeaderItem(5)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"Pret de vanzare", None));
        self.pushButton_finalizareIncheiereContract_8.setText(QCoreApplication.translate("MainWindow", u"Adauga produs", None))
        ___qtablewidgetitem153 = self.tableWidget_produseLichidateClient_5.horizontalHeaderItem(0)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"Denumire produs", None));
        ___qtablewidgetitem154 = self.tableWidget_produseLichidateClient_5.horizontalHeaderItem(1)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"Pret", None));
        self.pushButton_goHome_25.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_finalizareIncheiereContract_7.setText(QCoreApplication.translate("MainWindow", u"Vinde produs", None))
        self.label_textSusCercMijloc_52.setText(QCoreApplication.translate("MainWindow", u"Vanzare produse", None))
        self.label_dateClient_15.setText(QCoreApplication.translate("MainWindow", u"Detalii vanzare produs:", None))
        self.label_Nume_6.setText(QCoreApplication.translate("MainWindow", u"Denumire produs :", None))
        self.lineEdit_NumeClient_5.setPlaceholderText("")
        self.label_Nume_7.setText(QCoreApplication.translate("MainWindow", u"Observatii:", None))
        self.lineEdit_NumeClient_6.setPlaceholderText("")
        self.label_SerieCI_6.setText(QCoreApplication.translate("MainWindow", u"Pret vanzare/bucata:", None))
        self.label_SerieCI_7.setText(QCoreApplication.translate("MainWindow", u"Pret vanzare:", None))
        self.label_NumarCI_7.setText(QCoreApplication.translate("MainWindow", u"Reducere:", None))
        self.lineEdit_PrenumeClient_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_PrenumeClient_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_dateClient_16.setText(QCoreApplication.translate("MainWindow", u"Detalii client:", None))
        self.label_CNP_3.setText(QCoreApplication.translate("MainWindow", u"Serie Nr C.I/Reg.com:", None))
        self.lineEdit_CNP_3.setText("")
        self.lineEdit_CNP_3.setPlaceholderText("")
        self.lineEdit_CNP_2.setPlaceholderText("")
        self.label_CNP_2.setText(QCoreApplication.translate("MainWindow", u"CNP/CUI", None))
        self.lineEdit_NumeClient_2.setPlaceholderText("")
        self.lineEdit_Adresa_2.setPlaceholderText("")
        self.label_Adresa_2.setText(QCoreApplication.translate("MainWindow", u"Adresa", None))
        self.label_Telefon_2.setText(QCoreApplication.translate("MainWindow", u"Telefon", None))
        self.lineEdit_Telefon_2.setPlaceholderText("")
        self.label_Email_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_Email_2.setPlaceholderText("")
        self.label_Nume_3.setText(QCoreApplication.translate("MainWindow", u"Nume complet:", None))
        self.pushButton_goHome_26.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_finalizareIncheiereContract_10.setText(QCoreApplication.translate("MainWindow", u"Finalizeaza vanzare", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Crafted by: Cyber-Octopus", None))
    # retranslateUi

