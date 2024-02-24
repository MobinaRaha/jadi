import mysql.connector
print('connecting...')
cnx = mysql.connector.connect(user ='root' , password = 'ada9zajqwpMYSQL' ,
                             host ='localhost', database = 'learn')
print('connected :) ')
cursor = cnx.cursor()
values = ("Rachel", 32, "F")
cursor.execute("INSERT INTO people (name , age , gender) VALUES (%s, %s , %s)", values)
cnx.commit()
cursor.close()
cnx.close()


