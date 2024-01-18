#!G:\python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>Welcome to My page</h1>")

Form=cgi.FieldStorage()
FName=Form.getvalue("name")
FPassword=Form.getvalue("password")

#print("<h1>",FName,FPassword,"</h1>")

print("Record stored.......Thank You for Register mr/ms",FName)

mydp=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="amazon"
    )
mycursor=mydp.cursor();
sql="INSERT INTO register(Name,Password)VALUES(%s,%s)";
val=(FName,FPassword);
mycursor.execute(sql,val)
mydp.commit()

print("</body>")
print("</html>")
