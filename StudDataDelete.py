#StudDataDelete.py-->file name and module name
import oracledb as orc
class Delete:
    def deletedata(self):
        while(True):
            try:
                con = orc.connect("system/kajal@localhost/orcl")
                cur = con.cursor()
                self.sno=int(input("Enter Student Number for Deleting the Record:"))
                dq = "delete from student where sno=%d" % self.sno
                print("-" * 50)
                cur.execute(dq)
                con.commit()
                if (cur.rowcount > 0):
                    print("\t{} Record Deleted Successfully".format(cur.rowcount))
                else:
                    print("\tRecord Does not Exists")
                print("-" * 50)
                ch = input("Do you want to Delete Another Record(yes/no):")
                if (ch.lower() == 'no'):
                    print("Thanks for using this Application")
                    break

            except orc.DatabaseError as db:
                print("Problem with Oracle Database=", db)

            except ValueError:
                print("Don't Enter Alphanum,str and symbols for student number")

#main program



