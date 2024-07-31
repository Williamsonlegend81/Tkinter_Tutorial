from tkinter import *

def myClick():
    myLabel = Label(root,text=f"Your name is {e.get()}")
    myLabel.pack()
root = Tk()
e = Entry(root,width=50)
e.insert(0, "Enter your name:")
e.pack()

myButton = Button(root,text="Enter your name",command=myClick)
myButton.pack()
root.mainloop()