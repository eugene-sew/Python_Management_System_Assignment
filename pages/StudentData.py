import csv
from tkinter import Frame, Label, ttk, BOTH, END, PhotoImage, CENTER, E, Toplevel, W, Entry

from tkmacosx import Button

from build.DBcon import DBCon
from build.FileOP import FileOp
from build.pages.AddPage import AddScreen

class CustomEntry(Entry):
    def __init__(self, *args, **kwargs):
        kwargs["borderwidth"] = 1
        kwargs["background"] = "white"
        kwargs["foreground"] = "black"
        kwargs["cursor"] = "ibeam"
        kwargs["insertbackground"] = "black"
        kwargs["font"] = ("Arial Regular", 19)
        super().__init__(*args, **kwargs)

class StudentData:
    db = DBCon()
    d_id =""
    def __init__(self, master):
        root = Frame(master)
        root.configure(width=924, height=695, bg='white')
        page_title = Label(root, text="Students Data", fg="white", bg="#32326B", width=924, font=("Inter SemiBold", 25),
                           pady=5)
        page_title.pack()

        col_names = ("name", "program", "level", "cgpa")
        self.table = ttk.Treeview(root, columns=col_names)
        self.table.column("#0", anchor=E, width=100, stretch=False)
        self.table.column("name", anchor=CENTER, width=200)
        self.table.column("program", anchor=CENTER, width=100, minwidth=100, stretch=False)
        self.table.column("level", anchor=CENTER, width=100, minwidth=100, stretch=False)
        self.table.column("cgpa", anchor=CENTER, width=80, stretch=False)
        self.table.pack(fill=BOTH, expand=False, padx=20, pady=40)

        self.table.heading("#0", text="Student ID")
        self.table.heading("name", text="Student Name")
        self.table.heading("program", text="Program")
        self.table.heading("level", text="Level")
        self.table.heading("cgpa", text="CGPA")
        data = self.db.fetchStudentData()
        for d in data:
            self.table.insert(parent="",
                              index=END,
                              text=str(d[0]),
                              values=(f"{d[1]} {d[2]}", d[3], d[4], d[5]))

        self.buttons_frame = Frame(root)

        # select btn
        select_btn = Button(self.buttons_frame, text="Edit Data", bg="blue", fg="white", font=("regular", 20),
                            relief="flat", command=self.select_data)
        select_btn.grid(row=0, column=0, ipadx=20, ipady=10)

        # import btn
        import_button = Button(self.buttons_frame, text="Import Student Data", command=lambda: self.get_file_data(),
                               bg="#32326B",
                               fg="white", font=("Bold", 20), relief="flat", )
        import_button.grid(row=0, column=1, ipadx=20, ipady=10)

        # refresh btn
        refresh_button = Button(self.buttons_frame, text="Refresh Data", command=lambda: self.refresh_table(),
                                bg="green",
                                fg="white", font=("Bold", 20), relief="flat", )
        refresh_button.grid(row=0, column=2, ipadx=20, ipady=10)

        # add btn
        add_button = Button(self.buttons_frame, text="Add student data", command=self.on_add_click,
                                bg="gray",
                                fg="white", font=("Bold", 20), relief="flat", )
        add_button.grid(row=0, column=3, ipadx=20, ipady=10)
        self.buttons_frame.pack()

        # edit boxes
        self.fields_frame = Frame(root)
        Label(self.fields_frame, text="first name", foreground="black", bg="white", font=("Arial Regular", 15)).grid(row=0,column=0)
        self.fname_box = CustomEntry(self.fields_frame, width=18, highlightthickness=0)
        self.fname_box.grid(row=1,column=0)

        Label(self.fields_frame, text="last name", foreground="black", bg="white", font=("Arial Regular", 15)).grid(row=0,column=1)
        self.lname_box = CustomEntry(self.fields_frame, width=18, highlightthickness=0)
        self.lname_box.grid(row=1,column=1)

        Label(self.fields_frame, text="level", foreground="black", bg="white", font=("Arial Regular", 15)).grid(row=0,column=2)
        self.lv_box = CustomEntry(self.fields_frame, width=18, highlightthickness=0)
        self.lv_box.grid(row=1,column=2)

        Label(self.fields_frame, text="cgpa", foreground="black", bg="white", font=("Arial Regular", 15)).grid(row=0,column=3)
        self.cgp_box = CustomEntry(self.fields_frame, width=18, highlightthickness=0)
        self.cgp_box.grid(row=1,column=3)

        self.op_btn_frame = Frame(self.fields_frame)
        self.op_btn_frame.grid(row=2,column=3, columnspan=2)

        # update button
        update_btn = Button(self.op_btn_frame, text="update", command=self.on_update_data_click,
                                bg="lightblue",
                                fg="white", font=("Bold", 20), relief="flat", )
        update_btn.grid(row=0, column=0,pady=10,ipady=5,sticky='w',padx=5 )

        # delete btn
        delete_btn = Button(self.op_btn_frame, text="delete", command=self.on_delete_click,
                                bg="red",
                                fg="white", font=("Bold", 20), relief="flat", )
        delete_btn.grid(row=0, column=1,pady=10,ipady=5, padx=5, sticky='e')

        self.fields_frame.pack(pady=25,padx=10)
        root.pack()

    def select_data(self):
        self.clear_box()
        selected = self.table.focus()
        values = self.table.item(selected,"values")
        self.d_id = self.table.item(selected,"text")
        name = values[0].split(" ")
        fname = name[0]
        lname = name[1]
        self.fname_box.insert(0,fname)
        self.lname_box.insert(0,lname)
        self.lv_box.insert(0,values[2])
        self.cgp_box.insert(0,values[3])



    def clear_box(self):
        self.fname_box.delete(0,'end')
        self.lname_box.delete(0,'end')
        self.lv_box.delete(0,'end')
        self.cgp_box.delete(0,'end')

    def on_update_data_click(self):
        id=self.d_id
        fn=self.fname_box.get()
        ln=self.lname_box.get()
        lv=self.lv_box.get()
        cg=self.cgp_box.get()

        rs = self.db.update_record(id=id,ln=ln,fn=fn,lv=lv,cgp=cg)
        if rs:
            n = NotifyWindow(message="Data Imported Successfully")
        else:
            n = NotifyWindow(message="Error importing data")
        pass

    def on_delete_click(self):
        id=self.d_id
        self.clear_box()
        rs = self.db.delete_data(id=id)
        if rs:
            NotifyWindow(message="Data Imported Successfully")
        else:
            NotifyWindow(message="Error importing data")
        pass

    def get_file_data(self):
        d = ImportWindow()
        # data = d.data
        # for d in data:
        #     print(d)

    def refresh_table(self):
        refdb = DBCon()
        for item in self.table.get_children():
            self.table.delete(item)
        data = refdb.fetchStudentData()
        for d in data:
            self.table.insert(parent="",
                              index=END,
                              text=str(d[0]),
                              values=(f"{d[1]} {d[2]}", d[3], d[4], d[5]))

    def on_add_click(self):
        add_window = AddScreen()

