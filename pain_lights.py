from ast import Lambda
from email.policy import default
import tkinter as tk
from tkinter import *
from tkinter import LabelFrame, ttk
from turtle import color


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Світлофор")
    root.geometry("1250x700")
    root.resizable(width=False, height=False)
    legend_frame = LabelFrame(root, text="Світлофор", width=600, height=500)
    legend_frame.place(x=50, y=50)
    canva = Canvas(legend_frame, height=330, width=110,
                   highlightthickness=1, highlightbackground="black")
    canva.place(x=390, y=60)
    canva.create_oval(10, 10, 100, 100, width=3)
    canva.create_oval(10, 120, 100, 210, width=3)
    canva.create_oval(10, 230, 100, 320, width=3)
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
