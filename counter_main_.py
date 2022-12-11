import tkinter
from tkinter import Tk
from tkinter import *

windows = Tk()

# windows.configure(bg='white',height=800,width=800)


count_num = 0


windows.geometry('1000x800')


def incr():
   pass

def decr():
    pass

def reset():
    pass

incre_btn = Button(windows,bg='white',height=10,width=15,text='increase' \
                    ,activebackground='yellow',activeforeground='red',relief=RIDGE,command=incr())

decre_btn = Button(windows,bg='white',height=10,width=15,text='decrease' \
                    ,activebackground='yellow',activeforeground='red',relief=RIDGE, command=decr())

res_btn = Button(windows,bg='white',height=10,width=15,text='reset' \
                    ,activebackground='yellow',activeforeground='red',relief=RIDGE,command=reset())

counter_box = Label(windows,background='white',height=5,width=58,text=count_num)

incre_btn.place(x=300,y=300)
decre_btn.place(x=450,y=300)
res_btn.place(x=600,y=300)
counter_box.place(x=300,y=170)




windows.mainloop()