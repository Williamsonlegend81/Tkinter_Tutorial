from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Learning Tkinter")
vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide(var):
    myLabel = Label(root, text=var)
    myLabel.pack()
    root.geometry(f"{horizontal.get()}x400")
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide)
horizontal.pack()

btn = Button(root, text="Click here to display", command=slide)
btn.pack()
root.mainloop()