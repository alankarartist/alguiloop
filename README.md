# AlGUILoop
AlGUILoop is to use while and for loops without blocking the GUI. This is currently for Tkinter and PyQT.

## Installation
You can install AlGUILoop from [PyPI](https://pypi.org/project/alguiloop/):
```pip install alguiloop```
The AlGUILoop supports Python 3.6 and above.

## Usage
There are following examples to use while and for loops without blocking the GUI using AlGUILoop:-
```
"""
This script uses a while loop that lets to toggle switch while the GUI(tkinter) is still responsive.
Running this script outputs
ON: Switch 1
ON: Switch 2
ON: Switch 3
OFF: Switch 1
OFF: Switch 2
OFF: Switch 3
ON: Switch 1
ON: Switch 2
ON: Switch 3
CLICKED
OFF: Switch 1
OFF: Switch 2
OFF: Switch 3
CLICKED
"""
from tkinter import *
from AlGUILoop import AlGUILoop 

@AlGUILoop
def toggleSwitch(argument):
    while 1:
        print("ON: " + argument)
        yield 0.5 # time to wait
        print("OFF: " + argument)
        yield 0.5

root = Tk()

# you can run several loops at once:
toggleSwitch(root, 'Switch 1')
toggleSwitch(root, 'Switch 2')
toggleSwitch(root, 'Switch 3')

# add a responsive button
def click():
    print('CLICKED')
Button(root, command = click, text = 'CLICK HERE').pack(fill=X)

# start the GUI loop
root.mainloop()
```
```
"""
This script uses a while loop that lets to toggle switch while the GUI(tkinter) is still responsive. It shows how loops can be started and stopped when GUI is responsive.
# Running this script outputs
Switch ON
Switch OFF
Switch ON
Switch OFF
"""
from tkinter import *
from AlGUILoop import AlGUILoop, stopLoop 

class StartAndStoopLoop():
    def __init__(self):
        root = Tk()

        @AlGUILoop
        def toggleSwitch():
            while 1:
                print("Switch ON")
                yield 0.5 # time to wait
                print("Switch OFF")
                yield 0.5

        def start():
            self.generator = toggleSwitch(root)

        def stop():
            stopLoop(self.generator)

        # This button will start the loop
        b1 = Button(root, command = start, text = 'START')
        b1.pack(fill=X)

        # This button will stop the loop
        b2 = Button(root, command = stop, text = 'STOP')
        b2.pack(fill=X)

        root.mainloop()

if __name__ == "__main__":
    StartAndStoopLoop() 
```
```
"""
This script uses a while loop that lets to toggle switch while the GUI(PyQt5) is still responsive.
Running this script outputs
ON: Switch 1
ON: Switch 2
ON: Switch 3
OFF: Switch 1
OFF: Switch 2
OFF: Switch 3
CLICKED
ON: Switch 1
ON: Switch 2
ON: Switch 3
"""
from PyQt5 import QtWidgets
import sys
from AlGUILoop import AlGUILoop

@AlGUILoop
def toggleSwitch(argument):
    while 1:
        print("ON: " + argument)
        yield 0.5 # time to wait
        print("OFF: " + argument)
        yield 0.5

app = QtWidgets.QApplication(sys.argv)

# add a responsive button
def click():
    print('CLICKED')
window = QtWidgets.QPushButton()
window.setText('CLICK')
window.clicked.connect(click)
window.show()

# you can run several loops at once:
toggleSwitch(window, 'Switch 1')
toggleSwitch(window, 'Switch 2')
toggleSwitch(window, 'Switch 3')

sys.exit(app.exec_())
```
```
"""
This script uses a while loop that lets to toggle switch while the GUI(PyQt5) is still responsive. It shows how loops can be started and stopped when GUI is responsive.
# Running this script outputs
Switch ON
Switch OFF
Switch ON
Switch OFF
"""
from PyQt5.QtWidgets import *
import sys
from AlGUILoop import AlGUILoop, stopLoop 

class StartAndStoopLoop(QWidget):
    def __init__(self):
        super().__init__()
        self.w = QVBoxLayout(self)
        self.w.setContentsMargins(2, 2, 2, 2)
        self.w.setSpacing(0)
        self.w1 = QPushButton()
        self.w2 = QPushButton()
        self.w1.setText('START')
        self.w2.setText('STOP')
        self.w.addWidget(self.w1)
        self.w.addWidget(self.w2)
        self.w1.clicked.connect(self.start)
        self.w2.clicked.connect(self.stop)
        self.show()

    @AlGUILoop
    def toggleSwitch(self):
        while 1:
            print("Switch ON")
            yield 0.5 # time to wait
            print("Switch OFF")
            yield 0.5

    def start(self):
        self.generator = self.toggleSwitch()

    def stop(self):
        stopLoop(self.generator)

if __name__ == "__main__" : 
    App = QApplication(sys.argv) 
    window = StartAndStoopLoop() 
    sys.exit(App.exec()) 
```

## License
© 2021 Alankar Singh
This repository is licensed under the MIT license. See LICENSE for details.
