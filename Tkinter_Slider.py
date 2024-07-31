from tkinter import *
from PIL import ImageTk,Image

root = Tk()
def slide(var):
    my_label = Label(root,text=horizontal.get())
    my_label.pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
root.title("Tkinter Tutorials")
root.geometry("400x400")   
vertical = Scale(root,from_=0,to=200)
vertical.pack()

horizontal = Scale(root,from_=0,to=200,orient=HORIZONTAL,command=slide)
horizontal.pack()

my_btn = Button(root,text="Click Me!",command=slide).pack()
root.mainloop()