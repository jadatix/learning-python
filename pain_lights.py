from ast import Lambda
import tkinter as tk
from tkinter import *
from tkinter import LabelFrame, ttk

import click


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Світлофор")
    root.geometry("1250x700")
    root.resizable(width=False, height=False)
    
    legend_frame = LabelFrame(root, text="Світлофор", width=600, height=500)
    legend_frame.place(x=50, y=50)
    remote_legend_frame = LabelFrame(root, text="Пульт", width=200, height=100)
    remote_legend_frame.place(x=650, y=550)
    
    canva = Canvas(legend_frame, height=330, width=110,
                   highlightthickness=1, highlightbackground="black")
    canva.place(x=390, y=60)
    canva.create_oval(10, 10, 100, 100, width=3)
    canva.create_oval(10, 120, 100, 210, width=3)
    canva.create_oval(10, 230, 100, 320, width=3)
    
    isChecked = IntVar(value=1)
    checkbox = Checkbutton(remote_legend_frame, text="вкл.",
                           variable=isChecked, onvalue=1, offvalue=0, command=lambda: check(isChecked.get()))
    checkbox.place(x=50,y=25)
    color = StringVar()
    r1 = Radiobutton(legend_frame, text="Green", variable=color,
                     value="green", command=lambda: radio_clicked(color.get()))
    r2 = Radiobutton(legend_frame, text="Yellow", variable=color,
                     value="yellow", command=lambda: radio_clicked(color.get()))
    r3 = Radiobutton(legend_frame, text="Red", variable=color,
                     value="red", command=lambda: radio_clicked(color.get()))
    r1.place(x=50, y=100)
    r2.place(x=50, y=200)
    r3.place(x=50, y=300)

    def check(value):
        if(value == 0):
            r1.config(state=DISABLED)
            r2.config(state=DISABLED)
            r3.config(state=DISABLED)
        else:
            r1.config(state=NORMAL)
            r2.config(state=NORMAL)
            r3.config(state=NORMAL)

    def radio_clicked(value: str):
        defaultbg = canva.cget('bg')
        if(value == "green"):
            canva.create_oval(10, 10, 100, 100, width=3, fill=value)
            canva.create_oval(10, 120, 100, 210, width=3, fill=defaultbg)
            canva.create_oval(10, 230, 100, 320, width=3, fill=defaultbg)
        elif(value == "yellow"):
            canva.create_oval(10, 10, 100, 100, width=3, fill=defaultbg)
            canva.create_oval(10, 120, 100, 210, width=3, fill=value)
            canva.create_oval(10, 230, 100, 320, width=3, fill=defaultbg)
        else:
            canva.create_oval(10, 10, 100, 100, width=3, fill=defaultbg)
            canva.create_oval(10, 120, 100, 210, width=3, fill=defaultbg)
            canva.create_oval(10, 230, 100, 320, width=3, fill=value)


    root.mainloop()
