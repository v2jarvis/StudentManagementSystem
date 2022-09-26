import sqlite3 as sql
con=sql.connect("iimt")
qry="create table if not exists student_info(roll int,name varchar(25),email varchar(30),phone varchar(10))"
cur=con.cursor()
cur.execute(qry)
con.commit()
while True:
    print("1 Add Student Record ")
    print("2 Display All Student Record ")
    print("3 Display Student Record by RollNo ")
    print("4 Exit ")
    choice=int(input("Enter choice: "))
    if choice == 1:
        r=int(input("Enter Roll Number: "))
        n=(input("Enter Name: "))
        e=(input("Enter E-mail: "))
        p=int(input("Enter Phone No: "))
        qry="insert into student_info values(%d,'%s','%s',%d)"%(r,n,e,p)
        cur.execute(qry)
        con.commit()
        if cur.rowcount>0:
            print("Record Inserted")
        else:
            print("Not Inserted")
    elif choice==2:
        qry="select * from student_info"
        cur.execute(qry)
        for i in cur.fetchall():
            print(i)
    elif choice==3:
        qry="select * from student_info where roll=%d"%(r)
        cur.execute(qry)
        print(cur.fetchone())

