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

