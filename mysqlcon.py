import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="HumaHassan8",
    port="3306",
    database="2d_platformer"
)

mycursor = db.cursor()

mycursor.execute("DROP TABLE IF EXISTS leaderboards")
mycursor.execute("DROP TABLE IF EXISTS time")
mycursor.execute("DROP TABLE IF EXISTS scores")
mycursor.execute("DROP TABLE IF EXISTS users")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        score INT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

# Creating time table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS time (
    user_id INTEGER NOT NULL,
    score_id INTEGER NOT NULL,
    user_time TIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (score_id) REFERENCES scores(id)
)
""")

# Creating leaderboards table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS leaderboards (
    user_id INTEGER NOT NULL,
    score_id INTEGER NOT NULL,
    username VARCHAR(255) UNIQUE,
    PRIMARY KEY (user_id, score_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (score_id) REFERENCES scores(id)
)
""")


# Displaying the leaderboard
mycursor.execute("""
SELECT l.username, s.score, t.user_time
FROM leaderboards l
JOIN scores s ON l.score_id = s.id
JOIN time t ON l.user_id = t.user_id
ORDER BY s.score DESC, t.user_time
""")

leaderboard = mycursor.fetchall()

for entry in leaderboard:
    print(entry)

db.commit()
db.close()
