from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Tkinter Tutorials")

def Open_Second_Window():
    global my_Img
    top = Toplevel()
    my_Img = ImageTk.PhotoImage(Image.open("Images/Blastoise.png"))
    MyLabel2 = Label(top,image=my_Img)
    myLabel = Label(top,text="Hello World")
    myLabel.pack()
    MyLabel2.pack()
    btn2 = Button(top,text="Close the window",command=top.destroy)
    btn2.pack()
Button_quit = Button(root,text="Exit Program",command=root.quit)
Button_quit.pack()
Btn = Button(root,text="Click to open second window",command=Open_Second_Window)
Btn.pack()
root.mainloop()