from tkinter import *
import time

window = Tk()
window.title("Digital Clock")
window.geometry("600x400")


def mytime():
    hour = time.strftime("%I")  # "%H"
    minute = time.strftime("%M")
    second = time.strftime("%S")
    AM_PM = time.strftime("%p")
    day = time.strftime("%A")
    zone = time.strftime("%Z")

    mytext = hour + ":" + minute + ":" + second + " " + AM_PM
    mytext2 = day + "," + zone
    myLabel.config(text=mytext)
    myLabel2.config(text=mytext2)
    myLabel.after(1000, mytime)


myLabel = Label(
    window, text="", font=("arial", 23), foreground="white", background="green"
)  # این لیبل رو به پنجره Window اختصاص بده
myLabel.pack()
myLabel2 = Label(window, text="", font=("Arial", 24))
myLabel2.pack()
mytime()
window.mainloop()
