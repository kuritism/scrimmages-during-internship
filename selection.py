"""WHERE DID TE BUTTONS GO"""

# Imports
import tkinter
from PIL import Image, ImageTk

# Define window
root = tkinter.Tk()
root.resizable(False, False)
root.attributes('-fullscreen', True)
bg = Image.open('Assets/UI/Character Selection/Player 1 Select.png')
tk_bg = ImageTk.PhotoImage(bg)
label = tkinter.Label(root, image=tk_bg)
label.grid(row=0, column=0)
e = 0

fart = ["bingo", "emu", "petticoat", "tbh"]

def what():
    global bg, tk_bg, e
    print('lesgo')
    if e == 0:
        bg = Image.open('Assets/UI/Character Selection/Player 2 Select.png')
        tk_bg = ImageTk.PhotoImage(bg)
        label.config(image=tk_bg)
        label.grid(row=0, column=0)
    else:
        print("all done")
    e += 1

def func(character):
    global image, tk_image, fart

    # Get image
    image = Image.open(f'Characters/{character}/sprites/{character}_Icon.png')
    tk_image = ImageTk.PhotoImage(image.resize((256, 256)))

    # Put on button
    button = tkinter.Button(root, image=tk_image, command=lambda:what)
    button.image = tk_image
    button.grid(row=1, column=fart.index(character), padx=10, pady=10)


# Call function
for char in fart:
    func(char)

# Run the man loop
root.mainloop()
