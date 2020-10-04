# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'Mouse_CoordskhoKAc.ui'
##
# Created by: Qt User Interface Compiler version 5.15.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import Icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(498, 234)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(19, 22, 39);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Mouse_Coords = QLabel(self.frame)
        self.Mouse_Coords.setObjectName(u"Mouse_Coords")
        self.Mouse_Coords.setGeometry(QRect(10, 180, 461, 31))
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(9)
        self.Mouse_Coords.setFont(font)
        self.Mouse_Coords.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Screen_res = QLabel(self.frame)
        self.Screen_res.setObjectName(u"Screen_res")
        self.Screen_res.setGeometry(QRect(100, 150, 331, 21))
        self.Screen_res.setFont(font)
        self.Screen_res.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Close = QPushButton(self.frame)
        self.Close.setObjectName(u"Close")
        self.Close.setGeometry(QRect(430, 0, 51, 31))
        font1 = QFont()
        font1.setPointSize(6)
        self.Close.setFont(font1)
        self.Close.setStyleSheet(u"QPushButton {	\n"
                                 "	border: none;\n"
                                 "	background-color: transparent;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "	background-color: rgb(64, 63, 95);\n"
                                 "}\n"
                                 "QPushButton:pressed {	\n"
                                 "	\n"
                                 "	background-color: rgb(177, 68, 48);\n"
                                 "}")
        icon = QIcon()
        icon.addFile(u":/IconsC/Icons/cil-x.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.Close.setIcon(icon)
        self.Close.setIconSize(QSize(15, 15))
        self.Minimize = QPushButton(self.frame)
        self.Minimize.setObjectName(u"Minimize")
        self.Minimize.setGeometry(QRect(390, 0, 41, 31))
        self.Minimize.setFont(font1)
        self.Minimize.setStyleSheet(u"QPushButton {	\n"
                                    "	border: none;\n"
                                    "	background-color: transparent;\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "	background-color: rgb(64, 63, 95);\n"
                                    "}\n"
                                    "QPushButton:pressed {	\n"
                                    "	background-color: rgb(85, 170, 255);\n"
                                    "}")
        icon1 = QIcon()
        icon1.addFile(u":/IconsC/Icons/cil-window-minimize.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.Minimize.setIcon(icon1)
        self.Minimize.setIconSize(QSize(15, 15))
        self.Image = QLabel(self.frame)
        self.Image.setObjectName(u"Image")
        self.Image.setGeometry(QRect(180, 20, 121, 61))
        self.Image.setPixmap(QPixmap(u":/IconsC/Icons/Mouse_cursor_image.png"))
        self.Title = QLabel(self.frame)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(110, 85, 261, 21))
        font2 = QFont()
        font2.setPointSize(9)
        self.Title.setFont(font2)
        self.Title.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Title.setAlignment(Qt.AlignCenter)
        self.Github_link = QLabel(self.frame)
        self.Github_link.setObjectName(u"Github_link")
        self.Github_link.setGeometry(QRect(0, 120, 471, 21))
        self.Github_link.setFont(font2)
        self.Github_link.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Github_link.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.Mouse_Coords.setText(QCoreApplication.translate(
            "MainWindow", u"Mouse X:         Mouse Y:", None))
        self.Screen_res.setText(QCoreApplication.translate(
            "MainWindow", u"Current Screen Resolution: ", None))
        self.Close.setText("")
        self.Minimize.setText("")
        self.Image.setText("")
        self.Title.setText(QCoreApplication.translate(
            "MainWindow", u"Thunderz's Mouse Tracking Tool", None))
        self.Github_link.setText(QCoreApplication.translate(
            "MainWindow", u"Github Link:                          ", None))
    # retranslateUi
