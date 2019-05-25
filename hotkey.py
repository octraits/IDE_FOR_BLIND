import tkinter

def fileOpen(event):
    print('qwerty')

def makeMenu(parent):
    top = tkinter.Menu(parent) 
    parent.config(menu = top)                           

    file = tkinter.Menu(top, tearoff = False)
    file.add_command(label = 'Open...', command = fileOpen, accelerator = 'ctrl+o')
    top.add_cascade(label = 'File', menu = file)


root = tkinter.Tk()
root.bind_all('<Control-Key-o>', fileOpen)
makeMenu(root)
root.mainloop()
