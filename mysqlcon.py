import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user= "hassan401",
    password = "HumaHassan8",
    port = "3306",
    database = "2d_platformer"
)

mycursor = db.cursor()

mycursor.execute("SELECT * FROM user")

users = mycursor.fetchall()

for user in users:
    print(user)