from datetime import date
from tkinter import *

today = date.today()

window = Tk()
window.title('Age Calculator!')

year1 = 365
month1 = today.day
tody1 = today.day


def exit():
    window.destroy()


def get_age():
    t1.delete("1.0", "end")
    d = int(e1.get())
    m = int(e2.get())
    y = int(e3.get())
    age = today.year - y - ((today.month, today.day) < (m, d))
    day = age * 365
    print(today.month - m)

    if (age >= 0):

        t1.insert(END, age)
    else:
        t1.insert(END, "Invalid Year")


def get_ageInDay():
    result1 = get_age() * 365
    t2.insert(result1)


window.minsize(600, 350)
window.config(bg="#F7DC6F")

l1 = Label(window, text="The Age Calculator!", font=("Arial", 20), fg="black", bg="#F7DC6F")
l2 = Label(window, font=("Arial", 12), text="Enter your birthday which includes the day-month-year.", fg="black",bg="#F7DC6F")
l_n = Label(window, text="Name: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")
l_d = Label(window, text="Day: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")
l_m = Label(window, text="Month: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")
l_y = Label(window, text="Year: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")
e1 = Entry(window, width=10)
e2 = Entry(window, width=10)
e3 = Entry(window, width=10)
e4 = Entry(window, width=10)

b1 = Button(window, text="Calculate Age!", font=("Arial", 13), command=get_age)

l3 = Label(window, text="Age is:", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")
l5 = Label(window, text="Year:", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")
l6 = Label(window, text="Month: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")
l7 = Label(window, text="Day: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")

t1 = Text(window, width=7, height=0)

t2 = Text(window, width=7, height=0)

t3 = Text(window, width=7, height=0)

b2 = Button(window, text="Exit Application!", font=("Arial", 13), command=exit)

l1.place(x=200, y=5)
l2.place(x=140, y=40)
l_d.place(x=10, y=90)
l_m.place(x=10, y=120)
l_y.place(x=10, y=150)
l_n.place(x=10, y=180)
e1.place(x=80, y=93)
e2.place(x=80, y=123)
e3.place(x=80, y=153)
e4.place(x=80, y=183)
b1.place(x=100, y=250)
l3.place(x=350, y=93)
l5.place(x=350, y=123)
l6.place(x=350, y=153)
l7.place(x=350, y=180)
t1.place(x=450, y=123)
t2.place(x=450, y=153)
t3.place(x=450, y=180)
b2.place(x=350, y=250)
window.mainloop()