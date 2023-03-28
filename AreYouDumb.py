from tkinter import *
from tkinter import messagebox
import random

def Yes():
    messagebox.showinfo("YES", "I KNOW !")
    quit()

def motionMouse():
    btnNo.place(y=random.randint(0, 200), x=random.randint(0, 250))

root = Tk()
root.geometry('300x250')
root.title("Are U Dumb")
root.resizable(width=False, height=False)
root["bg"] = "white"

label = Label(root, text="Are you dumb?", bg="white", font=("Arial", 20)).pack()

btnYes = Button(root, text="Yes", command=Yes).place(x=90, y=110)
btnNo = Button(root, text="No", command=motionMouse)
btnNo.place(x=180, y=110)

root.mainloop()