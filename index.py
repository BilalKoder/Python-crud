import mysql.connector
import bcrypt


#Creating new database

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pydoc")

#connecting to database

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pydoc"
)

mycursor = mydb.cursor()

#creating table in database

mycursor.execute("CREATE TABLE users(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(30) NOT NULL,email VARCHAR(60) NOT NULL,password VARCHAR(256) NOT NULL,PRIMARY KEY(id));")


#Create

# Declaring our password
password = b'click123'

#use pip install bcrypt
 
# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password, salt)

sql = "INSERT INTO users (name,email,password) VALUES (%s, %s,%s)"
val = ("Syed", "bilal.ali@koderlabs.com",hashed)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


#Fetch

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#Update 

sql = "UPDATE users SET name = 'Ali' WHERE id = 1"

mycursor.execute(sql)

mydb.commit()

#Delete 

sql = "DELETE FROM users WHERE id = 1"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")