# import window opens up to view importable data
class ImportWindow(Toplevel):
    f = FileOp()
    db = DBCon()

    def __init__(self):
        super().__init__()

        self.data = self.f.import_st_file()

        self.frame = Frame(self)

        self.frame.configure(width=700, height=624)
        self.table = ttk.Treeview(self.frame)
        self.col_names = ("name", "program", "level", "cgpa")
        self.table.configure(columns=self.col_names)
        self.table.heading("#0", text="Student ID")
        self.table.heading("name", text="Student Name")
        self.table.heading("program", text="Program")
        self.table.heading("level", text="Level")
        self.table.heading("cgpa", text="CGPA")

        for d in self.data:
            self.table.insert(parent="",
                              index=END,
                              text=str(d[0]),
                              values=(f"{d[1]} {d[2]}", d[3], d[4], d[5]))

        self.buttons_frame = Frame(self.frame)

        self.ok_btn = Button(self.buttons_frame, text="Import Data", command=lambda: self.im_data(),
                             bg="green", fg="white")

        self.cancel_btn = Button(self.buttons_frame, text="Cancel", command=lambda: self.destroy(), bg="red",
                                 fg="white")
        self.frame.pack(fill=BOTH, expand=True, pady=10)
        self.table.pack(fill=BOTH, expand=False)
        self.ok_btn.grid(row=0, column=1)
        self.cancel_btn.grid(row=0, column=0)
        self.buttons_frame.pack(anchor=E)
        self.transient(self.master)
        self.grab_set()
        self.wait_window(self)

    # import data
    def im_data(self):
        print("clicked")

        filename = self.f.get_filename()
        print(filename)
        file = open(filename)
        reader = csv.reader(file)
        for d in reader:
            print(d)
            result = self.db.importData(id=d[0], fn=d[1], ln=d[2], pg=d[3], lv=d[4], cgpa=d[5])
            print(result)
        if result:
            n = NotifyWindow(message="Data Imported Successfully")
        else:
            n = NotifyWindow(message="Error importing data")

        self.destroy()


# notification box
class NotifyWindow(Toplevel):
    def __init__(self, message):
        super().__init__()

        self.frame = Frame(self)

        self.message = Label(self, text=message, fg="white")
        self.message.pack()
        self.ok_btn = Button(self, text="Okay", command=lambda: self.destroy())
        self.ok_btn.pack(anchor=CENTER, ipadx=2, )
        self.frame.pack(pady=20, padx=20)
