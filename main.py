from tkinter import *
import tkinter.messagebox
import random
root=Tk()


while True:
    random_value = random.randrange(1, 5)
    question = tkinter.messagebox.showinfo('Your Word','This is your word!\n:' + str(random_value) + "\nIf done or repitition press OK")
    end = tkinter.messagebox.askquestion('Are you done', 'Would you like to play another round?')
    if(end == 'no'):
        question = tkinter.messagebox.showinfo('Good Bye','Thank you for playing!')
        break
