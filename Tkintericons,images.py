from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Learning Tkinter")
Myimg = ImageTk.PhotoImage(Image.open("Images/Bhagwan Swaminarayan.jpg"))
myLabel = Label(image=Myimg)
myLabel.pack()
button_quit = Button(root,text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()