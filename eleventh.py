from tkinter import *

root = Tk()

photo = PhotoImage(file='paradrop.png')

label = Label(root, image=photo)
label.pack()
root.mainloop()

"""
    If u wanna handle jpg as well: 
    
    
    
    from tkinter import *
    rom PIL import Image, ImageTk

    root = Tk()
    
    image = Image.open("moe.jpg")
    photo = ImageTk.PhotoImage(image)
    # photo = PhotoImage(file="png-002.png")
    label = Label(root, image=photo)
    label.pack()
    
    root.mainloop()
"""