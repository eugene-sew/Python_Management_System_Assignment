import csv

import mysql.connector


class DBCon:
    mydb = ""
    cursor = ""
    ldb_name = "users"
    sdb_name = "students"
    password = ""

    def __init__(self):
        self.is_import = None
        self.mydb = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password=self.password,
            database=self.sdb_name
        )

        self.cursor = self.mydb.cursor()

    def login(self, uid, password):
        query = "select staff_id,role from {} where {} = '{}' and {} = '{}'".format(self.ldb_name, "staff_id", uid,
                                                                                    "password", password)
        self.cursor.execute(query)
        rs = self.cursor.fetchone()
        if rs is None:
            return False
        else:
            return True

    def fetchStudentData(self):
        query = "select * from {}".format(self.sdb_name)
        self.cursor.execute(query)
        rs = self.cursor.fetchall()
        return rs

    def importData(self, id, fn, ln, pg, lv, cgpa):
        query = f"insert into {self.sdb_name} values ('{id}','{fn}','{ln}','{pg}','{int(lv)}','{float(cgpa)}')"

        try:
            self.cursor.execute(query)
            self.mydb.commit()
            self.is_import = True
        except:
            self.mydb.rollback()
            self.is_import = False

        return self.is_import


    def update_record(self,id,fn,ln,lv,cgp):
        query = f"update {self.sdb_name} set first_name='{fn}',last_name='{ln}',level={int(lv)},cgpa='{float(cgp)}' where index_no='{id}'"

        try:
            self.cursor.execute(query)
            self.mydb.commit()
            self.is_import = True
        except:
            self.mydb.rollback()
            self.is_import = False

        return self.is_import

    def delete_data(self,id):
        query=f"DELETE FROM {self.sdb_name} WHERE index_no='{id}'"
        try:
            self.cursor.execute(query)
            self.mydb.commit()
            self.is_import = True
        except:
            self.mydb.rollback()
            self.is_import = False

        return self.is_import
        # UPDATE Customers
        # SET ContactName = 'Alfred Schmidt', City = 'Frankfurt'
        # WHERE CustomerID = 1;
