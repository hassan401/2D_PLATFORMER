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

# class Database:
#     def __init__(self):
#         self.

def farzad(x, y):
    username = x
    password = y
    n = 4
    mycursor.execute("""
    INSERT INTO `2d_platformer`.`users`
    (`userid`,
    `username`,
    `password`)
    VALUES
    (n),(username),(password);
    """)

farzad("hello","poop")

mycursor.execute("""
INSERT INTO `2d_platformer`.`users`
(`userid`,
`username`,
`password`)
VALUES
("3","oddsdfsfp","O3dfdPe");
""")
mycursor.execute("SELECT * FROM users")

users = mycursor.fetchall()

for user in users:
    print(user)








