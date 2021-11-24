import tkinter as tk

class Painttk(object):
    def __init__(self):
        #Initializing selections for color and shape
        self._currentshape = None
        self._currentcolor = None
        #Setting up main window
        self._root = tk.Tk()
        self._root.title("Painttk")
        self._root.geometry("500x500")
        self._root.columnconfigure(0, weight= 1)
        self._root.columnconfigure(1, weight= 2)
        self._root.rowconfigure([0,1], weight= 1)
        #Laying out shape selection menu
        self._shapeselect = tk.Frame(self._root)
        self._shapeselect.grid(column=0, row=0)
        #Adding the widgets to the shape selection menu
        self._shapetitle = tk.Label(self._shapeselect,text="Shapes")
        self._shapetitle.grid(column=0, row=0, columnspan= 3)
        self._rectanglebutton = tk.Button(master = self._shapeselect, text="Rectangle", relief=tk.RAISED, command=lambda shape = "rectangle" : self.changeShape(shape))
        self._rectanglebutton.grid(column=0, row=1)
        self._ovalbutton = tk.Button(master = self._shapeselect, text="Oval", relief=tk.RAISED,command=lambda shape = "oval" : self.changeShape(shape))
        self._ovalbutton.grid(column=1, row=1)
        self._linebutton = tk.Button(master = self._shapeselect, text="Line", relief=tk.RAISED, command=lambda shape = "line" : self.changeShape(shape))
        self._linebutton.grid(column=2, row=1)
        self._labelcurrentshape = tk.Label(master=self._shapeselect, text=("Current selection: " + str(self._currentshape)))
        self._labelcurrentshape.grid(column=0, row = 2, columnspan= 3)
        #Laying out color selection menu
        self._colorselect = tk.Frame(self._root)
        self._colorselect.grid(column=0, row=1)
        #Adding the widgets to the shape selection menu
        self._colortitle = tk.Label(self._colorselect,text="Colors")
        self._colortitle.grid(column=0, row=0, columnspan=3)
        self._bluebutton = tk.Button(master = self._colorselect, text="Blue", relief=tk.RAISED, command=lambda color = "blue" : self.changeColor(color))
        self._bluebutton.grid(column=0, row=1)
        self._redbutton = tk.Button(master = self._colorselect, text="Red", relief=tk.RAISED, command=lambda color = "red" : self.changeColor(color))
        self._redbutton.grid(column=1, row=1)
        self._yellowbutton = tk.Button(master = self._colorselect, text="Yellow", relief=tk.RAISED, command=lambda color = "yellow" : self.changeColor(color))
        self._yellowbutton.grid(column=2, row=1)
        self._labelcurrentcolor = tk.Label(master=self._colorselect, text=("Current selection: " + str(self._currentcolor)))
        self._labelcurrentcolor.grid(column=0, row = 2, columnspan= 3)
        #Layout canvas
        self._drawingarea = tk.Canvas(master=self._root, bg ="white", height = 300, width=300)
        self._drawingarea.grid(column=1, row= 0)
        


        self._root.mainloop()

    def changeShape(self, shape):
        self._currentshape = shape
        self._labelcurrentshape['text'] ='Current selection: ' + shape


    def changeColor(self, color):
        self._currentcolor = color
        self._labelcurrentcolor['text'] = 'Current selection: ' + color



app = Painttk()