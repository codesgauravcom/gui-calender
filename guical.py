from tkinter import *
import calendar
root = Tk()

root.title('my own gui calender')

year = 2020

mycal = calendar.calendar(year)

cal_year = Label(root, text=mycal, font='consolas 10 bold')

cal_year.pack()


root.mainloop()