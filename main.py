from tkinter import *
import tkinter.messagebox
root=Tk()
i = 0
while True:

    question = tkinter.messagebox.showinfo('Your Word','This is your word!\n' + str(i) + "\nIf the word was guessed press OK")
    end = tkinter.messagebox.askquestion('Are you done', 'Would you like to exit this game?')
    if(end == 'yes'):
        question = tkinter.messagebox.showinfo('Good Bye','Thank you for playing!')
        break
    elif(end == 'no'):
        i = i + 1
        
