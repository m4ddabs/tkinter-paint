import tkinter as tk
from selectionmenu import Selectionmenu

class Painttk(object):
    def __init__(self):
        #Initializing selections for color,shape and click coordinates 
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        #Setting up main window
        self._root = tk.Tk()
        self._root.title("Painttk")
        self._root.geometry("500x500")
        self._root.columnconfigure(0, weight= 1)
        self._root.columnconfigure(1, weight= 2)
        self._root.rowconfigure([0,1], weight= 1)
        #Laying out shape selection menu
        self._shapemenu = Selectionmenu(master= self._root, title='Shapes', names=['rectangle', 'oval', 'line'])
        self._shapemenu.frame.grid(column=0, row=0)
        for i, name in enumerate(self._shapemenu.getNames()):
            self._shapemenu.addButton(name, col=i, row=1)
        #Laying out color selection menu
        self._colormenu = Selectionmenu(master=self._root,title='Colors', names=['blue','red','yellow'])
        self._colormenu.frame.grid(column=0, row = 1)
        #Adding the widgets to the shape selection menu
        for i, name in enumerate(self._colormenu.getNames()):
            self._colormenu.addButton(name, col=i, row=1)
        #Layout canvas
        self._drawingarea = tk.Canvas(master=self._root, bg ="white", height = 300, width=300)
        self._drawingarea.grid(column=1, row= 0)
        self._drawingarea.bind('<Button-1>', self.draw)
        


        self._root.mainloop()

    def draw(self, event):
        if self._shapemenu.currentselec == None or self._colormenu.currentselec == None:
            print("No color or shape selected")
            return
        self._x1 = event.x
        self._y1 = event.y
        self._drawingarea.unbind("<Button-1>")
        self._drawingarea.bind("<Button-1>", self.draw2)

    def draw2(self, event):
        self._x2 = event.x
        self._y2 = event.y
        #Here we are adjusting the coordinates according to where the user clicked
        if self._shapemenu.currentselec == 'rectangle' or self._shapemenu.currentselec == 'oval':
            if self._x1 - self._x2 > 0:
                a = self._x1 
                self._x1 = self._x2
                self._x2 = a
            if self._y1 - self._y2 > 0:
                b = self._y1
                self._y1 = self._y2
                self._y2 = b
        if self._shapemenu.currentselec == 'rectangle':
            self._drawingarea.create_rectangle(self._x1, self._y1, self._x2, self._y2, fill=self._colormenu.currentselec)
        if self._shapemenu.currentselec == 'oval':
            self._drawingarea.create_oval(self._x1, self._y1, self._x2, self._y2, fill=self._colormenu.currentselec)
        if self._shapemenu.currentselec == 'line':
            self._drawingarea.create_line(self._x1, self._y1, self._x2, self._y2, fill=self._colormenu.currentselec)
        self._drawingarea.unbind("<Button-1>")
        self._drawingarea.bind("<Button-1>", self.draw)


        
        



if __name__ == '__main__':
    app = Painttk()