from studentMenu import Menu
from CreateStudentTable import Table
from StudentAdd import Student
from StudDataDelete import Delete
from StudDataUpdate import Update
from StudDataSearch import Search
from StudentDetailsView import View
class St:pass

#main program
s=St()

while(True):
    try:
        m=Menu()
        m.menu()
        ch=int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                s1 = Table()
                s1.createstutable()
            case 2:
                    s = Student()
                    s.insertstuddata()
            case 3:
                d = Delete()
                d.deletedata()
            case 4:
                u = Update()
                u.updatedata()
            case 5:
                s = Search()
                s.detailsearch()
            case 6:
                v = View()
                v.viewtudentdata()

            case 7:
                print("Thanks For using This Application")
                break
            case _:
                print("Your Selection of choice is Wrong---try again")
    except ValueError:
        print("Don't Try to enter Alphanum, str and symbols")

