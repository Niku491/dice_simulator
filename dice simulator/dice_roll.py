import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

dice = ["images/dice1.jpg","images\dice2.png","images\dice3.jpg","images\dice4.png","images\dice5.png","images\dice6.png"]
# new_image = dice.resize((500, 500))
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
# image2 = ImageTk.PhotoImage(Image.open(random.choice(dice))) -----------------------

label1 = tk.Label(window,image = image1)
# label2 = tk.Label(window,image = image2)-------------------

label1.image = image1
# label2.image = image2-----------------

label1.place(x = 40, y = 100)
# label2.place(x = 250, y = 100)---------------------

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1

    # image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # label2.configure(image = image2)
    # label2.image = image2--------------------------------------------------

button = tk.Button(window,text="ROLL",bg = "red", fg = "white",font= "Times 20 bold",command=dice_roll )
button.place(x = 200, y = 0)
window.mainloop()
