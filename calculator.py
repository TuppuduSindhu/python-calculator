#tkinter module is used to create gul(graphical user interface) applications
from tkinter import *
root=Tk() #this root is used to on the module
root.title("sindhu's calculator")
e=Entry(root,width=50,borderwidth=20,fg="grey")#entery means space to display what we are doing in calculator ,present at top of the calci
e.grid(row=0,column=0,columnspan=20,padx=20,pady=30)#grid is used to define overall rows and columns space and all
#declaring functions
def buttonclick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))#this function is used to click the surrent number and disable it until we perform specific operation ,get used to get the num then insert used to add present num and previous num
def clear():
    e.delete(0,END)
def buttonadd():
    firstnum=e.get()
    global fnum 
    global math 
    math="add" 
    fnum=int(firstnum) 
    e.delete(0,END)#this func is used to take current num and store it in first num then declaring two global variables fnum and math chechikng math="add" then declaring fisrtnum to fnum in int form  
def equal():
    secondnum=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,fnum+int(secondnum)) #it is used to get fnum and add it to second num if math is given add,mul,div or something else whatever it may be
    elif math=="sub":
        e.insert(0,fnum-int(secondnum))
    elif math=="mul":
        e.insert(0,fnum*int(secondnum))
    elif math=="div":
        e.insert(0,fnum/int(secondnum))
    elif math=="pow":
        e.insert(0,fnum**int(secondnum))
#functions calculate global is used to access anotherfunctions
def sub():
    firstnum=e.get()
    global fnum 
    global math 
    math="sub"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def mul():
    firstnum=e.get()
    global fnum 
    global math 
    math="mul"
    fnum=int(firstnum)
    e.delete(0,END)
    return
def div():
    firstnum=e.get()
    global fnum 
    global math 
    math="div"
    fnum=int(firstnum)
    e.delete(0,END)
    return 
def pow():
    firstnum=e.get()
    global fnum 
    global math 
    math="pow"
    fnum=int(firstnum)
    e.delete(0,END)
    return 
#creation of butons
button1=Button(root,text="1",padx=40,pady=30,command=lambda:buttonclick(1))
button2=Button(root,text="2",padx=40,pady=30,command=lambda:buttonclick(2))
button3=Button(root,text="3",padx=40,pady=30,command=lambda:buttonclick(3))
button4=Button(root,text="4",padx=40,pady=30,command=lambda:buttonclick(4))
button5=Button(root,text="5",padx=40,pady=30,command=lambda:buttonclick(5))
button6=Button(root,text="6",padx=40,pady=30,command=lambda:buttonclick(6))
button7=Button(root,text="7",padx=40,pady=30,command=lambda:buttonclick(7))
button8=Button(root,text="8",padx=40,pady=30,command=lambda:buttonclick(8))
button9=Button(root,text="9",padx=40,pady=30,command=lambda:buttonclick(9))
button0=Button(root,text="0",padx=40,pady=30,command=lambda:buttonclick(0))#creating uttons and placing numbers or text what we want and paddinf 
#operations
buttonadd=Button(root,text="+",padx=40,pady=30,command=buttonadd)
buttonsub=Button(root,text="-",padx=40,pady=30,command=sub)
buttondiv=Button(root,text="/",padx=40,pady=30,command=div)
buttonmul=Button(root,text="*",padx=40,pady=30,command=mul)
buttonpow=Button(root,text="pow",padx=40,pady=30,command=pow)
buttonequal=Button(root,text="==",padx=40,pady=30,command=equal)
buttonclear=Button(root,text="clear",padx=40,pady=30,command=clear)
buttonquit=Button(root,text="exit",padx=40,pady=30,command=root.quit)
#put buttons on screen means arranging buttons based on position to particular symbol
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
buttonpow.grid(row=6,column=1)
buttonclear.grid(row=6,column=0)
buttonquit.grid(row=6,column=2)
buttonadd.grid(row=4,column=1)
buttonsub.grid(row=4,column=2)
button0.grid(row=4,column=0)
buttonequal.grid(row=5,column=2)
buttonmul.grid(row=5,column=0)
buttondiv.grid(row=5,column=1)
root.mainloop()



    
        
    
    
