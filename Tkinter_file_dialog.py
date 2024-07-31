from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Tkinter Tutorials")

def open():
    global my_Img
    root.filename = filedialog.askopenfilename(initialdir="E:\Tkinter Tutorial\Images",title="Select A File", filetypes=(("jpg files","*.jpg"),("all files", "*.*")))
    my_Img = ImageTk.PhotoImage(Image.open(f"{root.filename}"))
    my_Label = Label(image=my_Img)
    my_Label.pack()
Btn = Button(root,text="Open dialog box",command=open)
Btn.pack()
root.mainloop()