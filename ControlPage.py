from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel, ttk

from build.DBcon import DBCon


class ControlWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("pages/assets")
        self.geometry("1124x695")
        self.configure(bg="#FFFFFF")
        self.state("zoomed")
        self.title("Department  of Computer Science")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=695,
            width=1124,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.entry_image_1 = PhotoImage(file="pages/assets/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            636.5,
            116.52120208740234,
            image=self.entry_image_1
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=262.0,
            y=92.0,
            width=749.0,
            height=47.04240417480469
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            193.0,
            695.0,
            fill="#323469",
            outline="")

        self.image_image_1 = PhotoImage(
            file="pages/assets/image_1.png")
        self.image_1 = self.canvas.create_image(
            104.0,
            94.0,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(
            file="pages/assets/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=17.0,
            y=213.0,
            width=176.0,
            height=39.0
        )

        self.button_image_2 = PhotoImage(
            file="pages/assets/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=17.0,
            y=264.0,
            width=176.0,
            height=39.0
        )

        self.button_image_3 = PhotoImage(
            file="pages/assets/button_3.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=17.0,
            y=315.0,
            width=176.0,
            height=39.0
        )

        # logout button
        self.button_image_4 = PhotoImage(
            file="pages/assets/button_4.png")
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=9.0,
            y=645.0,
            width=176.0,
            height=39.0
        )

        self.canvas.create_text(
            267.0,
            61.0,
            anchor="nw",
            text="Search",
            fill="#000000",
            font=("Inter SemiBold", 18 * -1)
        )

        self.canvas.create_text(
            267.0,
            150.0,
            anchor="nw",
            text="Search Criteria",
            fill="#8D8D8D",
            font=("Inter SemiBold", 18 * -1)
        )

        self.canvas.create_text(
            262.0,
            186.0,
            anchor="nw",
            text="*names",
            fill="#CD3535",
            font=("Inter Regular", 16 * -1)
        )

        self.canvas.create_text(
            418.0,
            186.0,
            anchor="nw",
            text="*class",
            fill="#CD3535",
            font=("Inter Regular", 16 * -1)
        )

        self.canvas.create_text(
            480.0,
            186.0,
            anchor="nw",
            text="*age",
            fill="#CD3535",
            font=("Inter Regular", 16 * -1)
        )

        self.canvas.create_text(
            335.0,
            186.0,
            anchor="nw",
            text="*position",
            fill="#CD3535",
            font=("Inter Regular", 16 * -1)
        )

        self.button_image_5 = PhotoImage(
            file="pages/assets/button_5.png")
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=1011.0,
            y=92.0,
            width=70.0,
            height=49.0
        )

        self.button_image_6 = PhotoImage(
            file="pages/assets/button_6.png")
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=404.38677978515625,
            y=377.2232666015625,
            width=212.64151000976562,
            height=195.77674865722656
        )

        self.button_image_7 = PhotoImage(
            file="pages/assets/button_7.png")
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=652.3457641601562,
            y=377.0,
            width=210.65420532226562,
            height=195.60748291015625
        )

        self.entry_image_2 = PhotoImage(
            file="pages/assets/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            636.5,
            116.52120208740234,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#F4F4F4",
            highlightthickness=0
        )
        self.entry_2.place(
            x=262.0,
            y=92.0,
            width=749.0,
            height=47.04240417480469
        )




if __name__ == "__main__":
    controlWindow = ControlWindow()
    controlWindow.resizable(False,False)
    controlWindow.mainloop()
