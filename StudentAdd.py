#StudentAdd.py--->file name and module name
import oracledb as orc
import sys
sys.path.append("C:/Users/DELL/PycharmProjects/PythonProject/ExceptionHandling")
from Namevalidation import namevalidate
from Namevalidation import ZeroLengthError, SpaceError, InvalidNameError
class Student():
    def getStudval(self):
        self.sno=int(input("Enter Student Number:"))
        self.name=namevalidate(input("Enter Student Name:"))
        self.marks=float(input("Enter Student Marks:"))
    def insertstuddata(self):
        while(True):
            try:
                self.getStudval()
                con = orc.connect("system/*****@localhost/orcl")
                cur = con.cursor()
                iq = "insert into student values(%d,'%s',%f)"
                cur.execute(iq % (self.sno, self.name, self.marks))
                con.commit()
                print("{} Record Inserted".format(cur.rowcount))
                ch = input("Do you want to Insert Another Record(yes/no):")
                if (ch == 'no'):
                    print("Thanks for using this Application")
                    break

            except orc.DatabaseError as db:
                print("Problem with Oracle Database", db)
            except ValueError:
                print("Don't Enter Alphanum, str and symbols")
            except ZeroLengthError:
                print("\t You must enter your Student name and College name")
            except SpaceError:
                print("\tDon't enter space for Student name and College name")
            except InvalidNameError:
                print("\tStudent Name and College name is invalid")

#main program



