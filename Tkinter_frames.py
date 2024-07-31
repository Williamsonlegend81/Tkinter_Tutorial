from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Tkinter Tutorials")
frame = LabelFrame(root,text="This is a Frame...",padx=100,pady=100)
frame.pack(padx=100,pady=100)

b = Button(frame,text="Don't click here",command=root.quit)
b.pack()

root.mainloop()