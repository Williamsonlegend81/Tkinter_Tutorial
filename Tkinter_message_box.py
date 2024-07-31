from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Tkinter Tutorials")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my Popup!","Hello World!")
    if response==1:
        Label(root,text="You clicked Yes!").pack()
    else:
        Label(root,text="You clicked No!").pack()

Button(root,text="Pop Up",command=popup).pack()

root.mainloop()