import mysql.connector as con

class Phone_lib:

    def __init__(self,fname = None , lname = None , contact = None):

            self.dbCon = con.connect(host="localhost", user="root", passwd="root", database="plib")
            self.myCur = self.dbCon.cursor()
            self.fname = fname
            self.lname = lname
            self.contact = contact

    def Add_contact(self):
        self.fname = input("Enter FirstName : ")
        self.lname = input("Enter LastName : ")
        self.contact = int(input("Enter contact no :"))
        AddQuery = "insert into pinfo values('{}', '{}',{})".format(self.fname, self.lname, self.contact)
        self.myCur.execute(AddQuery)
        print(self.myCur.rowcount, "Record inserted!!!!!!")
        self.dbCon.commit()


    def searchContact(self):
        self.fname = input("Enter fname for search:")
        searchQuery = "select * from pinfo where fname='{}'".format(self.fname)
        self.myCur.execute(searchQuery)
        print(searchQuery)
        std1 = self.myCur.fetchall()
        for row in std1:
            print(row)
        self.dbCon.commit()

    def updateContact(self):

        self.fname = input("Enter fname for update : ")
        searchCon = "select * from pinfo where fname = '{}'".format(self.fname)
        self.myCur.execute(searchCon)
        Conon = self.myCur.fetchone()
        print(Conon)
        print("------------------record update ------------------")
        self.fname = input("Enter FirstName : ")
        self.lname = input("Enter LastName : ")
        self.contact = input("Enter contact no :")

        updateQuery ="update pinfo set fname ='{}',lname='{}',contact='{}'".format(self.fname, self.lname, self.contact)
        self.myCur.execute(updateQuery)
        self.dbCon.commit()


    def deletContact(self):

        self.fname = input("Enter fname for delet :")
        searchCon = "delete from pinfo where fname = '{}'".format(self.fname)
        self.myCur.execute(searchCon)
        Conon1 = self.myCur.fetchone()
        print(Conon1)
        for x in Conon1:
            print(x)
        self.dbCon.commit()

    def viewContact(self):

        viewQuery = "select * from pinfo"
        self.myCur.execute(viewQuery)
        view1 = self.myCur.fetchall()
        for x in view1:
                print(x)
        print(self.myCur.rowcount, "")
        self.dbCon.commit()

exit = True

contactobj =  Phone_lib()

while(exit):
    print('''
    
    1. view contact
    2. Add new contact
    3. search contact
    4. edit contact
    5. delete contact
    6. Exit app

    ''')


    b = int(input("Enter Your choice : "))

    if b == 1:
        contactobj.viewContact()

    elif b == 2:
        contactobj.Add_contact()

    elif b == 3:
        contactobj.searchContact()

    elif b == 4:
        contactobj.updateContact()

    elif b == 5:
        contactobj.deletContact()

    elif b == 6:
        print("Exit!!!!!!!!")


        break





   
