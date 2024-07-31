from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def popup():
    response = messagebox.askyesno("This is my popup!", "Hello World")
    Label(root, text=response).pack()
    if (response==1):
        Label(root, text="You clicked Yes!").pack()
    else:
        Label(root, text="You clicked No!").pack()
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
root = Tk()
root.title("Learning Tkinter")
Button(root, text="Popup", command=popup).pack()
Button(root, text="Exit Program", command=root.quit).pack()
root.mainloop()