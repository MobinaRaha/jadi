import mysql.connector

cnx = mysql.connector.connect(user ='root' , password = 'ada9zajqwpMYSQL' ,
                             host ='localhost', database = 'learn')
cursor = cnx.cursor()

query = "Select* From people"
cursor.execute(query)
for(name , age , gender) in cursor:
    print(f'name is {name} , age is {age} and gender is {gender}')
cnx.close()


