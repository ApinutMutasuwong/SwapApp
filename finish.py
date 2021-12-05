from tkinter import *
import pygame
import json

pygame.mixer.init()

def okstop():
    pygame.mixer.music.stop()
    finish.destroy()
def play():
    pygame.mixer.music.load('sound.mp3')
    pygame.mixer.music.play(loops=0)
with open('save/savefile.txt') as file:
    listb=json.load(file)
text1=listb[0]
text2=listb[1]
play()

finish=Tk()
finish.title("SwapApp")
finish.geometry('200x100')

Label(finish, text=text2).pack()
Label(finish,text=text1).pack()
Button(finish,width=8,text='Ok',command=okstop,font=("Times",13)).pack()

finish.mainloop()