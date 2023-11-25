import sys
from typing import Optional
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem


class TreeWidgeDemo(QTreeWidget):

    data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
            "Project B": ["file_b.csv", "photo.jpg"],
            "Project C": []}

    def __init__(self, parent=None):
        super(TreeWidgeDemo, self).__init__(parent)
        self.setColumnCount(2)
        self.setHeaderLabels(["Name", "Type"])

        items = []

        for key, values in self.data.items():
            item = QTreeWidgetItem([key])
            for value in values:
                ext = value.split(".")[-1].upper()
                child = QTreeWidgetItem([value, ext])
                item.addChild(child)
            items.append(item)

        self.insertTopLevelItems(0, items)


if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    tree = TreeWidgeDemo()
    tree.show()
    # Run the main Qt loop
    sys.exit(app.exec())
