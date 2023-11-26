import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QPushButton,\
                            QWidget, QListWidget, QListWidgetItem, \
                            QVBoxLayout, QHBoxLayout


class Widget(QWidget):
    _placeholder = "Hello, World!"
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)

        menu_widget = QListWidget()
        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            menu_widget.addItem(item)

        text_widget = QLabel(self._placeholder)
        button = QPushButton("Something")

        content_layout = QVBoxLayout()
        content_layout.addWidget(text_widget)
        content_layout.addWidget(button)
        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(menu_widget, 1)
        layout.addWidget(main_widget, 4)
        self.setLayout(layout)

import os
if __name__ == "__main__":
    app = QApplication()

    w = Widget()
    w.show()
    # 绝对路径
    # style_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.qss")
    # 查看当前运行位置， vscode 默认运行位置是打开的文件夹位置， 不是当前文件的位置
    # print(os.getcwd())
    # https://doc.qt.io/qt-6/stylesheet-examples.html
    with open("./09_Styling_the_Widgets_Application/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
