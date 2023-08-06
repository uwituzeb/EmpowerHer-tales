import mysql.connector

def create_database_and_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS test")
    cursor.close()

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            profession VARCHAR(255) NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS stories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            story VARCHAR(255) NOT NULL,
            profession VARCHAR(255) NOT NULL
        )
        """
    )
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS comments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            comment VARCHAR(255) NOT NULL,
            story_id INT NOT NULL
        )
        """
    )
    conn.commit()
    cursor.close()
    conn.close()


def register_user(username, password, profession):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password, profession) VALUES (%s, %s, %s)",
        (username, password, profession)
    )
    conn.commit()
    conn.close()


def login_user(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    return user


def get_profession_by_username(username):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT profession FROM users WHERE username = %s", (username,))
    profession = cursor.fetchone()
    conn.close()
    return profession[0] if profession else None

def populate_stories():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()

    stories = [
        {"title": "The Skilled Doctor", "story": "Once upon a time, there was a skilled doctor...", "profession": "doctor"},
        {"title": "The Talented Engineer", "story": "In the land of engineers, there lived a talented...", "profession": "engineer"},
        {"title": "Art", "story": "In the of beautifull art, there lived a talented...", "profession": "art"},

    ]

    for story_data in stories:
        cursor.execute(
            "INSERT INTO stories (title, story, profession) VALUES (%s, %s, %s)",
            (story_data["title"], story_data["story"], story_data["profession"])
        )

    conn.commit()
    conn.close()
    
def leave_comment(username, story_id, comment):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO comments (story_id, username, comment) VALUES (%s, %s, %s)",
        (story_id, username, comment)
    )
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    populate_stories()
