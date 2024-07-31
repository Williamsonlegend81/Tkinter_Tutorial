from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")
def forward(image_number):
    global status
    global MyLabel
    global button_forward
    global button_backward
    MyLabel.grid_forget()
    status.grid_forget()
    
    myImage = myList[image_number-1]
    MyLabel = Label(image=myImage)
    MyLabel.grid(row=0, column=0, columnspan=3)

    status = Label(root, text=f"Image {image_number} of {len(myList)}", bd=1, relief=SUNKEN, anchor=E)

    button_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_quit = Button(root, text="Exit Program", command=root.quit)

    if (image_number==len(myList)):
        button_forward = Button(root, text=">>", command=lambda: forward(1))
    if (image_number==1):
        button_backward = Button(root, text="<<", command=lambda: backward(len(myList)))
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
def backward(image_number):
    global status
    global MyLabel
    global button_forward
    global button_backward
    MyLabel.grid_forget()
    status.grid_forget()
    
    myImage = myList[image_number-1]
    MyLabel = Label(image=myImage)
    MyLabel.grid(row=0, column=0, columnspan=3)

    status = Label(root, text=f"Image {image_number} of {len(myList)}", bd=1, relief=SUNKEN, anchor=E)

    button_backward = Button(root, text="<<", command=lambda: backward(image_number-1))
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_quit = Button(root, text="Exit Program", command=root.quit)

    if (image_number==len(myList)):
        button_forward = Button(root, text=">>", command=lambda: forward(1))
    if (image_number==1):
        button_backward = Button(root, text="<<", command=lambda: backward(len(myList)))
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    button_forward.grid(row=1, column=2)
    button_backward.grid(row=1, column=0)
    button_quit.grid(row=1, column=1)
myImg1 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/25_Pikachu.png"))
myImg2 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/26_Raichu.png"))
myImg3 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/81_Magnemite.png"))
myImg4 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/82_Magneton.png"))
myImg5 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/100_Voltorb.png"))
myImg6 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/101_Electrode.png"))
myImg7 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/125_Electabuzz.png"))
myImg8 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/135_Jolteon.png"))
myImg9 = ImageTk.PhotoImage(Image.open("Pokemon/Electric/145_Zapdos.png"))
myList = [myImg1,myImg2,myImg3, myImg4,myImg5,myImg6,myImg7,myImg8,myImg9]

status = Label(root, text=f"Image 1 of {len(myList)}", bd=1, relief=SUNKEN, anchor=E)

button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_backward = Button(root, text="<<", command=lambda: backward(len(myList)))
MyLabel = Label(image=myImg1)
MyLabel.grid(row=0,column=0, columnspan=3)
button_forward.grid(row=1,column=2)
button_backward.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()