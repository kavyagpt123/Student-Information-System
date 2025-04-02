import oracledb as orc
class Search:
    import oracledb as orc
    def detailsearch(self):
        while (True):
            try:
                connection = orc.connect("system/kajal@localhost/orcl")
                cursor = connection.cursor()
                # Search Student Details based on Student Number
                self.sno = int(input("Enter Student Number for Searching Student Details:"))
                sq = "select * from student where sno=%d"
                cursor.execute(sq % self.sno)

                records = cursor.fetchall()
                if not records:
                    print("Records Does not Exits")
                else:
                    print("*" * 50)
                    # Get the Col Names from cursor object'
                    for studinfo in cursor.description:
                        print("\t{}".format(studinfo[0]), end="\t")
                    print()
                    print("*" * 50)
                # Get the records'
                for record in records:
                        for val in record:
                            print("\t{}".format(val), end="\t")
                        print()
                        print("-"*50)

                self.ch = input("Do you want to search Another Student Details(yes/no):")
                if (self.ch.lower() == 'no'):
                    print("Thanks for using this application")
                    break


            except orc.DatabaseError as db:
                print("Problem with Oracle Database", db)
#main program
#s = Search()
#s.detailsearch()