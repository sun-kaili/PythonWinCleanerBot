from cleanWinBot import RemoveFileFrom,getPathFromJson
from tkinter import *
from pathlib import Path

pathDict = getPathFromJson('setting.json')

def clicked():
    for index,jsnPath in enumerate(pathDict):
        removepath = Path(jsnPath['pathloc'])
        #print(removepath)
        list.insert(0,removepath)
        for res in enumerate(RemoveFileFrom(removepath)):
            #print(res)
            list.insert(0,res)


window = Tk()
window.title("Welcome Windows Cleaner")
window.geometry('500x400')
btn = Button(window, text="Clean Your PC",command=clicked)
btn.grid(column=2, row=0)
btn.pack()
list = Listbox(window,bg = 'white',width = 90,height=90)
list.pack()
window.mainloop()