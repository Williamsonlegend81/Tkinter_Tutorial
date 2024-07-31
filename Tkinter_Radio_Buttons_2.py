from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorials")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]
def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()
pizza = StringVar()
pizza.set("Pepperoni")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

myButton = Button(root,text="Click me!",command=lambda: clicked(pizza.get()))
myButton.pack()
root.mainloop()