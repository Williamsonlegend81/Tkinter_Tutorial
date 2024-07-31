from tkinter import *
from PIL import ImageTk,Image

root = Tk()
def forward(image_number):
    global myLabel
    global Button_forward
    global Button_backward

    myLabel.grid_forget()
    myLabel = Label(image=my_Images[image_number-1])
    Button_forward = Button(root,text=">",command=lambda: forward(image_number+1))
    Button_backward = Button(root,text="<",command=lambda: backward(image_number-1))
    if image_number==5:
        Button_forward = Button(root,text=">",state=DISABLED)
    Button_backward.grid(row=1,column=0)
    Button_forward.grid(row=1,column=2)
    Button_quit.grid(row=1,column=1)
    myLabel.grid(row=0,column=0,columnspan=3)
def backward(image_number):
    global myLabel
    global Button_forward
    global Button_backward

    myLabel.grid_forget()   
    myLabel = Label(image=my_Images[image_number-1])
    Button_forward = Button(root,text=">",command=lambda: forward(image_number+1))
    Button_backward = Button(root,text="<",command=lambda: backward(image_number-1))
    if (image_number==1):
        Button_backward = Button(root,text="<",state=DISABLED)
    Button_backward.grid(row=1,column=0)
    Button_forward.grid(row=1,column=2)
    myLabel.grid(row=0,column=0,columnspan=3)
myImg1 = ImageTk.PhotoImage(Image.open("Images/Blastoise.png"))
myImg2 = ImageTk.PhotoImage(Image.open("Images/Charizard.png"))
myImg3 = ImageTk.PhotoImage(Image.open("Images/Metagross.png"))
myImg4 = ImageTk.PhotoImage(Image.open("Images/Pikachu.png"))
myImg5 = ImageTk.PhotoImage(Image.open("Images/Venasaur.png"))
my_Images = [myImg1,myImg2,myImg3,myImg4,myImg5]
myLabel = Label(image=myImg1)
Button_forward = Button(root,text=">",command=lambda: forward(2))
Button_backward = Button(root,text="<",command=lambda: backward(2),state=DISABLED)
Button_quit = Button(root,text="Exit Program",command=lambda: root.quit())
Button_forward.grid(row=1,column=2)
Button_backward.grid(row=1,column=0)
Button_quit.grid(row=1,column=1)
myLabel.grid(row=0,column=0,columnspan=3)

root.mainloop()
