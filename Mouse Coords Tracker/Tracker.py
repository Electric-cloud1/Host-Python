
# ==============================================================================
# Simple Program which gets the coordinates of your mouse real-time
# Created by: ThunderZ
# Github Link: https://github.com/ThunderZ-Coder-A
# ==============================================================================

import pyautogui
import time
from time import sleep
import keyboard

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, Qt, QEvent, QTimer, Slot
from PySide2.QtWidgets import *
import sys

from ui_Mouse_Coords import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setMouseTracking(True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.PositnStr = ''
        self.EndProcess = False
        self.ContinueProcessing = True

        self.ui.Github_link.setText(
            "Github Link: https://github.com/ThunderZ-Coder-A")

        self.DelaydLaunch = QTimer()
        self.DelaydLaunch.singleShot(2000, self.StartTracking)

        self.ui.Minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.Close.clicked.connect(lambda: self.close())

        screen_resolution = MainEventThread.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        print(width)
        print(height)

        self.ui.Screen_res.setText(
            f"Current Screen Resolution: {width}x{height}")

    def StartTracking(self):
        print('Starting Tracker')

        self.ProcessDelay = QTimer()
        self.ProcessDelay.timeout.connect(self.ShowMousePosition)

        try:

            self.ProcessDelay.start(500)
            while self.ContinueProcessing:
                x, y = pyautogui.position()

                self.strPositn = ''
                self.strPositn += 'Mouse X: '
                self.strPositn += str(x).rjust(4)
                self.strPositn += ' Mouse Y: '
                self.strPositn += str(y).rjust(4)

                QCoreApplication.processEvents()

                time.sleep(0.750)
                if self.EndProcess:

                    self.ProcessDelay.stop()
                    self.ContinueProcessing = False
        except KeyboardInterrupt:

            print('Error Occurred Program Aborting')

    def ShowMousePosition(self):
        if self.EndProcess:
            print("ENDING")

        self.ui.Mouse_Coords.setText(self.strPositn)

    def closeEvent(self, event):

        print('Closing')
        self.EndProcess = True
        QCoreApplication.processEvents()
        event.accept()


MainEventThread = QApplication([])

MainApp = MainWindow()
MainApp.show()


sys(MainEventThread.exec_())
