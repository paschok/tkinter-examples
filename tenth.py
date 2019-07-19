from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()
# two for start point and two for end point
blackline = canvas.create_line(0, 0, 200, 50)
redline = canvas.create_line(0, 100, 200, 50, fill='red')

# 2 starting point, then width and height
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill='green')

canvas.delete(redline) # - deleting a red line
# canvas.delete(ALL) - deleting everything
root.mainloop()