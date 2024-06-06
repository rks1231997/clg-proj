import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        usr = "root",
        password = "root",
        database = "ayush"
        )

print(mydb)

cursor = mydb.cursor()

ret = "select * from mydb.employee"

cursor.execute(ret)

print(cursor.fetchall)

var1 = "insert into employee(empid, name, mobile, gender, email) 
        values(%s, %s, %s, %s, %s)"

var2 = ("12", "tanu", "88987883", "f", "tanu1234@gmail.com")

cursor.execute()

mydb.commit()

print(cursor.fetchall()) 
