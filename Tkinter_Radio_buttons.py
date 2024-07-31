from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorials")

r = IntVar()
r.set("3")

def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()
Radiobutton(root,text="Option 1",variable=r,value=1).pack()
Radiobutton(root,text="Option 2",variable=r,value=2).pack()
Radiobutton(root,text="Option 3",variable=r,value=3).pack()

myButton = Button(root,text="Click me!", command=lambda: clicked(r.get()))
myButton.pack()
root.mainloop()