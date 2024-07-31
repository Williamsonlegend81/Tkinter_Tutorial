from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter Tutorials")
root.geometry("400x400")

def clicked():
    global myLabel
    myLabel = Label(root,text=var.get())
    myLabel.pack()
var = StringVar()
c = Checkbutton(root,text="Check this box, I dare you!", variable=var,onvalue="Rudra Desai is still great",offvalue="Rudra Desai is great")
c.deselect()
c.pack()
myButton = Button(root,text="Show Selection",command=clicked).pack()

root.mainloop()