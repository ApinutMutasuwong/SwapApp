from tkinter import *
import fuction
import json
import PIL.Image
import PIL.ImageTk

with open('save/exchangelist.txt') as file:
    exchangelist = json.load(file)
with open('save/check.txt') as file:
    coinlist = json.load(file)
with open('save/coin.txt') as file:
    coin = json.load(file)


def pagec1(root, frame):
    frame.pack_forget()
    page1(root)


def pagec2(root, frame):
    frame.pack_forget()
    page2(root)


def maincpage(root, frame):
    frame.pack_forget()
    mainpage(root)


def donec(root, frame):
    frame.pack_forget()
    donepage(root)


def pagesearch1c(root, frame, savelist):
    frame.pack_forget()
    pagesearch1(root, savelist)


def pagesearch2c(root, frame, savelist):
    frame.pack_forget()
    pagesearch2c(root, savelist)


def runcpage(root, frame):
    root.destroy()
    import runpage


def mainpage(root):
    global image1
    mainFrame = Frame(root)
    image1 = PIL.ImageTk.PhotoImage(PIL.Image.open('400x200.png'))
    Label(mainFrame, image=image1).pack()
    Button(mainFrame, width=15, height=1, text='exchange', fg='black', bg='grey', font=("Times", 18),
           command=lambda: pagec1(root, mainFrame)).place(x=0, y=205)
    Button(mainFrame, width=15, height=1, text='coin', fg='black', bg='grey', font=("Times", 18),
           command=lambda: pagec2(root, mainFrame)).place(x=200, y=205)
    Button(mainFrame, width=30, height=1, text='run', fg='black', bg='grey', font=("Times", 18),
           command=lambda: runcpage(root, mainFrame)).place(x=0, y=253)
    mainFrame.pack(fill='both', expand=1)


def page1(root):
    with open('save/exchangelist.txt') as file:
        exchangelist = json.load(file)
    page1Frame = Frame(root)

    def printInput():
        name = inputtxt.get(1.0, "end-1c")
        if name != '':
            lista = fuction.seachexchangefn(name)
            if lista[0]['sume'] == 1:
                fuction.addmyexchange(name)
                donec(root, page1Frame)
            else:
                savelista = []
                for i in range(10):
                    savelista.append(lista[i]['name'])
                pagesearch1c(root, page1Frame, savelista)

    inputtxt = Text(page1Frame, height=1, width=100, font=50)
    inputtxt.place(y=225)

    label2 = Label(page1Frame, text='Input Your Exchange Name', font=("Times", 15))
    label2.place(y=190, x=90)

    lb = Listbox(page1Frame, height=11, width=30)
    lb.pack()

    Button1 = Button(page1Frame, width=15, height=1, text="AddExchange", fg='black', bg='grey', font=("Times", 15),
                     command=printInput)
    Button1.place(x=15, y=255)
    Button2 = Button(page1Frame, width=14, height=1, text="Exit", fg='black', bg='grey', font=("Times", 15),
                     command=lambda: maincpage(root, page1Frame))
    Button2.place(x=210, y=255)

    for i in exchangelist:
        lb.insert(END, i)
    page1Frame.pack(fill='both', expand=1)


def pagesearch1(root, savelist):
    search1Fream = Frame(root)

    def showSelected():
        cname = lb.curselection()
        op = lb.get(cname)
        fuction.addmyexchange(op)
        donec(root, search1Fream)

    show = Label(search1Fream, text="Select Your Exchange", font=("Times", 20), padx=10, pady=10)
    show.pack()
    lb = Listbox(search1Fream, height=10, width=30)
    lb.pack()

    for item in savelist:
        lb.insert(END, item)

    Button(search1Fream, text="AddExchange", fg='black', bg='grey', font=("Times", 16), command=showSelected).place(
        x=130, y=240)
    Button2 = Button(search1Fream, width=5, height=1, text="Exit", fg='black', bg='grey', font=("Times", 15),
                     command=lambda: maincpage(root, search1Fream)).place(x=300, y=240)
    search1Fream.pack(fill='both', expand=1)


def page2(root):
    page2Frame = Frame(root)

    with open('save/check.txt') as file:
        coinlist = json.load(file)

    def printInput():

        name = inputtxt.get(1.0, "end-1c")
        if name != '':
            lista = fuction.seachcoinfn(name)
            if lista[0]['sume'] == 1:
                fuction.addandupdatecoin(lista[0]['name'])
                donec(root, page2Frame)
            else:
                savelista = []
                for i in range(10):
                    savelista.append(lista[i]['name'])
                pagesearch1c(root, page2Frame, savelista)

    inputtxt = Text(page2Frame, height=1, width=100, font=50)
    inputtxt.place(y=225)

    label2 = Label(page2Frame, text='Input Your Coin Name', font=("Times", 15))
    label2.place(y=190, x=110)

    lb = Listbox(page2Frame, height=11, width=30)
    lb.pack()

    Button1 = Button(page2Frame, width=15, height=1, text="AddCoin", fg='black', bg='grey', font=("Times", 15),
                     command=printInput)
    Button1.place(x=15, y=255)
    Button2 = Button(page2Frame, width=14, height=1, text="Exit", fg='black', bg='grey', font=("Times", 15),
                     command=lambda: maincpage(root, page2Frame))
    Button2.place(x=210, y=255)
    for i in coinlist:
        lb.insert(END, i)
    page2Frame.pack(fill='both', expand=1)


def pageserch2(root, savelist):
    search2Fream = Frame(root)

    def showSelected():
        cname = lb.curselection()
        op = lb.get(cname)
        fuction.addandupdatecoin(op)
        donec(root, search2Fream)

    show = Label(search2Fream, text="Select Your Coin", font=("Times", 20), padx=10, pady=10)
    show.pack()
    lb = Listbox(search2Fream, height=10, width=30)
    lb.pack()

    for item in savelist:
        lb.insert(END, item)

    Button(search2Fream, width=10, height=1, text="AddCoin", fg='black', bg='grey', font=("Times", 16),
           command=showSelected).place(x=130, y=240)
    Button2 = Button(search2Fream, width=5, height=1, text="Exit", fg='black', bg='grey', font=("Times", 15),
                     command=mainpage).place(x=300, y=240)
    search2Fream.pack(fill='both', expand=1)


def donepage(root):
    doneFream = Frame(root)
    label2 = Label(doneFream, text='D O N E', font=('RD CHULAJARUEK', 50)).pack()
    Button2 = Button(doneFream, width=27, height=1, text="BackToMenu", fg='black', bg='grey', font=50,
                     command=lambda: maincpage(root, doneFream)).pack()
    doneFream.pack(fill='both', expand=1)


if __name__ == '__main__':
    root = Tk()
    root.title("SwapApp")
    root.geometry('400x300')
    mainpage(root)
    root.mainloop()
