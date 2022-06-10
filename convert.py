#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
# Created By  : Alaa Albayed
# Created Date: 6/9/2022
# version = 1.0

""" This program help people to convert currency """

from tkinter import *
from tkinter import ttk

# from PIL import ImageTk, Image


root = Tk()
root.config(bg="#6207a8")
root.title("Convert Currency")
root.minsize(600, 600)

result = Text(root, width=26, height=3, fg="#000000", bg="#ffffff", font=('Helvatical bold', 15))
lbW = Label(text="Welcome to Simple program to \n Convert Currency ", fg="#ffffff", bg="#6207a8",
            font=('Helvatical bold', 20))

Clist = ["USD", "JOD", "EUR"]

drop = ttk.Combobox(root, values=Clist)
drop.set("Select first Currency")
drop1 = ttk.Combobox(root, values=Clist)
drop1.set("Select second Currency")

lbAmount = Label(text="Enter your Amount", fg="#ffffff", bg="#6207a8", font=('Helvatical bold', 13))
entryAmount = Entry(root, width=25)


# --------- function to convert currency   ----------

def convert():
    result.delete(1.0, END)

    if str(entryAmount.get()) == "" and drop.get() == "EUR" and drop1.get() == "JOD":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "EUR" and drop1.get() == "USD":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "EUR" and drop1.get() == "EUR":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "USD" and drop1.get() == "USD":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "USD" and drop1.get() == "EUR":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "USD" and drop1.get() == "JOD":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "JOD" and drop1.get() == "JOD":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "JOD" and drop1.get() == "USD":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif str(entryAmount.get()) == "" and drop.get() == "JOD" and drop1.get() == "EUR":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif drop.get() == "USD" and drop1.get() == "JOD":

        getAmount = float(entryAmount.get())
        x = str(getAmount * 0.71) + " JOD"
        result.insert(END, x)

    elif drop.get() == "JOD" and drop1.get() == "USD":

        getAmount = float(entryAmount.get())
        x = str(getAmount * 1.41) + " USD"

        result.insert(END, x)

    elif drop.get() == "EUR" and drop1.get() == "JOD":

        getAmount = float(entryAmount.get())
        x = str(getAmount * 0.75777) + " JOD"

        result.insert(END, x)

    elif drop.get() == "JOD" and drop1.get() == "EUR":

        getAmount = float(entryAmount.get())
        x = str(getAmount * 1.31945) + " EUR"

        result.insert(END, x)

    elif drop.get() == "USD" and drop1.get() == "EUR":

        getAmount = float(entryAmount.get())
        x = str(getAmount * 0.93549) + " EUR"

        result.insert(END, x)

    elif drop.get() == "EUR" and drop1.get() == "USD":

        getAmount = float(entryAmount.get())
        x = str(getAmount * 1.06879) + " USD"

        result.insert(END, x)

    elif drop.get() == "USD" and drop1.get() == "USD":

        getAmount = float(entryAmount.get())
        x = str(getAmount) + " USD"
        result.insert(END, x)

    elif drop.get() == "JOD" and drop1.get() == "JOD":

        getAmount = float(entryAmount.get())
        x = str(getAmount) + " JOD"

        result.insert(END, x)

    elif drop.get() == "EUR" and drop1.get() == "EUR":

        getAmount = float(entryAmount.get())
        x = str(getAmount) + " EUR"

        result.insert(END, x)

    elif str(entryAmount.get()) == "":

        x = "please enter your ammount!"
        result.insert(END, x)

    elif drop.get() == "Select first Currency" and drop1.get() == "Select second Currency":

        x = "please select currncy to convert !"
        result.insert(END, x)

    elif drop.get() == "Select first Currency" and drop1.get() == "USD":

        x = "please Select first Currency"
        result.insert(END, x)

    elif drop.get() == "Select first Currency" and drop1.get() == "JOD":

        x = "please Select first Currency"
        result.insert(END, x)

    elif drop.get() == "Select first Currency" and drop1.get() == "EUR":

        x = "please Select first Currency"
        result.insert(END, x)

    elif drop.get() == "USD" and drop1.get() == "Select second Currency":

        x = "please Select second Currency"
        result.insert(END, x)

    elif drop.get() == "JOD" and drop1.get() == "Select second Currency":

        x = "please Select second Currency"
        result.insert(END, x)

    elif drop.get() == "EUR" and drop1.get() == "Select second Currency":

        x = "please Select second Currency"
        result.insert(END, x)


# --------- function to close program   ----------

def close():
    root.destroy()


# --------- function to reset elements ----------

def reset():
    drop.set("Select first Currency")
    drop1.set("Select second Currency")
    entryAmount.delete(0, END)
    result.delete(1.0, END)


# ------------ ALL BUTTON ------------

ConvertBtn = Button(text="Convert", command=convert, width=15, fg="#000000", bg="#ffffff")
Close = Button(text="Exit", command=close, width=15, fg="#000000", bg="#ffffff")
reset = Button(text="Reset", command=reset, width=15, fg="#000000", bg="#ffffff")

# ------------ Place elements in a specific place ------------

lbW.place(x=110, y=50)
drop.place(x=60, y=200)
drop1.place(x=350, y=200)
lbAmount.place(x=210, y=290)
entryAmount.place(x=205, y=320)
reset.place(x=50, y=409)
ConvertBtn.place(x=240, y=409)
Close.place(x=430, y=409)
result.place(x=140, y=509)

root.mainloop()
