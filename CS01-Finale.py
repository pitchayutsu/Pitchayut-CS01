from tkinter import *
root = Tk()

root.title("Calculator")
content = ""
txt = StringVar(value="0")

def btn(number):
    global content 
    content=content+str(number)
    txt.set(content)

def equal():
    global content 
    calculate=float(eval(content))
    txt.set(calculate)
    content = ""

def clear():
    global content 
    content = ""
    txt.set("")
    display.insert(0,"0")

display = Entry(font=("arial",30,"bold"),fg="white",bg="grey", textvariable=txt,justify="right")
display.grid(columnspan=4)

ButDT = Button(fg="black",bg = "yellow",font=("arial",30,"bold"),text = ".", command = lambda:btn("."),padx=35,pady=15).grid(row=4,column=0)
But0 = Button(fg="black",font=("arial",30,"bold"),text = "0", command = lambda:btn(0),padx=30,pady=15).grid(row=4,column=1)
But1 = Button(fg="black",font=("arial",30,"bold"),text = "1", command = lambda:btn(1),padx=30,pady=15).grid(row=3,column=0)
But2 = Button(fg="black",font=("arial",30,"bold"),text = "2", command = lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
But3 = Button(fg="black",font=("arial",30,"bold"),text = "3", command = lambda:btn(3),padx=30,pady=15).grid(row=3,column=2)
But4 = Button(fg="black",font=("arial",30,"bold"),text = "4", command = lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
But5 = Button(fg="black",font=("arial",30,"bold"),text = "5", command = lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
But6 = Button(fg="black",font=("arial",30,"bold"),text = "6", command = lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
But7 = Button(fg="black",font=("arial",30,"bold"),text = "7", command = lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
But8 = Button(fg="black",font=("arial",30,"bold"),text = "8", command = lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
But9 = Button(fg="black",font=("arial",30,"bold"),text = "9", command = lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)

ButC= Button(fg="black",bg="cyan",font=("arial",30,"bold"),text = "C", command = clear,padx=30,pady=15).grid(row=1,column=3)
ButPl= Button(fg="black",bg="orange",font=("arial",30,"bold"),command = lambda:btn("+"),text = "+",padx=32,pady=15).grid(row=2,column=3)
ButMn= Button(fg="black",bg="orange",font=("arial",30,"bold"),command = lambda:btn("-"),text = "-",padx=37,pady=15).grid(row=3,column=3)
ButMp= Button(fg="black",bg="orange",font=("arial",30,"bold"),command = lambda:btn("*"),text = "*",padx=33,pady=15).grid(row=4,column=3)
ButDv= Button(fg="black",bg="orange",font=("arial",30,"bold"),command = lambda:btn("/"),text = "/",padx=36,pady=15).grid(row=4,column=2)

Butequal=Button(fg="black",bg="cyan",font=("arial",30,"bold"),text="=",command=equal,padx=93,pady=15).grid(row=5,column=0)
Butopen=Button(fg="black",bg="orange",font=("arial",30,"bold"),command = lambda:btn("("),text = "(",padx=36,pady=15).grid(row=5,column=2)
Butclose= Button(fg="black",bg="orange",font=("arial",30,"bold"),command = lambda:btn("/"),text = "/",padx=36,pady=15).grid(row=5,column=3)

root.mainloop()
