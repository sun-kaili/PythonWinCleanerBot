from tkinter import *
from pathlib import Path

def clicked():
    removepath = Path(r"C:\Windows\Temp")
    res=RemoveFileFrom(removepath)
    lbl.configure(text=res)


window = Tk()
window.title("Welcome Windows Cleaner")
window.geometry('350x200')
lbl = Label(window, text="PC ready to clean!")
lbl.grid(column=0, row=0)
btn = Button(window, text="Clean Your PC",command=clicked)
btn.grid(column=1, row=0)
window.mainloop()