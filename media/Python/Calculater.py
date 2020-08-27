import tkinter as tk
import tkinter.font as tkFont

effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised":tk.RAISED,
    "groove":tk.GROOVE,
    "ridge":tk.RIDGE
}
window = tk.Tk()

window.minsize(530,510)
window.maxsize(530,510)
window.configure(bg="black")
fontStyle = tkFont.Font(size=50)
e = tk.Entry(bg="black", fg="white",width=80, font=fontStyle)
e.pack()
e2 = tk.Entry(bg="black",fg="white",width=50)
e2.pack()
e3 = tk.Entry(bg="black",fg="white",width=5)
e3.place(x=10, y=80)
def insert1():
    e.insert(0, "1")
def insert2():
    e.insert(0, "2")
def insert3():
    e.insert(0, "3")
def insert4():
    e.insert(0, "4")
def insert5():
    e.insert(0, "5")
def insert6():
    e.insert(0, "6")
def insert7():
    e.insert(0, "7")
def insert8():
    e.insert(0, "8")
def insert9():
    e.insert(0, "9")
def insert0():
    e.insert(0, "0")
def plus():
    out = e.get()
    e2.insert(0,out)
    e.delete(0, tk.END)
    e3.insert(0,"+")
def min():
    out = e.get()
    e2.insert(0,out)
    e.delete(0,tk.END)
    e3.insert(0,"-")
def div():
    out = e.get()
    e2.insert(0,out)
    e.delete(0,tk.END)
    e3.insert(0,"/")
def mul():
    out = e.get()
    e2.insert(0,out)
    e.delete(0,tk.END)
    e3.insert(0,"x")
def pridam():
    out2 = e.get()
    ou = e2.get()
    q = e3.get()
    out2 = int(out2)
    ou = int(ou)
    if q == "+":
        re=float(out2+ou)
    if q == "-":
        re=float(ou-out2)
    if q == "/":
        re=float(out2/ou)
    if q == "x":
        re=float(out2*ou)
    e.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e.insert(0,re)
def allcl():
    e.delete(0,tk.END) 
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
   


fontStyle = tkFont.Font(size=30)
labd1 = tk.Button(text="1", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert1)
labd2 = tk.Button(text="2", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert2)
labd3 = tk.Button(text="3", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert3)
labd4 = tk.Button(text="4", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert4)
labd5 = tk.Button(text="5", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert5)
labd6 = tk.Button(text="6", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert6)
labd7 = tk.Button(text="7", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert7)
labd8 = tk.Button(text="8", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert8)
labd9 = tk.Button(text="9", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert9)
labd0 = tk.Button(text="0", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=insert0)
labdplus = tk.Button(text="+", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=12, command=plus)
labdmin = tk.Button(text="_", width=2, bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=13, command=min)
labddiv = tk.Button(text="/", width=2, bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=12, command=div)
labdmul = tk.Button(text="x", width=2, bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=12, command=mul)
result = tk.Button(text="=", width=3, bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=12,command=pridam)
allclear = tk.Button(text="AC", bg="black", fg="white", font=fontStyle, relief=tk.GROOVE, borderwidth=12, command=allcl)

allclear.place(x=410, y=100)
labd1.place(x=10, y=100)
labd2.place(x=90, y=100)
labd3.place(x=170, y=100)
labd4.place(x=10, y=200)
labd5.place(x=90, y=200)
labd6.place(x=170, y=200)
labd7.place(x=10, y=300)
labd8.place(x=90, y=300)
labd9.place(x=170, y=300)
labd0.place(x=90, y=400)
labdplus.place(x=250, y=100)
labdmin.place(x=250, y=200)
labddiv.place(x=330, y=100)
labdmul.place(x=330, y=200)
result.place(x=410 ,y=200)



window.mainloop()