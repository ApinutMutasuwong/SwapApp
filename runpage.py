import time
from tkinter import *
from tkinter import ttk
import json
from threading import *
import fuction
import PIL.Image
import PIL.ImageTk
import pygame
# Top level window
root =Tk()
root.title("SwapApp")
root.geometry('400x300')
pygame.mixer.init()
x=True
j=False
savea={}
text1=''
text2=''



def play():
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play(loops=0)

def NewWindow():
    global text2,text1,j
    play()
    fin =Toplevel(root)
    fin.title("SwapApp")
    fin.geometry('200x100')
    Label(fin, text=text2).pack()
    Label(fin, text=text1).pack()

def callback():
    global x, panel,j
    x = False
    j=False
    img2 = PIL.ImageTk.PhotoImage(PIL.Image.open('red.png'))
    panel.configure(image=img2)
    panel.image = img2

def Threading():
    t1=Thread(target=runfn)
    t1.start()

def runfn():
    global x,savea,text1,text2,j
    x=True
    if j:
        j=False
        clist = savea['listex']
        coin=savea['coin']
        namemax=clist[0]
        namemin=clist[0]
        mina=fuction.getpriceeach(coin,clist[0])
        maxa=mina
        while x:
            for i in clist:
                price=fuction.getpriceeach(coin,i)
                if price>maxa:
                    maxa=price
                    namemax=i
                if price<mina:
                    mina=price
                    namemin=i
            if ((maxa-mina)*100/mina)>savea['percent']:
                text2= namemax+' : '+str(maxa)+' - '+namemin+' : '+str(mina)
                text1='percent: '+str(format(((maxa-mina)*100/mina),'.2f'))+' %'
                NewWindow()
                callback()
            time.sleep(5)

def selected(event):
    coin=mycombo.get()
    lb.delete(0,END)
    for i in file[coin].keys():
        lb.insert(END,i)

def mainpage():
    root.destroy()
    import main
    return None

def showSelected():
    global savea,j
    coin=coina.get()
    fuction.addandupdatecoin(coin)
    coinli = []
    cname = lb.curselection()
    name = inputtxt.get(1.0, "end-1c")
    if cname!=() and name.isnumeric():
        j=True
        for i in cname:
            op = lb.get(i)
            coinli.append(op)
        savea={'listex':coinli,'percent':int(name),'coin':coin}
        img2 = PIL.ImageTk.PhotoImage(PIL.Image.open('green.png'))
        panel.configure(image=img2)
        panel.image = img2

with open('save/check.txt') as file:
    lista=json.load(file)
with open('save/coin.txt') as file:
    file=json.load(file)

Label(root,text='Select Your Exchange',font=("Times", 15)).place(x=13,y=260)
Label(root,text='Select Your Coin',font=("Times", 15)).place(x=28,y=10)
Label(root,text='Set Target Percent:',font=("Times", 13)).place(x=200,y=20)


img = PIL.ImageTk.PhotoImage(PIL.Image.open('red.png'))
panel = Label(root, image=img)
panel.place(x=270,y=125)

inputtxt = Text(root,height=1,width=3,font=5)
inputtxt.place(x=340,y=20)

coina=StringVar()
mycombo=ttk.Combobox(root,value=lista, textvariable=coina, state='readonly')
mycombo.current(0)
mycombo.bind("<<ComboboxSelected>>",selected)
mycombo.place(x=30,y=50)

lb = Listbox(root,selectmode = "multiple",height=11,width=30)
lb.place(x=10,y=80)


Button(root,width=12,text="Set", command=showSelected,font=("Times",11)).place(x=250,y=60)
Button(root, text="Exit", command=mainpage,font=("Times",13)).place(x=280,y=260)
Button(root,width=8, text="Run", command=Threading,font=("Times",13)).place(x=220,y=220)
Button(root,width=8,text='Stop',command=callback,font=("Times",13)).place(x=310,y=220)


root.mainloop()