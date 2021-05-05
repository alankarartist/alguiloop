def tkinterafter(guiElement, waitTime, callThis):
    guiElement.after(waitTime, callThis)

def PyQT5QTimer(guiElement, waitTime, callThis):
    from PyQt5.QtCore import QTimer
    QTimer.singleShot(waitTime, callThis)

def anyTimer(guiElement, waitTime, callThis):
    if hasattr(guiElement, 'after'):
        tkinterafter(guiElement, waitTime, callThis)
    elif hasattr(guiElement, 'pyqtConfigure'):
        PyQT5QTimer(guiElement, waitTime, callThis)
    else:
        raise TypeError("Can not automatically detect which GUI this is.")

def loopGUI(guiElement, generator, startGUI):
    try:
        # generator yields the time to wait
        waitTime = next(generator)
    except StopIteration:
        pass
    else:
        if waitTime is None:
            # yield
            waitTime = 0
        else:
            # yield seconds
            waitTime = int(waitTime * 1000) # Tkinter works with milli seconds
        callThisAgain = lambda: loopGUI(guiElement, generator,
                                                   startGUI)
        startGUI(guiElement, waitTime, callThisAgain)

class AlGUILoop(object):
    
    def __init__(self, function, startGUI = anyTimer):
        """make a function to a AlGUILoop function
        The resulting function needs a gui element as first argument."""
        self.function = function
        self.__doc__ = function.__doc__
        self.__name__ = function.__name__
        self.startGUI = startGUI

    def __call__(self, guiElement, *args, **kw):
        generator = self.function(*args, **kw)
        loopGUI(guiElement, generator, self.startGUI)
        return generator

    def __get__(self, guiElement, cls):
        if guiElement is None:
            return self
        return lambda *args, **kw: self(guiElement, guiElement, *args, **kw)
        

def tkLoop(function):
    """a AlGUILoop for tkinter"""
    return AlGUILoop(function, tkinterafter)

def qt5Loop(function):
    """a AlGUILoop for PyQT5"""
    return AlGUILoop(function, PyQT5QTimer)

class StopLoopException(Exception):
    """This is raised if the loop shall stop"""
    pass

def stopLoop(generator):
    """stop the loop
    Generator is the return value of AlGUILoop."""
    try: generator.throw(StopLoopException())
    except StopLoopException: pass

__all__ = ['AlGUILoop', 'stopLoop', 'StopLoopException', 'tkLoop', 'qt5Loop']