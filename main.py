import mysql.connector
from database import create_database_and_table, register_user, login_user, get_profession_by_username, populate_stories
from resourcelist import display_resources
from community_forums import CommunityForums


def display_themes():
    themes = {
        1: "Doctor Stories",
        2: "Engineer Stories",
        3: "Art",
    }
    for theme_id, theme_name in themes.items():
        print(f"{theme_id}. {theme_name}")


def read_stories_by_theme(theme_id):
    themes = {
        1: "doctor",
        2: "engineer",
        3: "art"
    }
    theme = themes.get(theme_id)
    if theme:
        stories = get_story_by_profession(theme)
        if stories:
            for i, story in enumerate(stories, start=1):
                print(f"{i}. {story}")
            return True
    print("Sorry, no stories available for this theme.")
    return False


def get_story_by_profession(profession):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, story FROM stories WHERE profession = %s",
        (profession,)
    )
    stories = cursor.fetchall()
    conn.close()
    return stories


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
    create_database_and_table()
    populate_stories()

    forums = CommunityForums() 
    
    while True:
        print("1. Register\n2. Login\n3. Read a story\n4. leave comment\n5. resources\n6. community_forums\n7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            profession = input("Enter your profession: ")
            register_user(username, password, profession)
            print("User registered successfully!")

        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = login_user(username, password)
            if user:
                print("Login successful!")
            else:
                print("Invalid username or password.")

        elif choice == 3:
            if "user" in locals() and user:
                print("Select a theme:")
                display_themes()
                theme_id = int(input("Enter theme ID: "))
                read_stories_by_theme(theme_id)
            else:
                print("Please login first.")

        elif choice == 4:
            if "user" in locals() and user:
                story_id = int(
                    input("Enter the story ID to leave a comment: "))
                comment = input("Enter your comment: ")
                leave_comment(user[1], story_id, comment)
            else:
                print("Please login first.")

        elif choice == 5:
            display_resources()

        elif choice == 6:
            
            CommunityForums.display_discussions(self)
        
        elif choice == 7:
            break

        else:
            print("Invalid choice. Try again.")
