from tkinter import *
import tkinter.messagebox


root = Tk()
tkinter.messagebox.showinfo('window title', 'Monkeys can live up to 300 years')
answer = tkinter.messagebox.askquestion('Question 1', 'U like silly faces?')
if answer == 'yes' :
    print('He likes silly faces')
else:
    print('No silly faces allowed')

root.mainloop()