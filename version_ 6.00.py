from tkinter import*
import os
from time import sleep
import tkinter.messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import pyttsx3
import time
from threading import Event, Thread
import pynput
from pynput.mouse import Button, Controller
import jedi

flg=0
flag_colon=0
current_open_file="no_file"

class RepeatedTimer:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.start = time.time()
        self.event = Event()
        self.thread = Thread(target=self._target)
        self.thread.start()
    def _target(self):
        while not self.event.wait(self._time):
            self.function(*self.args, **self.kwargs)
    @property
    def _time(self):
        return self.interval - ((time.time() - self.start) % self.interval)

    def stop(self):
        self.event.set()
        self.thread.join()
  
def custom_quit():
    say("ARE YOU SURE YOU WANT TO QUIT? Press Enter to quit and escape to cancel.")
    answer=tkinter.messagebox.askokcancel("ARE YOU SURE?","YOUR DATA WILL BE LOST")
    if answer:
        print("Exit")
        root.destroy()
        
def work():
    print("this works")

def resize():
    root.geometry("640x600")
    
def norresize():
    root.geometry("1920x1080")
    
def open_1(event):
    open_command()
    
def open_command():
    say("Enter name of the file to open and press Enter key and if you have to cancel press escape")
    file=filedialog.askopenfile(parent=root,mode='rb',title="select a file")
    if file!=None:
        contents=file.read()
        textpad.delete("1.0",END)
        textpad.insert('1.0',contents)
        global current_open_file
        current_open_file=file.name
        file.close()
        
def save_as_file():
   global current_open_file
   if current_open_file=="no_file":
        say("Enter the file name and press enter to save as and if you have to cancel press escape")
        file=filedialog.asksaveasfile(mode='w',defaultextension=".py")
        if file is None:
            return
        text2save=textpad.get("1.0",END)
        current_open_file=file.name
        file.write(text2save)
        file.close()
        say("file is saved ")
   else:
        save()
        
def save_1(event):
    save()
    
def save():
    global current_open_file
    if current_open_file=="no_file":
        save_as_file()
    else:
        file=open(current_open_file,"w+")
        file.write(textpad.get("1.0",END))
        file.close()
        say("file is saved")

def tour(event):
    say("WElCOME TO BLINDS IDE ")
    say("LET ME GUIDE YOU THROUGH APPLICATION")
    say('''WRITING WINDOW IS IN ON LEFT AND IS UP TO HALF SIZE OF MONITOR
           ON THE RIGHT SIDE WINDOW CONSISTS OF THREE PART ONE BELOW ANOTHER
           INPUT WINDOW TO GIVE INPUTS TO THE PROGRAMS
           OUTPUT WINDOW WHICH GIVE OUTPUTS OF THE PROGRAM
           AND THE ERROR WINDOW TO SHOW AND SPOKE ERROR IN PROGRAMS
           BELOW IT IS SUGGESTION LISTBOX WHICH WILL GIVE SUGGESTION IS FORGET
           SOMETHING AND NEXT BESIDE ON RIGHT SIDE IS COMPILE BUTTON ''')
    shortcut_keys(0)
    
def shortcut_keys(event):
    say("control plus u is for suggestion")
    say("control plus i is for to hear all code you written")
    say("control plus o is for to hear single line ")
    say("control plus t is for to taking tour of application ")
    say("control plus e is for to hear error ")
    say("control plus w is for to hear output ")
    say("control plus r or f 5 is for compiling the code")
    say("control plus q is for to hear input")
    say("control plus s is for to saving the file")
    say("control plus h is for to opening a file")

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
    data=data.replace('\t', " Tab Space ")
    data=data.replace('+', " Plus ")
    data=data.replace('-', " Minus ")
    data=data.replace('^ Next line', "")
    data=data.replace('            ^ Next line', "")
    return data

def errshort(data):
    data=data.replace('File "a.py",', "Error on ")
    data=data.replace('<module>', "module ")
    data=data.replace('^ Next line', "")
    data=data.replace('Next line         ', "")
    data=data.replace('^', "")
    return data

