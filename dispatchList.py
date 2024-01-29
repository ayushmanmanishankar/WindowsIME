from tkinter import *

top = Tk()

listbox = Listbox(top, height = 10, 
                width = 15, 
                bg = "grey",
                activestyle = 'dotbox', 
                font = "Helvetica",
                fg = "yellow")

top.geometry("150x150")

listbox.pack()

top.mainloop()

# create a root window.
def dispatch(rootStr,listSuggest):
    while listbox.size>0:
        listbox.delete(0)
    k=1
    for i in listSuggest:
        listbox.insert(k,i)
        k+=1
    listbox.insert(k,rootStr)

