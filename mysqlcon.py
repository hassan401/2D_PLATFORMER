import mysql.connector
import mysql

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="HumaHassan8",
    port="3306",
    database="2d_platformer"
)

mycursor = db.cursor()


mycursor.execute("SELECT * FROM users")

users = mycursor.fetchall()

for user in users:
    print(user)