def dele():
    keyboard = pynput.keyboard.Controller()
    keyboard.press(pynput.keyboard.Key.delete)
    keyboard.release(pynput.keyboard.Key.delete)
    
def back():
    keyboard = pynput.keyboard.Controller()
    keyboard.press(pynput.keyboard.Key.left)
    keyboard.release(pynput.keyboard.Key.left)
    dele()
    
def down():
    keyboard = pynput.keyboard.Controller()
    keyboard.press(pynput.keyboard.Key.down)
    keyboard.release(pynput.keyboard.Key.down)

    
def fileOpen(event):
    line=textpad.index(INSERT)
    print (str(float(int(float(line))+1)))
    print (str(float(int(float(line)))))
    b=str(float(int(float(line))+1))
    a=str(float(int(float(line))))
    inputValue=textpad.get(a,b)
    print (inputValue)
    inputValue=inputValue.replace('\n', "")
    inputValue=specialchar(inputValue)
    say(inputValue)
    dele()
    
def allcode(event):
    inputValue=textpad.get("1.0","end-1c")
    if(inputValue[len(inputValue)-1]=='\t'):
        inputValue=inputValue[:-1]
    inputValue=specialchar(inputValue)
    say(inputValue)
    back()
  
def makeMenu(parent):
    top = tkinter.Menu(parent) 
    parent.config(menu = top)                           
    file = tkinter.Menu(top, tearoff = False)
    file.add_command(label = 'Open...', command = fileOpen, accelerator = 'ctrl+o')
    top.add_cascade(label = 'File', menu = file)
 
def say(tempvalue):
    engine = pyttsx3.init()
    pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 120)
    engine.say(tempvalue)
    engine.runAndWait()

def output(ar_out):
    text.configure(state='normal')
    text.delete('1.0', END)
    text.insert(INSERT, "OUTPUT:")
    if (len(ar_out)==0):
        text.insert(INSERT, "\nNo output")
    else:
        for i in range(0,len(ar_out)):
            text.insert(INSERT, '\n')
            text.insert(INSERT, ar_out[i])
    inputValue=text.get("1.0","end-1c")
    tempvalue=inputValue
    tempvalue=specialchar(tempvalue)
    say(tempvalue)
    text.configure(state='disabled')
    
def cursor_move(l):
    inputValue=textpad.get(float(int(l)),END).splitlines()
    k=0
    for i in range( 0, len(inputValue[0])):
        k+=1
    print(inputValue)
    textpad.mark_set("insert", "%d.%d" % (float(int(l)),float(k)))
    tmepval="You are now at the end of the error line number "+str(l)
    say(tmepval)
    
def err(ar_error):
    text2.configure(state='normal')
    text2.delete('1.0', END)
    l=0
    l2=0
    t=0
    if (len(ar_error)==0):
        text2.insert(INSERT, "ERROR: \nNo Error")
    else:
        text2.insert(INSERT, "ERROR: \n")
        for i in range(0,len(ar_error)):
            if(ar_error[i]=="Traceback (most recent call last):"):
                continue
            if(ar_error[i]=="SyntaxError: unexpected EOF while parsing"):
                t=1
            k=ar_error[i].split(' ')
            for a in range (0,len(k)):
                if k[a]=='line':
                    l=k[a+1:a+3][0]
                    break
            if t==1:
                ar_error[i]=ar_error[i].replace(l,str(int(l)-1))
                l2=str(int(l)-1)
            print("fsdfs",l)
            ar_error[i]=errshort(ar_error[i])
            print(ar_error[i])
            text2.insert(INSERT, ar_error[i])
            if (i!=len(ar_error)-1):
                text2.insert(INSERT, '\n')
    inputValue=text2.get("1.0","end-1c")
    if t==1:
        inputValue=inputValue.replace(l,l2)
        text2.delete('1.0', END)
        text2.insert(INSERT, inputValue)
    tempvalue=inputValue
    tempvalue=specialchar(tempvalue)
    tempvalue=errshort(tempvalue)
    print (inputValue)
    print (tempvalue)
    say(tempvalue)
    text2.configure(state='disabled')
    l=l.replace(",","")
    if t==1:
        cursor_move(l2)
        return
    if l!=0:
        cursor_move(l)
    
