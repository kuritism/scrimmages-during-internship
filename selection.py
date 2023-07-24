"""WHERE DID TE BACKGROUND GO"""

# Imports
import tkinter
from tkinter import DISABLED
from PIL import Image, ImageTk
import os


# Define window
root = tkinter.Tk()
root.resizable(False, False)
root.attributes('-fullscreen', True)
bg = Image.open('Assets/UI/Character Selection/Player 1 Select.png')
tk_bg = ImageTk.PhotoImage(bg)
play = Image.open("Assets/UI/Character Selection/Start.png")
tk_play = ImageTk.PhotoImage(play.resize((160,90)))

label = tkinter.Label(root, image=tk_bg, bd=0)
label.grid(row=0, column=0, columnspan=4, rowspan=4)
button_frame = tkinter.Frame(root, width=271*4, height=271)
button_frame.grid(row=0, column=0)

playbutton = tkinter.Label(root, image=tk_play, bd=0)
playbutton.grid(row=0, column=0, sticky="SE")

# Set values
var = 0
x = 0
y = 0
buttons = []
select = []


def what(event):
    global bg, tk_bg, var
    print(event)

    if var == 0:
        bg = Image.open('Assets/UI/Character Selection/Player 2 Select.png')
        tk_bg = ImageTk.PhotoImage(bg)
        label.config(image=tk_bg)
        label.grid(row=0, column=0)
    else:
        for widget in buttons:
            widget.config(state=DISABLED)
        print("all done")
    var += 1


for char in os.listdir("Characters"):
    # Get image
    try:
        image = Image.open(f'Characters/{char}/sprites/{char}_Icon.png')
        print("Imported Character:", char)
        tk_image = ImageTk.PhotoImage(image.resize((256, 256)))

        # Put on button
        button = tkinter.Button(button_frame, image=tk_image, bd=8)
        button.image = tk_image
        button.place(x=x, y=y)
        buttons.append(button)
        x += 271

    except FileNotFoundError:  # if file does not exist
        print(f"Error: {char} is missing sprites")

root.bind('<Button-1>', what)

# Run the man loop
root.mainloop()
