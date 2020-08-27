import math
import tkinter as tk
from datetime import datetime
from tkinter import *
window = tk.Tk()
window.geometry("400x400")
window.resizable(False,False)
window.rowconfigure(0,minsize=10,weight=10)
window.columnconfigure(0,minsize=10,weight=10)

class Poition:
    def __init__(self,Time,Ticks,Size_Of_Hand,Width,PT):
        self.Time = Time
        self.Ticks = Ticks
        self.Size_Of_Hand = Size_Of_Hand
        self.Width = Width
        Per_Angle = 360/Ticks
        Angle = Per_Angle*Time
        if Ticks < Time :
            Time = Time-Ticks
        x1 = 200+(math.sin(math.radians(Angle))*Size_Of_Hand)
        y1 = 200-(math.cos(math.radians(Angle))*Size_Of_Hand)
        self.Hand = Body.create_line(x1,y1,200,200,width=Width,fill="red")
        self.Point = Body.create_oval(x1-10,y1-10,x1+10,y1+10,fill="red")
        self.PointText = Body.create_text(x1,y1,text=PT,fill="white")
        self.Num = Body.create_text(200+(math.sin(math.radians(Angle))*175),200-(math.cos(math.radians(Angle))*175),text=Time,fill="white")


def Tim_(Hand,Point,Num,PointNum,Hand2,Point2,Num2,PointNum2,Hand3,Point3,Num3,PointNum3):
    if Hand == None:
        pass
    else:
        Body.delete(Hand,Point,Num,PointNum,Hand2,Point2,Num2,PointNum2,Hand3,Point3,Num3,PointNum3)
    time = datetime.today()
    Second = Poition(time.second,60,150,4,"S")
    Minute = Poition(time.minute,60,130,4,"M")
    Hour = Poition(time.hour,12,110,4,"H")
    Body.after(900,Tim_,Second.Hand,Second.Point,Second.Num,Second.PointText,
    Minute.Hand,Minute.Point,Minute.Num,Minute.PointText,
    Hour.Hand,Hour.Point,Hour.Num,Hour.PointText)
Body = tk.Canvas(window,bg="black")
Body.grid(row=0,column=0,sticky="nsew")
Body.create_rectangle(25,25,375,375,fill="white")
Body.create_oval(0,0,400,400,fill="black")
Body.create_oval(190,190,210,210,fill="red")
Hand = None
Point = None
Num = None
PointNum = None
Hand2 = None
Point2 = None
Num2 = None
PointNum2 = None
Hand3 = None
Point3 = None
Num3 = None
PointNum3 = None
if __name__ == '__main__':
    Tim_(Hand,Point,Num,PointNum,Hand2,Point2,Num2,PointNum2,Hand3,Point3,Num3,PointNum3)
window.mainloop()