import oracledb as orc
class View:
    def viewtudentdata(self):
        try:
            con=orc.connect("system/*****@localhost/orcl")
            cur=con.cursor()
            sq="select * from student"
            cur.execute(sq)
            #Get the Col Name
            print("-"*50)
            for colinfo in cur.description:
                print("\t{}".format(colinfo[0]),end="\t")
            print()
            print("-" * 50)
            #Get the records
            records=cur.fetchall()
            for record in records:
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            print("-" * 50)

        except orc.DatabaseError as db:
            print("Problem in Oracle in DB:",db)

#Main Program
