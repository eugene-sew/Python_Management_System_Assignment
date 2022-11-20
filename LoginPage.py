from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# from build.ControlPage import ControlWindow
from build.ManagePage import ManageWindow
from build.DBcon import DBCon


class LoginWindow(Tk):
    db = DBCon()

    def __init__(self):
        super().__init__()
        self.fonty = "Helvetica 20"
        self.title("Ho Technical University")
        self.geometry("745x517")
        # self.geometry("1124x695")

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=517,
            width=745,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file="./assets/login/image_1.png")
        self.image_1 = self.canvas.create_image(159.0, 259.0, image=self.image_image_1)

        self.canvas.create_text(
            411.0,
            63.0,
            anchor="nw",
            text="Ho Technical University",
            fill="#323469",
            font=("Inter Bold", 21 * -1)
        )

        self.canvas.create_text(
            415.0,
            91.0,
            anchor="nw",
            text="I.T Department Student Records",
            fill="#000000",
            font=("Inter Regular", 15 * -1)
        )

        self.canvas.create_text(
            409.0,
            452.0,
            anchor="nw",
            text="forgot password ?",
            fill="#000000",
            font=("Inter Regular", 15 * -1)
        )

        self.canvas.create_text(
            543.0,
            452.0,
            anchor="nw",
            text="reset password",
            fill="#FC0E0E",
            font=("Inter Regular", 15 * -1),

        )

        self.canvas.create_text(
            370.0,
            173.0,
            anchor="nw",
            text="Index No/ Staff ID :",
            fill="#000000",
            font=("Inter Regular", 15 * -1)
        )

        self.canvas.create_text(
            370.0,
            265.0,
            anchor="nw",
            text="Password :",
            fill="#000000",
            font=("Inter Regular", 15 * -1)
        )

        self.entry_image_1 = PhotoImage(file="./assets/login/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            529.5,
            219.5,
            image=self.entry_image_1
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#DFDADA",
            fg="#000000",
            font=self.fonty,
            highlightthickness=0,

        )
        self.entry_1.place(
            x=378.0,
            y=199.0,
            width=303.0,
            height=39.0
        )

        self.entry_image_2 = PhotoImage(
            file="./assets/login/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            529.5,
            311.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#DFDADA",
            fg="#000000",
            font=self.fonty,
            highlightthickness=0,
            show="*",

        )
        self.entry_2.place(
            x=378.0,
            y=291.0,
            width=303.0,
            height=39.0
        )

        self.error = self.canvas.create_text(
            370.0,
            410.0,
            anchor="nw",
            text="",
            fill="#000000",
            font=("Inter Regular", 15 * -1)
        )
        self.button_image_1 = PhotoImage(file="./assets/login/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginHandler,
            relief="flat"
        )
        self.button_1.place(
            x=370.0,
            y=366.0,
            width=319.0,
            height=41.0
        )

    def loginHandler(self):
        self.canvas.itemconfig(self.error, text="Signing In ..... ",fill="blue")
        if self.db.login(self.entry_1.get(), self.entry_2.get()):
            self.withdraw()
            
            c_win = ManageWindow(self)
            c_win.deiconify()
        else:
            self.canvas.itemconfig(self.error, text="User not found...  Enter correct details ", fill="#FF0000")
            print(f"{self.entry_1.get()} not found")


if __name__ == "__main__":
    loginWindow = LoginWindow()
    loginWindow.mainloop()
