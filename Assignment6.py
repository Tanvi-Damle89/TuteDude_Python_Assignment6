#step 1: import tkinter

from tkinter import *


# step 2: gui interaction
window = Tk()
window.geometry("240x290")

# Step 3: adding inputs
#enty box
e= Entry(window, width= 80, borderwidth=5)
e.place(x=0, y= 0)

#BUTTONS

def click(num):
    result= e.get()
    e.delete(0,END)
    e.insert(0, str(result)+str(num))

b= Button(window,text= 1, width=10, command= lambda: click(1))
b.place(x=10, y =60)
b= Button(window,text= 2, width=10, command= lambda: click(2))
b.place(x=80, y =60)
b= Button(window,text= 3, width=10, command= lambda: click(3))
b.place(x=150, y =60)
b= Button(window,text= 4, width=10, command= lambda: click(4))
b.place(x=10, y =100)
b= Button(window,text= 5, width=10, command= lambda: click(5))
b.place(x=80, y =100)
b= Button(window,text= 6, width=10, command= lambda: click(6))
b.place(x=150, y =100)
b= Button(window,text= 7, width=10, command= lambda: click(7))
b.place(x=10, y =140)

b= Button(window,text= 8, width=10, command= lambda: click(8))
b.place(x=80, y =140)

b= Button(window,text= 9, width=10, command= lambda: click(9))
b.place(x=150, y =140)

b= Button(window,text= 0, width=10, command= lambda: click(0))
b.place(x=10, y =180)
# operator
def add ():
    n1= e.get()
    global i
    global math
    math= "Addition"
    i = int(n1)
    e.delete(0, END)

def sub ():
    n1= e.get()
    global i
    global math
    math="Subtraction"
    i = int(n1)
    e.delete(0, END)
def mul ():
    n1= e.get()
    global i
    global math
    math="Multiplication"
    i = int(n1)
    e.delete(0, END)
def div ():
    n1= e.get()
    global i
    global math
    math="Division"
    i = int(n1)
    e.delete(0, END)
b= Button(window,text= "+", width=10, command= add)
b.place(x=80, y =180)

b= Button(window,text= "-", width=10, command=sub)

b.place(x=150, y =180)

b= Button(window,text= "*", width=10, command= mul)

b.place(x=10, y =220)

b= Button(window,text= "/", width=10, command=div)
b.place(x=80, y =220)
def eq():
    n2= e.get()
    e.delete(0, END)
    try:
      if math== "Addition":
        e.insert(0,i +int(n2))
      elif math=="Subtraction":
        e.insert(0, i- int(n2))
      elif math== "Multiplication":
        e.insert(0, i*int(n2))
      elif math=="Division":
        if int(n2)==0:
            e.insert(0,"Error--Can't divide by Zero")
        else:
            e.insert(0, i/int(n2))
    except ValueError:
        e.insert(0,"Invalid Input")
b= Button(window,text= "=", width=10, command= eq)
b.place(x=150, y =220)

def clr():
    e.delete(0, END)

b= Button(window,text= "Clear", width=10, command=clr)
b.place(x=10, y =260)



# Step 4: Main loop
mainloop()
