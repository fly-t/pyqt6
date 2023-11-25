import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# create a function that logs the message to console
@Slot()   # decorator that identifies a function as a slot.
def slot_print_hello():
    print("hello")



def hello_plus(func):
    def wrapper(*args, **kwargs):
        print("hello plus")
        
        print("args:", args)
        print("args[0]:", args[0])
        print("args[1]:", args[1])
        print("args[2]:", args[2])

        print("kwargs.get('v1'):",kwargs.get("v1"))
        print("kwargs.get('v2'):", kwargs.get("v2"))
        return func(*args)
    return wrapper

@hello_plus
def hello(a,b,c):
    print(a,b,c)

if __name__ =="__main__":
    hello(1, 2, 3, v1=200, v2=100)
