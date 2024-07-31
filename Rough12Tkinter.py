from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk()

def open():
    global myImg
    root.filename = filedialog.askopenfilename(initialdir="E:/Tkinter Tutorial/Pokemon/Grass", title="Select A File", filetypes=(("png files","*.png"),("all files","*.*")))
    myImg = ImageTk.PhotoImage(Image.open(root.filename))
    my_Label = Label(root, image=myImg)
    my_Label.pack()
my_btn = Button(root, text="Open file", command=open)
my_btn.pack()

root.mainloop()