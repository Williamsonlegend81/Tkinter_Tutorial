from tkinter import *

root = Tk()

option = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
clicked = StringVar()
drop = OptionMenu(root, clicked, *option)
drop.pack()
clicked.set(option[0])
def Show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()
myButton = Button(root, text="Show selection", command=Show)
myButton.pack()

root.mainloop()