# File:     dice-app.py
# Author:   r0paire
# Repo:     https://www.github.com/r0paire/dice-roller-app
# Date:     20/07/2021
# Info:     App that rolls dice using buttons.
# Python:   Python-3.9

import random
import tkinter
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk

app = Tk()
app.title("Dice Roller App")
app.iconphoto(False, tkinter.PhotoImage(file="images/icon.png"))
app.geometry("280x295")
app.resizable(False, False)

headerFont = tkFont.Font(family="Ubuntu", size=15)
buttonFont = tkFont.Font(family="Ubuntu", size=10, weight="bold")
textFont = tkFont.Font(family="Ubuntu", size=1, weight="bold")

# Label for dice faces
dice_label = Label()


# loop for app
loop = tkinter.IntVar()


# repeat loop function
def repeat():
    dice_label.pack_forget()
    yesBtn.pack_forget()
    noBtn.pack_forget()
    prompt.pack_forget()
    prompt_break.pack_forget()
    loop.set(1)
    x = "Y"


# Creating a Label widget
header = Label(app, text="Dice Roller", font=headerFont, fg="white", bg="#121212", height="2", width="35")
header.pack()
blankLabel = Label(app, text="")
blankLabel.pack()


# images
dice1 = ImageTk.PhotoImage(Image.open("images/face1.png"))
dice2 = ImageTk.PhotoImage(Image.open("images/face2.png"))
dice3 = ImageTk.PhotoImage(Image.open("images/face3.png"))
dice4 = ImageTk.PhotoImage(Image.open("images/face4.png"))
dice5 = ImageTk.PhotoImage(Image.open("images/face5.png"))
dice6 = ImageTk.PhotoImage(Image.open("images/face6.png"))


# dice roller app
x = "y"

while x == "y":

    no = random.SystemRandom().randint(1, 6)

    if no == 1:
        dice_label = Label(image=dice1)
        dice_label.pack()
    if no == 2:
        dice_label = Label(image=dice2)
        dice_label.pack()
    if no == 3:
        dice_label = Label(image=dice3)
        dice_label.pack()
    if no == 4:
        dice_label = Label(image=dice4)
        dice_label.pack()
    if no == 5:
        dice_label = Label(image=dice5)
        dice_label.pack()
    if no == 6:
        dice_label = Label(image=dice6)
        dice_label.pack()

    prompt_break = Label(app, text=" ", height="1")
    prompt_break.pack()
    prompt = Label(app, text="Roll the dice?", font="textFont")
    prompt.pack()

    # Buttons
    yesBtn = Button(app, text="Yes", font=buttonFont, command=repeat, fg="white", bg="green", height="1", width="6")
    yesBtn.place(x=65, y=247)

    noBtn = Button(app, text="No", font=buttonFont, command=app.destroy, fg="white", bg="red", height="1", width="6")
    noBtn.place(x=155, y=247)

    author = Label(app, text="r0paire© 2021", font=('Ubuntu', 8, 'bold italic'), fg="black")
    author.place(x=195, y=275)
    app.wait_variable(loop)

app.mainloop()
