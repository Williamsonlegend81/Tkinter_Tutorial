from tkinter import *

def myClick():
    myLabel = Label(root,text="Look I clicked button")
    myLabel.pack()
root = Tk()
myButton = Button(root,text="Click me!",command=lambda:myClick(),fg="blue",bg="yellow")

myButton.pack()
root.mainloop()