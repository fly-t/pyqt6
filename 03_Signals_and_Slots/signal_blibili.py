import sys

from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,\
                                QLineEdit, QPushButton
from PySide6.QtCore import Signal

class MyWindw(QWidget):

    signal_sendData2subWindow = Signal(object)

    def __init__(self):
        super(MyWindw, self).__init__()
        self.lineEdit_main_1 =  QLineEdit()
        self.pushButton_1 = QPushButton("发送到子窗口")
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEdit_main_1)
        self.mainLayout.addWidget(self.pushButton_1)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        # sub window
        self.subwindow = SubWindow(self)  # 通过self传递主窗口控件到子窗口
        self.subwindow.show()

        self.signal_sendData2subWindow.connect(self.subwindow.lineEdit_1.setText)
        self.pushButton_1.clicked.connect(self.send_value)
        

    def send_value(self):
        text = self.lineEdit_main_1.text()
        self.signal_sendData2subWindow.emit(text)

        


class SubWindow(QWidget):
    signal_sendData2mainWindow = Signal(object)

    def __init__(self,parent=None):
        super().__init__()
        self.parent = parent  # 保存parent变量
        self.lineEdit_1 = QLineEdit()
        self.pushButton_1 = QPushButton("发送到主窗口")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lineEdit_1)
        self.mainLayout.addWidget(self.pushButton_1)
        self.setLayout(self.mainLayout)
        self.bind()

    def bind(self):
        self.signal_sendData2mainWindow.connect(
            self.parent.lineEdit_main_1.setText)  # 通过parent变量访问mainwindow的控件
        self.pushButton_1.clicked.connect(self.send_value)   

    def send_value(self):
        text = self.lineEdit_1.text()
        self.signal_sendData2mainWindow.emit(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # main window
    w = MyWindw()
    w.show()
    app.exec()