from tkinter import Frame, Toplevel, Label, Entry, CENTER, OptionMenu, StringVar

from tkmacosx import Button

from build.DBcon import DBCon


class CustomEntry(Entry):
    def __init__(self, *args, **kwargs):
        kwargs["borderwidth"] = 1
        kwargs["background"] = "white"
        kwargs["foreground"] = "black"
        kwargs["cursor"] = "ibeam"
        kwargs["insertbackground"] = "black"
        kwargs["font"] = ("Arial Regular", 19)
        super().__init__(*args, **kwargs)


class AddScreen(Toplevel):
    db = DBCon()

    def __init__(self):
        super().__init__()
        self.geometry("600x800")
        self.configure(bg="#FFFFFF")
        self.state("zoom")
        self.title("Ho Technical University")
        self.width = 1000

        self.frame = Frame(self)
        self.frame.configure(bg="white")
        Label(self.frame, text="Add Student Record", foreground="black", bg="white", font=("Arial Bold", 20)).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=20)

        Label(self.frame, text="Index Number: ", foreground="black", bg="white",
              font=("Arial Regular", 20)).grid(row=1, column=0, pady=20, sticky="w")
        self.sn = CustomEntry(self.frame, width=20, highlightthickness=0)
        self.sn.grid(row=1, column=1)
        self.sn.focus_set()

        Label(self.frame, text="First Name: ", foreground="black", bg="white", font=("Arial Regular", 20)).grid(row=2,
                                                                                                                sticky="w")
        self.fn = CustomEntry(self.frame, width=20, highlightthickness=0)
        self.fn.grid(row=2, column=1)

        Label(self.frame, text="Last Name: ", foreground="black", bg="white", font=("Arial Regular", 20)).grid(row=3,
                                                                                                               sticky="w")
        self.ln = CustomEntry(self.frame, width=20, highlightthickness=0)
        self.ln.grid(row=3, column=1)

        Label(self.frame, text="Program: ", foreground="black", bg="white", font=("Arial Regular", 20)).grid(row=4,
                                                                                                             sticky="w")
        p_options = [
            "BT_ICT", "HND_IT", "BT_CS", "HND_CS"
        ]

        # datatype of menu text
        self.p_clicked = StringVar()

        # initial menu text
        self.p_clicked.set("BT_ICT")

        # Create Dropdown menu
        self.pg = OptionMenu(self.frame, self.p_clicked, *p_options)
        self.pg.configure(width=25)
        self.pg.grid(row=4, column=1)

        Label(self.frame, text="Level: ", foreground="black", bg="white", font=("Arial Regular", 20)).grid(row=5,
                                                                                                           sticky="w")
        # Dropdown menu options
        options = [
            "100", "200", "300", "400"
        ]

        # datatype of menu text
        self.y_clicked = StringVar()

        # initial menu text
        self.y_clicked.set("100")

        # Create Dropdown menu
        self.lv = OptionMenu(self.frame, self.y_clicked, *options)
        self.lv.configure(width=25)
        self.lv.grid(row=5, column=1)

        Label(self.frame, text="CGPA: ", foreground="black", bg="white", font=("Arial Regular", 20)).grid(row=6,
                                                                                                          sticky="w")
        self.cgp = CustomEntry(self.frame, width=20, highlightthickness=0)
        self.cgp.grid(row=6, column=1)

        self.add_btn = Button(self.frame, text="Add Book Record", command=self.add_data, width=250, height=40,
                              background="green", font=("Arial Bold", 23), foreground="white", relief="flat", bd=0,
                              borderwidth=0, highlightthickness=0)
        self.add_btn.grid(row=8, column=0, columnspan=2, pady=(10, 5), padx=20)

        self.cancel_btn = Button(self.frame, text="Cancel", command=lambda: self.destroy(), width=250, height=40,
                                 background="red", font=("Arial Bold", 23), foreground="black", relief="flat", bd=0,
                                 borderwidth=0, highlightthickness=0)
        self.cancel_btn.grid(row=9, column=0, columnspan=2, pady=(10, 0), padx=20)


        self.frame.pack()

    def add_data(self):
        sn = self.sn.get()
        fn = self.fn.get()
        ln = self.ln.get()
        pg = self.p_clicked.get()
        lv = self.y_clicked.get()
        cgp = self.cgp.get()
        self.clear()
        rs = self.db.importData(id=sn, fn=fn, ln=ln, pg=pg, lv=lv, cgpa=cgp)
        if rs:
            n = NotifyWindow(message="Data Imported Successfully")
        else:
            n = NotifyWindow(message="Error importing data")

    def clear(self):
        self.sn.delete(0, 'end')
        self.fn.delete(0, 'end')
        self.ln.delete(0, 'end')
        self.cgp.delete(0, 'end')


class NotifyWindow(Toplevel):
    def __init__(self, message):
        super().__init__()

        self.frame = Frame(self)

        self.message = Label(self, text=message, fg="white")
        self.message.pack()
        self.ok_btn = Button(self, text="Okay", command=lambda: self.destroy())
        self.ok_btn.pack(anchor=CENTER, ipadx=2, )
        self.frame.pack(pady=20, padx=20)
