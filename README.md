# learning pyside6

##  install pyside6

recomand python 3.7+ 
(lower than v3.7 recomand using pyqt5)

``` bash
pip install pyside6
```
## vscode plugin

install `qt for python`


## using a simple button

learning how to handle signals and slots

create a button that logs the button clicked.message to the python console each time we click.

**decorator:**

``` python
def hello_plus(func):# func menas hello funciton
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

``` 

output:
``` bash
hello plus
args: (1, 2, 3)
args[0]: 1
args[1]: 1
args[2]: 1
kwargs.get('v1'): 200
kwargs.get('v2'): 100
1 2 3
```


**sys.argv**

sys.argv is an arg of command line from sys module

``` python
import sys
print(sys.argv)
```

command line

``` bash
button.py hello sys_argv
# ouput 
['.\\02_Using_a_SimpleButton\\button.py', 'hello', 'sys_argv']
```

## 03 Signals and Slots

due to the nature of Qt, QObject require a way to communicate, so the slots and gisnal wasborn.

this sound like callback function. but there ar essential differences that make it an unintuitive approach, like ensuring the type correctness of callback arguments, and some others.

you can create any signal to connect sloat.

``` python
signal1 = Signal(int)  # Python types
signal2 = Signal(QUrl)  # Qt Types
signal3 = Signal(int, str, int)  # more than one type
signal4 = Signal((float,), (QDate,))  # optional types
```

## 04 Creating_a_Dialog_Application

``` python
class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent) # 显式调用， 多继承的时候使用， super为什么传递类还需要传递self对象， 对象和类同时确定才能具体确定。
    
    def __init__(self, parent=None):
        super().__init__(parent) # 单继承的时候二者无区别
```

## 05 Table_Widget

``` python
class Tabl_demo(QTableWidget):
    colors = [("Red", "#FF0000"),
              ("Green", "#00FF00"),
              ("Blue", "#0000FF"),
              ("Black", "#000000"),
              ("White", "#FFFFFF"),
              ("Electric Green", "#41CD52"),
              ("Dark Blue", "#222840"),
              ("Yellow", "#F9E56d")]

    def __init__(self, parent=None):
        # 这里为什么不需要self.item_name, 因为这里只是局部使用的，不需要存储在对象中，对象中使用self前缀的变量表示可以共享访问.

        for i, (name, code) in enumerate(self.colors):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)
            item_color = QTableWidgetItem()
            item_color.setBackground(self.get_rgb_from_hex(code))
            self.setItem(i, 0, item_name)
            self.setItem(i, 1, item_code)
            self.setItem(i, 2, item_color)
``` 

## 06 Tree_Widget

easy demo

## 07 QtDesigner

use QtDesinger to desing ui and slot we can focus on logic developing.

![](https://raw.githubusercontent.com/fly-t/images/main/blog/README-2023-11-25-23-49-18.png)

1. push an button on window. 
2. create slot(key:F4[edit slot], key:F3[exit edit slot] )

3. uic

![](https://raw.githubusercontent.com/fly-t/images/main/blog/README-2023-11-25-23-51-44.png)

4. then you will see the ui of python file.

