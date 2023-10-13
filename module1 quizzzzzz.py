from cgitb import text
from tkinter import *

def check(option):
    if(option == 1):
        val2.set(0)
        val3.set(0)
    elif(option == 2):
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)

win = Tk()
win.title("Quiz Game")

root = Frame()
root.pack()

question = Label(root, width=60, font=(10),text="Question")
question.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, variable=val1, text="option1", command=lambda:chek(1))
option1.pack()

option2 = Checkbutton(root, variable=val2, text="option2", command=lambda:chek(2))
option2.pack()

option3 = Checkbutton(root, variable=val3, text="option3", command=lambda:chek(3))
option3.pack()

next_b = Button(root, text="next")
next_b.pack()

score = Label(win)
score.place_forget()

win.mainloop()
