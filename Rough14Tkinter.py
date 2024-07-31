from tkinter import *

root = Tk()
root.title("Learning Tkinter")

var = StringVar()
c = Checkbutton(root, text="Check this box!", variable=var, onvalue="Pizza", offvalue="Hamburger")
c.deselect()
c.pack()

def show():
    myLabel = Label(root, text=var.get())
    myLabel.pack()
myButton = Button(root, text="Show selection", command=show)
myButton.pack()
root.mainloop()