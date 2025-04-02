import oracledb as orc
class Table:
    # table creation
    def createstutable(self):
        try:
            self.connection = orc.connect("system/kajal@localhost/orcl")
            self.cursor = self.connection.cursor()
            cq = "create table student(sno number(3) primary key,name varchar(10) not null,cgpa number(4,2) not null,college varchar(20) not null)"
            self.cursor.execute(cq)
            print("Student Table Created Successfully--verify")
        except orc.DatabaseError as db:
            print("Problem with Oracle Database=", db)

#main program
s1=Table()
s1.createstutable()