from tkinter import *
from PIL import ImageTk,Image

root = Tk()
def forward(image_number):
    global myLabel
    global Button_forward
    global Button_backward

    myLabel.grid_forget()
    myLabel = Label(image=my_Images[image_number-1])
    Button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    Button_backward = Button(root,text="<<",command=lambda: backward(image_number-1))
    if (image_number==1):
        Button_backward = Button(root,text="<<",command=lambda: backward(5))
    if (image_number==5):
        Button_forward = Button(root,text=">>",command=lambda:forward(image_number-4))
    Button_forward.grid(row=1,column=2)
    Button_backward.grid(row=1,column=0)
    myLabel.grid(row=0,column=0,columnspan=3)
    pokemon = ["Blastoise","Charizard","Metagross","Pikachu","Venasaur"]
    status = Label(root,text=f"{pokemon[image_number-1]}",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
def backward(image_number=5):
    global myLabel
    global Button_forward
    global Button_backward

    myLabel.grid_forget()
    myLabel = Label(image=my_Images[image_number-1])
    Button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    Button_backward = Button(root,text="<<",command=lambda: backward(image_number-1))
    if (image_number==5):
        Button_forward = Button(root,text=">>",command=lambda: forward(1))
    if (image_number==1):
        Button_backward = Button(root,text="<<",command=lambda: backward(image_number+4))
    Button_forward.grid(row=1,column=2)
    Button_backward.grid(row=1,column=0)
    myLabel.grid(row=0,column=0,columnspan=3)
    pokemon = ["Blastoise","Charizard","Metagross","Pikachu","Venasaur"]
    status = Label(root,text=f"{pokemon[image_number-1]}",bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
myImg1 = ImageTk.PhotoImage(Image.open("Images/Blastoise.png"))
myImg2 = ImageTk.PhotoImage(Image.open("Images/Charizard.png"))
myImg3 = ImageTk.PhotoImage(Image.open("Images/Metagross.png"))
myImg4 = ImageTk.PhotoImage(Image.open("Images/Pikachu.png"))
myImg5 = ImageTk.PhotoImage(Image.open("Images/Venasaur.png"))
my_Images = [myImg1,myImg2,myImg3,myImg4,myImg5]
status = Label(root,text="Blastoise",bd=1, relief=SUNKEN,anchor=E)
myLabel = Label(image=myImg1)
Button_forward = Button(root,text=">>",command=lambda: forward(2))
Button_backward = Button(root,text="<<",command= backward)
Button_quit = Button(root,text="Exit Program",command=root.quit)

Button_backward.grid(row=1,column=0)
Button_forward.grid(row=1,column=2,pady=10)
Button_quit.grid(row=1,column=1)
myLabel.grid(row=0,column=0,columnspan=3)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
root.mainloop()