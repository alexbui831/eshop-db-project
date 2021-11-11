#test for github
import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",password="mysql",database="shoppingcart")
cursor = connection.cursor()
selectquery="SELECT * from useraccount"
cursor.execute(selectquery)
records = cursor.fetchall()

for row in records:
  print("userid:", row[0])
  print("firstname:", row[1])
  print("lastname:", row[2])
  print("email:", row[3])
  print("address:", row[4])

  print()

cursor.close()
connection.close()