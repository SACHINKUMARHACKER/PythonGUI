#!/usr/bin/env python

def getting_started():
    print('This is alright')

from Tkinter import *
root = None
def buttonPushed():
    global root
    root.destroy()

def main():
    global root
    root = Tk()
    w = Label(root,text="Click here")
    w.pack()
    myButton = Button(root,text="Quit",command=buttonPushed)
    myButton.pack()
    root.mainloop()


main()


