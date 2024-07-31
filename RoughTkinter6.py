from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Learning Tkinter")

MyImg = ImageTk.PhotoImage(Image.open("Pokemon/Dragon/149_Dragonite.png"))
my_label = Label(image=MyImg)
my_label.pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()