def user_input_to_program(user_input,prog):
    k=user_input.split(" ")
    k.pop(0)
    k.pop(0)
    print("k",k)
    for i in k:
        prog=prog.replace('input()',i,1)
        print('rep',prog)
    return prog
    
def p():
    inputValue=textpad.get("1.0","end-1c")
    inputValue=inputValue.replace('\r', "")
    tempvalue=inputValue
    tempvalue=specialchar(tempvalue)
    user_input=text3.get("1.0","end-1c")
    y=user_input_to_program(user_input,inputValue)
    print(y)
    print(user_input)
    text.configure(state='normal')
    text2.configure(state='normal')
    text.delete('2.0', END)
    text2.delete('2.0', END)
    text.configure(state='disabled')
    text2.configure(state='disabled')
    text_file = open("a.py", "w")
    text_file.write(y)
    text_file.close()
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    if os.path.exists('error.txt'):
        os.remove('error.txt')
    os.startfile("vbs_output.vbs")
    os.startfile("vbs_error.vbs")
    sleep(2)
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
    
def boloekbaar(bol):
    global flg
    if flg==0:
        say(bol)
        flg=1
    return

def motion(event):
    say("this is your input window ")
    return
def output_window(event):
    say("this is your output window ")
    return
def error_window(event):
  say("this is your error window ")
  return 
def writing_window(event):
  say("this is your writing window ")
  return

def fg():
    global flg
    flg=0

timer = RepeatedTimer(3, fg)

root=Tk()
root.wm_state('zoomed')
root.geometry("1920x772")
root.title("Blinds IDE")
menu=Menu(root)
textpad=scrolledtext.ScrolledText(root,width=100,height=48)
textpad.grid(rowspan=5,row=0,column=0)
text = Text(root)
text=scrolledtext.ScrolledText(root, width=85,height=20)
text.insert(INSERT, "OUTPUT : ")
text.grid(row=2,column=1,columnspan=2)
text2 = Text(root)
text2=Text(root, width=85,height=7)
text2.insert(INSERT, "ERROR : ")    
text2.grid(row=3,column=1,columnspan=2)
text3=Text(root, width=85,height=5)
text3.insert(INSERT, "Input : ")    
text3.grid(row=0,column=1,columnspan=2)
text3.bind('<Button-3>',motion)
text2.bind('<Button-3>',error_window)
text.bind('<Button-3>',output_window)
textpad.bind('<Button-3>',writing_window)

mouse = Controller()

root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_cascade(label="New Project")
submenu.add_cascade(label="open",command=open_command)
submenu.add_cascade(label="save as",command=save_as_file)
submenu.add_cascade(label="save ",command=save)
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

def motion_comp(event):
  say("this is your compile option you can click to compile ")
  return

def com(event):
    global flg
    if flg==0:
        p()
        flg=1
    return

whatever_you_do = " This is your compile option you can click to compile "
msg = Message(root, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 26, 'italic'))
msg.bind('<Button-3>',motion_comp)
msg.bind('<Button-1>',com)
msg.grid(row=4,column=2)
text_auto=Listbox(root,selectmode=SINGLE,width=40,height=10)
text_auto.grid(row=4,column=1)

def auto_col(event):
    text_auto.delete(0, END)
    auto_string=textpad.get("1.0","end-1c")  #extract text from textfield
    line=textpad.index(INSERT)
    val=float(line)
    whole=int(val)
    cnt=0
    for i in range(0,len(line)):
        if line[i]=='.':
            cnt=i
    b=0
    for j in range(cnt +1, len(line)):
        k=int(line[j])
        b=b*10+k
    global completions
    script=jedi.Script(auto_string,whole,b,'example.py')
    completions=script.completions()
    c=1
    for j in range(len(completions)):
        print(completions[j].name)
        text_auto.insert(1,completions[j].name+'\n')
        c+=1
    
def valuebhej(evt):
    global completions
    value=str((text_auto.get(text_auto.curselection())))
    value=value[0:-1]
    for j in range(len(completions)):
        if value==completions[j].name:
            textpad.insert(INSERT,completions[j].complete)
            text_auto.delete(0,END)
    mouse.position = (650, 650)
    mouse.click(Button.left,1)
    
