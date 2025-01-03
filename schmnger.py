# 1. To create database ‘school’ and table ‘student’
def create():
    import mysql.connector as mys
    con = mys.connect(host='localhost', user='root', password="deepika", database="")
    cur = con.cursor()
    print("#" * 40)
    print("Database creation and table creation")
    print("#" * 40)
    print("\n\n")
    query = "create database if not exists school"
    cur.execute(query)
    query = "DROP DATABASE IF EXISTS school"
    cur.execute(query)
    query = "CREATE DATABASE school"
    cur.execute(query)

    query = "use school"
    cur.execute(query)
    query = "create table if not exists students(grno int primary key, name char(20), classs int(5), section char(5), grade char(5))"
    cur.execute(query)

# 2. To insert records into table ‘student’
def insertrecord():
    import mysql.connector as mys
    con = mys.connect(host='localhost', user='root', password="deepika", database="school")
    cur = con.cursor()
    print("#" * 40)
    print("ADDING RECORDS OF STUDENTS")
    print("#" * 40)
    print("\n\n")
    ans = 'y'
    while ans.lower() == 'y':
        grno = int(input("ENTER GR NO OF STUDENT :"))
        name = input("ENTER NAME :")
        classs = input("ENTER CLASS :")
        section = input("ENTER SECTION:")
        grade = input("ENTER GRADE(A,B,C)")
        query = "insert into students values({0},'{1}','{2}','{3}','{4}')".format(grno, name, classs, section, grade)
        cur.execute(query)
        con.commit()
        ans = input("ADD MORE (Y/N) :")

# 3. To display records
def showall():
    import mysql.connector as mys
    con = mys.connect(host='localhost', user='root', password="deepika", database="school")
    cur = con.cursor()
    print("#" * 40)
    print("DISPLAY ALL STUDENT DETAILS")
    print("#" * 40)
    print("\n\n")
    query = "select * from students"
    cur.execute(query)
    result = cur.fetchall()
    if cur.rowcount == 0:
        print("Sorry! No records in this database")
    else:
        print("DISPLAYING THE RECORDS\n")
        for row in result:
            print(row)

# 4. To search records
def search():
    import mysql.connector as mys
    con = mys.connect(host='localhost', user='root', password="deepika", database="school")
    cur = con.cursor()
    print("#" * 40)
    print("STUDENT SEARCHING FORM")
    print("#" * 40)
    print("\n\n")
    ans = 'y'
    while ans.lower() == 'y':
        no = int(input("ENTER STUDENT GRNO TO SEARCH :"))
        query = "select * from students where grno={}".format(no)
        cur.execute(query)
        result = cur.fetchall()
        if cur.rowcount == 0:
            print("Sorry! No records in this database ")
        else:
            print("FOUND THE RECORD...")
            for row in result:
                print(row)
        ans = input("SEARCH MORE RECORDS? (Y/N) :")

# 5. To update records
def update():
    import mysql.connector as mys
    con = mys.connect(host='localhost', user='root', password="deepika", database="school")
    cur = con.cursor()
    print("#" * 40)
    print("STUDENT UPDATE FORM")
    print("#" * 40)
    print("\n\n")
    ans = 'y'
    while ans.lower() == 'y':
        no = int(input("Enter grno for updation of record :"))
        query = "select * from students where grno={}".format(no)
        cur.execute(query)
        print(cur)
        result = cur.fetchall()
        if result != None:
            print("found")
            for row in result:
                print(row)
                an = input("What do you want to update?\n(Enter 1 - Name\n2-Class\n3-Grade):")
                if an == '1':
                    s1 = input("ENTER new Name :")
                    query = "update students set name='{}' where grno={}".format(s1, no)
                    cur.execute(query)
                    print("Name updated1")
                    con.commit()
                elif an == '2':
                    s1 = input("Enter new class :")
                    query = "update students set classs='{}' where grno={}".format(s1, no)
                    cur.execute(query)
                    print("Class updated!")
                    con.commit()
                elif an == '3':
                    s1 = input("Enter new grade:")
                    query = "update students set grade='{}' where grno={}".format(s1, no)
                    cur.execute(query)
                    print("Grade updated!")
                    con.commit()
                else:
                    print("Sorry! Wrong choice..")
        else:
            print("Sorry! No records in this database ")
        ans = input("SEARCH MORE (Y) :")

# 6. To delete records
def deleterec():
    import mysql.connector as mys
    con = mys.connect(host='localhost', user='root', password="deepika", database="school")
    cur = con.cursor()
    print("#" * 40)
    print("SCHOOL delete FORM")
    print("#" * 40)
    print("\n\n")
    no = int(input("ENTER grno for deletion of record:"))
    query = "select * from students where grno={}".format(no)
    cur.execute(query)
    print(cur)
    result = cur.fetchall()
    if result != None:
        print("found")
        for row in result:
            print(row)
            an = input("do you want to delete (Y) :")
        if an == 'Y' or an == 'y':
            query = "delete from students where grno={}".format(no)
            cur.execute(query)
            print("Record successfully deleted")
            con.commit()
    else:
        print("Sorry! No records in this database ")

# 7. Menu driven program
def menu():
    print("#" * 40)
    print("SCHOOL MANAGEMENT SYSTEM")
    print("#" * 40)
    print("\n")
    print("\n1.CREATE DATABASE AND STUDENTS TABLE")
    print("\n2.ADD RECORDS IN STUDENTS TABLE")
    print("\n3.DISPLAY ALL RECORDS")
    print("\n4.SEARCH FOR A RECORD")
    print("\n5.UPDATE A RECORD")
    print("\n6.DELETE A RECORD")
    ans = "y"
    while ans.lower() == "y":
        ch = int(input("ENTER CHOICE"))
        if ch == 1:
            create()
        elif ch == 2:
            insertrecord()
        elif ch == 3:
            showall()
        elif ch == 4:
            search()
        elif ch == 5:
            update()
        elif ch == 6:
            deleterec()
        else:
            print("EXITING, Bye!")
        ans = input("WANT TO CONTINUE?")

menu()