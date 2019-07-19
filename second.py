from tkinter import *

root = Tk()

# Frame - is just a layout
# We r making an invisible container that is gonna go in the main window-root
topFrame = Frame(root)

# pack means : place it in our our window
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="green")
button3 = Button(topFrame, text="Button 3", fg="yellow")
button4 = Button(bottomFrame, text="Button 4", fg="blue")

# every time we pack something it stacks one on each other
# if we wont button to appear on the left of the window
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()