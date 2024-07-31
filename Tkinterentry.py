from tkinter import *
root = Tk()

e = Entry(root,width=50)
e.pack()
e.insert(0, "Enter your name:")

def Clickme():
    myLabel = Label(root,text=f"Hello, {e.get()}")
    myLabel.pack()

myButton = Button(root,text="Enter Your Name",command=Clickme)
myButton.pack()
root.mainloop()