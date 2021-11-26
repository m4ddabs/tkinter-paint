import tkinter as tk


class Selectionmenu(object):
    def __init__(self, master = None, title = 'Selection menu', names = []):
        if master == None:
            raise(ValueError('No master object passed for selection menu !'))
        if type(names) != list:
            raise(TypeError("names must be a list of strings !"))
        else:
            for name in names:
                if type(name) != str:
                    raise(TypeError("Names in name list must be of type string !"))
        self._master = master
        self._currentselec = None
        self._names = names
        self._frame = tk.Frame(master)
        self._title = tk.Label(self._frame,text=title)
        self._title.grid(column=0, row=0, columnspan= 3)
        self._buttons = []
        self._labelcurrentselec = tk.Label(master=self.frame, text=("Current selection: " + str(self._currentselec)))
        self._labelcurrentselec.grid(column=0, row = 2, columnspan= 3)

    def getMaster(self):
        return self._master

    
    def getTitle(self):
        return self._title

    def setTitle(self, title):
        self._title = title
    
    def getNames(self):
        return self._names

    def getFrame(self):
        return self._frame

    def getCurrentselec(self):
        return self._currentselec

    def __addName__(self, name):
        if type(name) != str: 
            raise(TypeError("name parameter must be a string !")) 
        if name not in self._names:
            self._names.append(name)

    def addButton(self, name, col=None, row=None):
        self.__addName__(name)
        button = tk.Button(master = self.frame, text=name, command=lambda name=name: self.__changeSelec__(name))
        self._buttons.append(button)
        if col == None or row == None:
            button.pack()
        else:
            info = self._labelcurrentselec.grid_info()
            if row == info['row']:
                self._labelcurrentselec.grid(info['column'], info['row'] + 1)
            button.grid(column=col, row=row)
    def getButton(self, name):
        if type(name) != str: 
            raise(TypeError("shape parameter must be a string !"))
        for button in self._buttons:
            if name == button['text']:
                return button
        print("This button does not exist !")

    def __changeSelec__(self, selec):
        self._currentselec = selec
        self._labelcurrentselec['text'] ='Current selection: ' + selec

    names = property(getNames, )
    title = property(getTitle, setTitle)
    master = property(getMaster, )
    frame = property(getFrame,)
    currentselec = property(getCurrentselec,)
