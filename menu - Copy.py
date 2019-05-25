from tkinter import*
import os
from time import sleep
import tkinter.messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import pyttsx3
   
def custom_quit():
    answer=tkinter.messagebox.askokcancel("ARE YOU SURE?","YOUR DATA WILL BE LOST")
    if answer:
        print("Exit")
        quit()
        
def work():
    print("this works")

def resize():
    root.geometry("640x600")
def norresize():
    root.geometry("600x600")
def open_command():
    file=filedialog.askopenfile(parent=root,mode='rb',title="select a file")
    if file!=None:
        contents=file.read()
        #print(contents)
        textpad.insert('1.0',contents)
        file.close()
def specialchar(data):
    data=data.replace('!', " Exclamation ")
    data=data.replace('"', " Double quote ")
    data=data.replace("'", " Single quote ")
    data=data.replace('(', " Left parenthesis ")
    data=data.replace(')', " Right parenthesis ")
    data=data.replace(',', " Comma ")
    data=data.replace(':', " Colon ")
    data=data.replace('<', " Less than ")
    data=data.replace('>', " Greater than ")
    data=data.replace('[', " Left bracket ")
    data=data.replace(']', " Right bracket ")
    data=data.replace('_', " Underscore ")
    data=data.replace('{', " Left brace ")
    data=data.replace('}', " Right brace ")
    data=data.replace('\n', " Next line ")
    data=data.replace('+', " Plus ")
    data=data.replace('-', " Minus ")
    data=data.replace('      Next line                   ^ Next line ', " Minus ") 
    data=data.replace('Minus', "")
    return data

def fileOpen(event):
    line=textpad.index(INSERT)
    print (line)
    inputValue=textpad.get(str(float(line)-1),line)
    say(inputValue)


def makeMenu(parent):
    top = tkinter.Menu(parent) 
    parent.config(menu = top)                           

    file = tkinter.Menu(top, tearoff = False)
    file.add_command(label = 'Open...', command = fileOpen, accelerator = 'ctrl+o')
    top.add_cascade(label = 'File', menu = file)

    
def say(tempvalue):
    engine = pyttsx3.init()
    pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 130)
    engine.say(tempvalue)
    engine.runAndWait()

def output(ar_out):
    if (len(ar_out)==0):
        text.insert(INSERT, "\n N/A")
    else:
        for i in range(0,len(ar_out)):
            text.insert(INSERT, '\n')
            text.insert(INSERT, ar_out[i])
    #root.mainloop()
    inputValue=text.get("1.0","end-1c")
    tempvalue=inputValue
    tempvalue=specialchar(tempvalue)
    say(tempvalue)

def err(ar_error):
    if (len(ar_error)==0):
        text2.insert(INSERT, "\n N/A")
    else:
        for i in range(0,len(ar_error)):
            text2.insert(INSERT, '\n')
            text2.insert(INSERT, ar_error[i])
    #root.mainloop()
    inputValue=text2.get("1.0","end-1c")
    tempvalue=inputValue
    tempvalue=specialchar(tempvalue)
    print (inputValue)
    print (tempvalue)
    say(tempvalue)
    
def left(event):
    print(" u clicked left button")
def right(event):
    print(" u clicked right button")    
    
def p():
    inputValue=textpad.get("1.0","end-1c")
    inputValue=inputValue.replace('\r', "")
    tempvalue=inputValue
    tempvalue=specialchar(tempvalue)
    print(inputValue)
    print(tempvalue)

    text.delete('2.0', END)
    text2.delete('2.0', END)
    
    text_file = open("a.py", "w")
    text_file.write(inputValue)
    text_file.close()
    
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    if os.path.exists('error.txt'):
        os.remove('error.txt')
        
    say(tempvalue)
    
    
    os.startfile("vbs_output.vbs")
    os.startfile("vbs_error.vbs")

    sleep(5)

    lines = [line.rstrip('\n') for line in open('output.txt')]
    ar_out=lines
    print (ar_out)
    lines = [line.rstrip('\n') for line in open('error.txt')]
    ar_error=lines
    print (ar_error)

    if os.path.exists('output.txt'):
        os.remove('output.txt')
    if os.path.exists('error.txt'):
        os.remove('error.txt')
        
    output(ar_out)
    err(ar_error)


    
 

root=Tk()
root.geometry("1280x720")
menu=Menu(root)
textpad=scrolledtext.ScrolledText(root,width=100,height=20)
textpad.grid(row=0)
texttemp = Text(root)
texttemp=Text(root, width=100,height=1)
texttemp.grid(row=1)
text = Text(root)
text=Text(root, width=100,height=3)
text.insert(INSERT, "OUTPUT :")
text.grid(row=2)
texttemp = Text(root)
texttemp=Text(root, width=100,height=1)
texttemp.grid(row=3)
text2 = Text(root)
text2=Text(root, width=100,height=5)
text2.insert(INSERT, "ERROR :")    
text2.grid(row=4)



root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_cascade(label="New Project")
submenu.add_cascade(label="open",command=open_command)
submenu.add_cascade(label="save")
submenu.add_command(label="Exit",command=custom_quit)

submenu2=Menu(menu)
menu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_cascade(label="cut")
submenu2.add_cascade(label="copy")
submenu2.add_cascade(label="undo")
submenu2.add_cascade(label="redo")
submenu2.add_cascade(label="paste all")
submenu2.add_cascade(label="find")
  
submenu3=Menu(menu)
menu.add_cascade(label="Run",menu=submenu3)
submenu3.add_cascade(label="run")
submenu3.add_cascade(label="python shell resize",command=resize)
submenu3.add_cascade(label="Normal size",command=norresize)


submenu4=Menu(menu)
menu.add_cascade(label="Shell",menu=submenu4)
submenu4.add_cascade(label="restart shell")
submenu4.add_cascade(label="interup execution")






submenu5=Menu(menu)
menu.add_cascade(label="Help",menu=submenu5)
submenu5.add_cascade(label="about IDE")
submenu5.add_cascade(label="Python Docs")
submenu5.add_cascade(label="config IDE")
submenu5.add_command(label="credit",command=credits)


but=Button(text="compille",command=p)
but.grid(row=5)
#frame.bind("<Button-1>",left)


#textpad = tkinter.Tk()
textpad.bind_all('<Control-Key-o>', fileOpen)
#makeMenu(textpad)
textpad.mainloop()
status=Label(root,text="Running...",anchor=W,bg="GREY",fg="black")
status.pack(side=BOTTOM)



root.mainloop()
