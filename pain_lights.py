from ast import Lambda
import tkinter as tk
from tkinter import *
from tkinter import LabelFrame, ttk
from tkinter import scrolledtext

import click


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Світлофор")
    root.geometry("1250x700")
    root.resizable(width=False, height=False)
    
    #LabelFrames

    legend_frame = LabelFrame(root, text="Світлофор", width=600, height=500)
    legend_frame.place(x=50, y=50)
    remote_legend_frame = LabelFrame(root, text="Пульт", width=200, height=100)
    remote_legend_frame.place(x=650, y=550)
    log_legend = LabelFrame(root, text="Логи", width=300, height=200)
    log_legend.place(x=700,y=50)

    #canvas
    
    canva = [Canvas(legend_frame, height=110, width=110) for i in range(3)]
    for i in range(3):
        dx=110
        canva[i].place(x=390, y=60+i*dx) #Знаю, це мега пітонівський (ніт) цикл, але мені потрібний множник для зміщення
        canva[i].create_oval(10, 10, 100, 100, width=3)
            
    canva[0].bind("<Button-1>",lambda event: radio_clicked("red"))
    canva[1].bind("<Button-1>", lambda event: radio_clicked("yellow"))
    canva[2].bind("<Button-1>", lambda event: radio_clicked("green"))
    #widgets
    
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
    r1.place(x=50, y=300)
    r2.place(x=50, y=200)
    r3.place(x=50, y=100)

    text_log = scrolledtext.ScrolledText(log_legend,width=40)
    text_log.pack()
    clearbtn=Button(log_legend,text="Очистити",command=lambda:clear_btn())
    clearbtn.pack(pady=20)

    def clear_btn():
        text_log.delete("1.0",END)

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
        defaultbg = canva[0].cget('bg')
        if(value == "green"):
            for i in range(3):
                if(i==2):
                    canva[i].create_oval(10, 10, 100, 100, width=3, fill=value)
                else: 
                    canva[i].create_oval(10, 10, 100, 100, width=3, fill=defaultbg)
            text_log.insert(END,"зелений\n") 
        elif(value == "yellow"):
            for i in range(3):
                if(i == 1):
                    canva[i].create_oval(10, 10, 100, 100, width=3, fill=value)
                else:
                    canva[i].create_oval(10, 10, 100, 100, width=3, fill=defaultbg)
            text_log.insert(END, "жовтий\n")
        else:
            for i in range(3):
                if(i == 0):
                    canva[i].create_oval(10, 10, 100, 100, width=3, fill=value)
                else:
                    canva[i].create_oval(10, 10, 100, 100, width=3, fill=defaultbg)
            text_log.insert(END, "червоний\n")

    root.mainloop()
