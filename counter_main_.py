import tkinter
from tkinter import Tk
from tkinter import *


windows = Tk()
windows.geometry('1000x800')
windows.title('deez counter')


count_num = 0


counter_text = IntVar(windows,value=0) ##add parameter value= so that there will be a default value from start, not blank
counter_box = Entry(windows,bg='white',width=58,textvariable=counter_text) ##value of textvariable doesn't require parenthesis
counter_box.place(x=300,y=170)


''' define function '''

def incr():
   global count_num
   count_num += 1
   counter_text.set(count_num)

def decr():
    global count_num
    count_num -= 1
    counter_text.set(count_num)

def reset():
    global count_num
    count_num = 0
    counter_text.set(count_num)


''' create and place button '''
incre_btn = Button(windows,bg='white',height=10,width=15,text='increase',command=incr) #value of command doesn't need parenthesis
decre_btn = Button(windows,bg='white',height=10,width=15,text='decrease',command=decr)
res_btn = Button(windows,bg='white',height=10,width=15,text='reset',command=reset)
incre_btn.place(x=300,y=300)
decre_btn.place(x=450,y=300)
res_btn.place(x=600,y=300)



windows.mainloop()