import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# create a function that logs the message to console
@Slot()   # decorator that identifies a function as a slot.
def slot_print_hello():
    print("hello")

# now we must create the QApplication to run GUI
# sys.argv is an arg of command line from sys module
app = QApplication(sys.argv)  # create app must befor a qwidget

# Create a button
button = QPushButton("Click me")
# Connect the button to the function
button.clicked.connect(slot_print_hello)
# Show the button
button.show()



if __name__ =="__main__":
    # Run the main Qt loop
    app.exec()
