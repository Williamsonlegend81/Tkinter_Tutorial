from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorials")
root.geometry("400x400")
# Drop down boxes

def Display():
    myLabel = Label(root,text=clicked.get())
    myLabel.pack()
Options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
clicked = StringVar()
clicked.set(Options[0])
drop = OptionMenu(root,clicked,*Options)
drop.pack()

myButton = Button(root,text="Display selected option",command=Display)
myButton.pack()

root.mainloop()

