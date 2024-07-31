from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learning Tkinter")

def fn2():
    global myImg
    top = Toplevel()
    top.title("My Second Window")
    myImg = ImageTk.PhotoImage(Image.open("Pokemon/Grass/001_Bulbasaur.png"))
    lb2 = Label(top, image=myImg)
    lb2.pack()
    btn2 = Button(top, text="Exit Window", command=top.destroy)
    btn2.pack()
btn = Button(root, text="Open Second Window", command=fn2)
btn.pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()