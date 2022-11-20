from pathlib import Path
from tkinter import Tk, Frame, LEFT, PhotoImage, Label, END, CENTER, RIGHT, Toplevel, Canvas, Entry, ttk, BOTH
from tkmacosx import Button
from build.DBcon import DBCon
from build.FileOP import FileOp
from build.pages.MarkingPage import MarkingPage
from build.pages.ReportsPage import ReportsPage
from build.pages.StudentData import StudentData


class ManageWindow(Toplevel):
    db = DBCon()
    #
    def __init__(self,master):
        super().__init__(master)
    # def __init__(self):
    #     super().__init__()
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("pages/assets")
        self.geometry("1124x695")
        self.configure(bg="#FFFFFF")
        self.state("zoomed")
        self.title("Department  of Computer Science")
        self.btn_x_offset = 23
        # sidebar
        self.sidebar_frame = Frame(self, bg="#32326B")
        self.sidebar_frame.pack(side=LEFT)
        self.sidebar_frame.pack_propagate(False)
        self.sidebar_frame.configure(width=200, height=695)

        # logo
        self.image_image_1 = PhotoImage(
            file="pages/assets/image_1.png")
        self.image_1 = Label(self.sidebar_frame, image=self.image_image_1, )
        self.image_1.pack()
        self.image_1.place(x=50, y=20)

        # sidebar buttons
        # student data
        self.std_img = PhotoImage(
            file="pages/assets/button_1.png")
        self.student_data_btn = Button(self.sidebar_frame,
                                       image=self.std_img,
                                       relief="flat",
                                       # bd=0,
                                       borderwidth=0,
                                       highlightthickness=0,
                                       command=lambda: self.add_indicator(self.std_indicator, self.std_page)
                                       )
        self.student_data_btn.place(x=self.btn_x_offset,
                                    y=150,
                                    width=176.0,
                                    height=39.0)

        self.std_indicator = Label(self.sidebar_frame, bg="#32326B")
        self.std_indicator.place(x=0, y=150, width=5, height=40)

        # marking table
        self.asses_img = PhotoImage(
            file="pages/assets/button_2.png")
        self.marking_btn = Button(self.sidebar_frame,
                                  image=self.asses_img,
                                  relief="flat",
                                  bd=0,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  command=lambda: self.add_indicator(self.mk_indicator,self.marking_table_page)

                                  )
        self.marking_btn.place(x=self.btn_x_offset,
                               y=200,
                               width=176.0,
                               height=39.0, )
        self.mk_indicator = Label(self.sidebar_frame, bg="#32326B")
        self.mk_indicator.place(x=0, y=200, width=5, height=40)

        # reports
        self.rep_img = PhotoImage(
            file="pages/assets/button_3.png")
        self.report_btn = Button(self.sidebar_frame,
                                 image=self.asses_img,
                                 relief="flat",
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 command=lambda: self.add_indicator(self.rpt_indicator,self.reports_page)
                                 )
        self.report_btn.place(x=self.btn_x_offset,
                              y=250,
                              width=176.0,
                              height=39.0, )
        self.rpt_indicator = Label(self.sidebar_frame, bg="#32326B")
        self.rpt_indicator.place(x=0, y=250, width=5, height=40)

        # logout
        self.logout_img = PhotoImage(
            file="pages/assets/button_4.png")
        self.logout_btn = Button(self.sidebar_frame,
                                 image=self.logout_img,
                                 relief="flat",
                                 bd=0,
                                 borderwidth=0,
                                 highlightthickness=0,
                                 command=lambda: self.destroy()
                                 )
        self.logout_btn.place(x=9.0,
                              y=645.0,
                              width=176.0,
                              height=39.0,

                              )
        # main
        self.main_frame = Frame(self,
                                highlightbackground="black",
                                highlightthickness=0)
        self.main_frame.pack(side=LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=924, height=695)

    def std_page(self):
        s = StudentData(self.main_frame)


    def marking_table_page(self):
        m = MarkingPage(self.main_frame)

    def reports_page(self):
        r = ReportsPage(self.main_frame)

    def delete_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()

    def rem_indicator(self):
        self.std_indicator.configure(bg="#32326B")
        self.mk_indicator.configure(bg="#32326B")
        self.rpt_indicator.configure(bg="#32326B")

    def add_indicator(self, lb, page):
        self.rem_indicator()
        lb.configure(bg="white")
        self.delete_page()
        page()



if __name__ == "__main__":
    controlWindow = ManageWindow()
    controlWindow.resizable(False, False)
    controlWindow.mainloop()
