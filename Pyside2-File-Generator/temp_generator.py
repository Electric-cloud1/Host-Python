
# ==============================================================================
# Program that generates an beautifully formatted file to get started with your Pyside2 Project
# with clear comments and imports and more functionality so it does not get  repetitive for the programmer
# ==============================================================================
# Created by: ThunderZ
# Github Link: https://github.com/ThunderZ-Coder-A
# ==============================================================================

directory = input("Enter The Directory of the file: ")
file_name = input("Enter the name of the file: ") + ".py"

file_name = f"\{file_name}"

raw_directory = r'{}'.format(directory)

raw_file_name = r'{}'.format(file_name)

Full_directory = raw_directory + raw_file_name

write1 = ('import sys\nfrom PySide2 import QtCore, QtGui, QtWidgets\nfrom PySide2.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent\nfrom PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient\nfrom PySide2.QtWidgets import *'

          '\n\n# ==> FILE-IMPORTS'
          '\nfrom filename import Ui_MainWindow'


          '\n\n# ===================================================================='
          '\n# MAIN WINDOW'
          '\n# ===================================================================='


          '\n\nclass MainWindow(QMainWindow):\n\tdef __init__(self):\n\t\tQMainWindow.__init__(self)\n\t\tself.ui = Ui_MainWindow()\n\t\tself.ui.setupUi(self)\n\n\t\t# ==> CALLS AND ARGUMENTS'

          '\n\n\n\t# ===================================================================='
          '\n\t#  MOVING WINDOW AND (CLOSE/ MINIMIZE/ MAXIMIZE WINDOW FUNCTIONS)'
          '\n\t# ===================================================================='

          '\n\n\t\tself.ui.Minimize_Btn.clicked.connect(lambda: self.showMinimized())'
          '\n\t\tself.ui.Restore_Btn.clicked.connect(lambda: self.showNormal())'
          '\n\t\tself.ui.Close_btn.clicked.connect(lambda: self.close())'

          '\n\n\tdef mousePressEvent(self, event):\n\t\tif event.button() == QtCore.Qt.LeftButton:\n\t\t\tself.offset = event.pos()\n\t\telse:\n\t\t\tsuper().mousePressEvent(event)'

          '\n\n\tdef mouseMoveEvent(self, event):'
          '\n\t\tif self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:'
          '\n\t\t\tself.move(self.pos() + event.pos() - self.offset)'
          '\n\t\telse:'
          '\n\t\t\tsuper().mouseMoveEvent(event)'

          '\n\n\tdef mouseReleaseEvent(self, event):'
          '\n\t\tself.offset=None'
          '\n\t\tsuper().mouseReleaseEvent(event)'


          ''


          '\n\n\n\t# ===================================================================='
          '\n\t# APP FUNCTIONS'
          '\n\t# ===================================================================='

          '\n\n\t# ==> Your-Sub-Heading'

          '\n\n\n\n\n\n# ===> SHOW THE WINDOW'
          '\napp = QApplication(sys.argv)\nwindow = MainWindow()\nwindow.show()\nsys.exit(app.exec_())')

with open(Full_directory, 'w') as f:
    f.write(write1)
