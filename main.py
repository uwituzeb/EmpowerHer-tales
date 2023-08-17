import mysql.connector
from database import create_database_and_table, register_user, login_user, get_profession_by_username, populate_stories
from resourcelist import display_resources
from community_forums import CommunityForums

b = CommunityForums()


def display_themes():
    themes = {
        1: "Doctor Stories",
        2: "Engineer Stories",
        3: "Art",
        4: "fisher"
    }
    for theme_id, theme_name in themes.items():
        print(f"{theme_id}. {theme_name}")


def read_stories_by_theme(theme_id):
    themes = {
        1: "doctor",
        2: "engineer",
        3: "art",
        4: "fisher"
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
        database="empowerhertales"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, story FROM stories WHERE profession = %s",
        (profession,)
    )
    stories = cursor.fetchall()
    conn.close()
    return stories


def leave_comment( story_id,username, comment):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="empowerhertales"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO comments (story_id, username, comment) VALUES (%s, %s, %s)",
        (story_id, username, comment)
    )
    conn.commit()
    conn.close()


def save_story(title, story, profession):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="empowerhertales"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO stories(title, story, profession) VALUES (%s, %s, %s)",
        (title, story, profession)
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database_and_table()
    populate_stories()
    user = None  # Initialize user as None

    banner_text = """
*********************************************
*       Welcome To Empower Her Tails        *
*********************************************
"""

    print(banner_text)
    while True:


        if not user:  # If user is not logged in

            print("1. Register\n2. Login\n3. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("\n--- Register ---")
                username = input("Enter username: ")
                password = input("Enter password: ")
                profession = input("Enter your profession: ")
                register_user(username, password, profession)
                print("User registered successfully!")

            elif choice == 2:
                print("\n--- Login ---")
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = login_user(username, password)
                if user:
                    print("Login successful!")
                    print("________________________________________________________________")
                else:
                    print("Invalid username or password.")

            elif choice == 3:
                break

            else:
                print("Invalid choice. Try again.")

        else: 
            print("\nWelcome to the main menu of Empower her\n")
            print("1. Share story\n2. Read a story\n3. Leave comment\n4. Resources\n5. Community building\n6. Logout\n7. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("\n--- Share Story ---")
                title = input("Enter the story's title: ")
                story = input("Enter the story: ")
                profession= input("Enter your profession :")
                save_story(title, story, profession)  
                print("Story shared successfully!")

            elif choice == 2:
                print("\n--- Read a Story ---")
                print("Select a theme:")
                display_themes()
                theme_id = int(input("Enter theme ID: "))
                read_stories_by_theme(theme_id)

            elif choice == 3:
                print("\n--- Leave Comment ---")
                story_id = int(input("Enter the story ID to leave a comment: "))
                comment = input("Enter your comment: ")
                leave_comment(user[1], story_id, comment)
                print("Comment left successfully!")
                print("________________________________________________________________")

            elif choice == 4:
                print("\n--- Resources ---")
                display_resources()

            elif choice == 5:
                print("\n--- Community Building ---")
                b = CommunityForums()
                b.share_inspiring_()

            elif choice == 6:
                print("\n--- Logout ---")
                user = None  
                print("Logged out successfully!")

            elif choice == 7:
                break

            else:
                print("Invalid choice. Try again.")
