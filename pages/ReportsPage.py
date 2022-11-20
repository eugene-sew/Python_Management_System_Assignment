from tkinter import Frame, Label, ttk, BOTH, END, Button, PhotoImage
from turtle import bgpic

from build.DBcon import DBCon
from build.FileOP import FileOp


class ReportsPage:
    db = DBCon()

    def __init__(self, master):
        root = Frame(master)
        root.configure(width=924, height=695, bg='yellow')
        page_title = Label(master, text="Reports and FeedBack", fg="black", font=("Inter SemiBold", 25))
        page_title.pack()

        root.pack(padx=20, pady=10)

