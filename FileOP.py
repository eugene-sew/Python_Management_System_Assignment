import csv
from tkinter import filedialog


class FileOp:
    filename = ""

    def import_st_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/Documents", title="Select a file",
                                                   filetypes=(
                                                       ("txt files", "*.txt"),
                                                       ("csv files", "*.csv"),
                                                       ("png files", "*.png"),
                                                       ("jpg files", "*.jpg"),
                                                       ("jpg files", "*.jpeg")
                                                   ))

        file = open(self.filename)
        reader = csv.reader(file)
        return reader

    def get_filename(self):
        return self.filename
