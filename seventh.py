from tkinter import *


class PavelsButton:
    # master == root
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='Print message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        # quit brakes mainloop - closes the window
        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('print smth')


root = Tk()
b = PavelsButton(root)

root.mainloop()