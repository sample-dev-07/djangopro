import numpy as np
import pandas as pd
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile, asksaveasfile
  

window = tk.Tk()
window.title("CRM")
window.rowconfigure([0,1],minsize=50,weight=50)
window.columnconfigure(0,minsize=50,weight=50)

file = askopenfile(mode ='r', filetypes =[('Exal Files', '*.xlsx')])
kishan = pd.read_excel(f"{file.name}")

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", )
filemenu.add_command(label="Open")
filemenu.add_command(label="Save",)
filemenu.add_command(label="Save as...")
filemenu.add_command(label="Close",)

filemenu.add_separator()

filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo",)

editmenu.add_separator()

editmenu.add_command(label="Cut",)
editmenu.add_command(label="Copy",)
editmenu.add_command(label="Paste",)
editmenu.add_command(label="Delete",)
editmenu.add_command(label="Select All",)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)
def main(kishan):
    d = e.get()
    i = 0
    lis = np.array([b,b2,b3,b4,b5,b6,b7,b8,b9,b10])
    lis2 = np.array([m,m2,m3,m4,m5,m6,m7,m8,m9,m10])
    try:
        jj = kishan.loc[(kishan[kishan.columns[0]]) == d]
        for i in range(len(kishan.columns)):
            column = str(kishan.columns[i])
            info = jj.iloc[0,i]
            lis2[i].config(text=column)
            lis[i].config(text=info)
    except:
        pass

f2 = tk.Frame(window)
f2.grid(row=0,column=0,sticky="nsew")
f2.rowconfigure([0,1,2],minsize=10,weight=50)
f2.columnconfigure([0,1],minsize=10,weight=50)
e = tk.Entry(f2,fg="white",bg="light blue",font=[None,20],width=75)
e.grid(row=0,column=0,sticky="nsew")
b = tk.Button(f2,text="Submit",command=lambda:main(kishan),bg="light blue",font=[None,20])
b.grid(row=0,column=1,sticky="nsew")

f = tk.Frame(window,bg="light blue")
f.grid(row=1,column=0,sticky="nsew")
f.rowconfigure([0,1,2,3,4,5,6,7,8,9],minsize=50,weight=50)
f.columnconfigure([0,1,2,3],minsize=50,weight=50)
m = tk.Label(f,bg="light blue",font=[None,20])
m.grid(row=0,column=0,sticky="nsew")
m2 = tk.Label(f,bg="light blue",font=[None,20])
m2.grid(row=1,column=0,sticky="nsew")
m3 = tk.Label(f,bg="light blue",font=[None,20])
m3.grid(row=2,column=0,sticky="nsew")
m4 = tk.Label(f,bg="light blue",font=[None,20])
m4.grid(row=3,column=0,sticky="nsew")
m5 = tk.Label(f,bg="light blue",font=[None,20])
m5.grid(row=4,column=0,sticky="nsew")
m6 = tk.Label(f,bg="light blue",font=[None,20])
m6.grid(row=5,column=0,sticky="nsew")
m7 = tk.Label(f,bg="light blue",font=[None,20])
m7.grid(row=6,column=0,sticky="nsew")
m8 = tk.Label(f,bg="light blue",font=[None,20])
m8.grid(row=7,column=0,sticky="nsew")
m9 = tk.Label(f,bg="light blue",font=[None,20])
m9.grid(row=8,column=0,sticky="nsew")
m10 = tk.Label(f,bg="light blue",font=[None,20])
m10.grid(row=9,column=0,sticky="nsew")

b = tk.Label(f,bg="light blue",font=[None,20])
b.grid(row=0,column=1,sticky="nsew")
b2 = tk.Label(f,bg="light blue",font=[None,20])
b2.grid(row=1,column=1,sticky="nsew")
b3 = tk.Label(f,bg="light blue",font=[None,20])
b3.grid(row=2,column=1,sticky="nsew")
b4 = tk.Label(f,bg="light blue",font=[None,20])
b4.grid(row=3,column=1,sticky="nsew")
b5 = tk.Label(f,bg="light blue",font=[None,20])
b5.grid(row=4,column=1,sticky="nsew")
b6 = tk.Label(f,bg="light blue",font=[None,20])
b6.grid(row=5,column=1,sticky="nsew")
b7 = tk.Label(f,bg="light blue",font=[None,20])
b7.grid(row=6,column=1,sticky="nsew")
b8 = tk.Label(f,bg="light blue",font=[None,20])
b8.grid(row=7,column=1,sticky="nsew")
b9 = tk.Label(f,bg="light blue",font=[None,20])
b9.grid(row=8,column=1,sticky="nsew")
b10 = tk.Label(f,bg="light blue",font=[None,20])
b10.grid(row=9,column=1,sticky="nsew")
window.mainloop()