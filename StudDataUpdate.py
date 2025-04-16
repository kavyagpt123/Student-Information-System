import oracledb as orc
class Update:
    def getdata(self):
        self.sno = int(input("Enter Student Number for Updating Details of student:"))
        self.newname = input("Enter New Student Name:")
        self.newmarks = float(input("Enter New Marks:"))

    def updatedata(self):
        while (True):
            try:
                con = orc.connect("system/*****@localhost/orcl")
                cur = con.cursor()
                self.getdata()
                uq = "update student set name='%s',marks=%f where sno=%d"
                cur.execute(uq % (self.newname, self.newmarks, self.sno))
                con.commit()
                if (cur.rowcount > 0):
                    print("\t{} Record Updated Successfully".format(cur.rowcount))
                else:
                    print("\tRecord Does not Exits")
                ch = input("Do you want to Update Another Record(yes/no):")
                if (ch.lower() == 'no'):
                    print("Thank For using This Application")
                    break
            except orc.DatabaseError as db:
                print("Problem with Oracle Database", db)
            except ValueError:
                print("Don't Enter alphanum,str and symbols for Student number and cgpa")
#main program




