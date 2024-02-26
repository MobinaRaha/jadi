import re
import mysql.connector
cnx = mysql.connector.connect(user ='root' , password = 'ada9zajqwpMYSQL' ,
                             host ='localhost', database = 'project')
cursor = cnx.cursor()
#cursor.execute("create table data_input(username varchar(25),password varchar(25) ) ")
cursor.execute("ALTER TABLE data_input MODIFY COLUMN username VARCHAR(255)")
username = input("username: ")
password = input("password: ")

if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', username) and re.match(r'[a-zA-Z0-9._%+-]{8,}',password):
    print("Valid email address")
    cursor.execute("INSERT INTO data_input(username , password) VALUES(%s , %s)" , (username , password))
    cnx.commit() 
    print("Data inserted successfully")
else:
    print("Invalid email address, please enter like: example@example.com")

cursor.close()
cnx.close()
