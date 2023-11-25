import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import *

from ui.ui_test import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
    # create the slot of QtDesinger slot(Key:F4 config)
    def slot1(self):
        print("click demo")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.setWindowTitle("Desinger Demo")
    win.show()
    app.exit(app.exec())
