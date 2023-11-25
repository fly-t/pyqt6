import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (QApplication, QTableWidget,
                               QTableWidgetItem)


class Table_demo(QTableWidget):
    colors = [("Red", "#FF0000"),
              ("Green", "#00FF00"),
              ("Blue", "#0000FF"),
              ("Black", "#000000"),
              ("White", "#FFFFFF"),
              ("Electric Green", "#41CD52"),
              ("Dark Blue", "#222840"),
              ("Yellow", "#F9E56d")]

    def __init__(self, parent=None):
        super(Table_demo, self).__init__(parent)
        # Create widgets

        self.setRowCount(len(self.colors))
        self.setColumnCount(len(self.colors[0]) + 1)
        self.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

        for i, (name, code) in enumerate(self.colors):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)
            item_color = QTableWidgetItem()
            item_color.setBackground(self.get_rgb_from_hex(code))
            self.setItem(i, 0, item_name)
            self.setItem(i, 1, item_code)
            self.setItem(i, 2, item_color)

    def get_rgb_from_hex(self, code):
        code_hex = code.replace("#", "")
        rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
        return QColor.fromRgb(rgb[0], rgb[1], rgb[2])


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)  
    # Create and show the form
    table1 = Table_demo()
    table1.show()
    # Run the main Qt loop
    sys.exit(app.exec())