def CurSelet(evt):
    value=str((text_auto.get(text_auto.curselection())))
    say(value)
    print (value)
    text_auto.bind('<Double-1>', valuebhej)
    
def auto_name(event):
    say("This is your auto complete window")
    
def run(event):
    p()
    
def cal_pos():
    line=textpad.index(INSERT)
    val=float(line)
    y=line
    cnt=0
    for i in range(0,len(y)):
        if y[i]=='.':
            cnt=i

    b=0
    for j in range(cnt+1,len(y)):
        m=y[j]
        k=int(m)
        b=b*10+k
    
    inputValue=textpad.get(str(float(int(float(line)))),"end-1c")
    print(inputValue[b-1])
    print(line)
    l=[]
    l.append(float(int(val)))
    l.append(b)
    l.append(inputValue)
    return l

def iden(whole):
    print("this is")
    global flag_colon
    for i in range(0,flag_colon):
        if(i==0): 
            textpad.insert(str(whole+1),"\n\t")
            back()
        else:
            textpad.insert(str(whole+1),"\t")
    
def check_iden(event):
    imple()
    
       
def imple():
    global flag_colon
    l=cal_pos()
    whole=l[0]
    s=l[1]
    inputValue=l[2]
    line=textpad.index(INSERT)
    textpad.mark_set("insert", END)
    line2=textpad.index(INSERT)
    textpad.mark_set("insert", line)
    print("asdf",line)
    print(line2)
    if line!=line2 and flag_colon!=0:
        if inputValue[s-1]==':':
               flag_colon+=1
        for i in range(0,flag_colon):
            if i==0:
                textpad.insert(str(whole+1),"\n")
            textpad.insert(str(whole+1),"\t")
        back()
        down()
        
    else:
        if inputValue[s-1]==':':
               flag_colon+=1
        iden(whole)
        
def remove_iden(event):
    global flag_colon
    line=textpad.index(INSERT)
    print(line)
    print (str(float(int(float(line))+1)))
    print (str(float(int(float(line)))))
    b=str(float(int(float(line))+1))
    a=str(float(int(float(line))))
    inputValue=textpad.get(a,b)
    inputValue=inputValue.replace('\t', "")
    inputValue=inputValue.replace('\n', "")
    if inputValue == "":
        if flag_colon!= 0:
            flag_colon-=1
    strng=textpad.get("1.0","end-1c")
    if strng=='':
        flag_colon=1

def speak_output(event):
    value=text.get("1.0",END)
    value=value[:-1]
    value=specialchar(value)
    say(value)

def speak_input(event):
    value=text3.get("1.0",END)
    value=value[:-1]
    value=specialchar(value)
    say(value)
        
def speak_error(event):
    value=text2.get("1.0",END)
    value=value[:-1]
    value=specialchar(value)
    say(value)
        
textpad.bind('<Return>',check_iden)
textpad.bind('<BackSpace>',remove_iden)
text.configure(state='disabled')
text2.configure(state='disabled')
text_auto.bind('<<ListboxSelect>>',CurSelet)
text_auto.bind('<Button-3>',auto_name)
textpad.bind_all('<Control-Key-u>',auto_col)
textpad.bind_all('<Control-Key-o>', fileOpen)
textpad.bind_all('<Control-Key-i>', allcode)
textpad.bind_all('<Control-Key-r>', run)
textpad.bind_all('<F5>', run)
textpad.bind_all('<Control-Key-w>', speak_output)
textpad.bind_all('<Control-Key-e>', speak_error)
textpad.bind_all('<Control-Key-q>', speak_input)
root.bind('<Control-Key-t>', tour)
root.bind('<Control-Key-b>',shortcut_keys)
root.bind('<Control-Key-s>',save_1)
root.bind('<Control-Key-h>',open_1)

textpad.mainloop()
status=Label(root,text="Running...",anchor=W,bg="GREY",fg="black")
status.pack(side=BOTTOM)
root.mainloop()
