from cgitb import text
from cleanWinBot import RemoveFileFrom
from tkinter import *
from pathlib import Path

def clicked():
    removepath = Path(r"C:\Windows\Temp")
    for res in enumerate(RemoveFileFrom(removepath)):
        list.insert(0,res)


window = Tk()
window.title("Welcome Windows Cleaner")
window.geometry('350x200')
btn = Button(window, text="Clean Your PC",command=clicked)
btn.grid(column=2, row=0)
btn.pack()
list = Listbox(window,bg = 'white',width = 50)
list.pack()
window.mainloop()