import mysql.connector
cnx = mysql.connector.connect(user ='root' , password = '********' ,
                             host ='localhost', database = 'project')
cursor = cnx.cursor()

cursor.execute("INSERT INTO Employee(name , weight, height) VALUES('Amin' , 75 , 180),('Mahdi' ,90 , 190) ,('Mohammad' , 75, 190) , ('Ahmad' , 60 ,175) ")
cursor.execute("SELECT* FROM Employee")
rows = cursor.fetchall()
print(rows)
rows.sort(key= lambda tuple_item: (tuple_item[2],tuple_item[1] ) , reverse=True)

for i in range(len(rows)-1):
    if rows[i][2] == rows[i + 1][2]:
        even_rows = [rows[i], rows[i + 1]]
        even_rows.sort(key=lambda tuple_item: tuple_item[1])
        rows[i], rows[i+1]= even_rows
        print(even_rows)

cnx.commit()
cursor.close()
cnx.close()
