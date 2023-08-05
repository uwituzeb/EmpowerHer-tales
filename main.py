from database import create_database_and_table, register_user, login_user, get_profession_by_username, populate_stories

import mysql.connector


def get_story_by_profession(profession):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT story FROM stories WHERE profession = %s",
        (profession,)
    )
    story = cursor.fetchone()
    conn.close()
    return story[0] if story else "Sorry, no story available for this profession."


def get_story_by_profession(username):
    profession = get_profession_by_username(username)
    print(profession)

    if profession:
        stories = {
            "doctor": "Once upon a time, there was a skilled doctor...",
            "engineer": "In the land of engineers, there lived a talented...",
            "art": "The art is another story"
        }
        return stories.get(profession, "Sorry, no story available for this profession.")
    else:
        return "User not found or profession not specified."
    
def write_to_file(shared_stories.txt, shared_stories_content):
    with open(shared_stories, 'w') as file:
        file.write(shared_stories_content)

def read_from_file(shared_stories.txt):
    with open(shared_stories, 'r') as file:
        data = file.read()
        print(data)


if __name__ == "__main__":
    create_database_and_table()
    populate_stories()

    while True:
        print("1. Register\n2. Login\n3. Read a story\n4. Share your story\n5. Exit")
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
            if user in locals() and user:
                profession = user[3]
                if not profession:
                    print("You haven't provided a profession.")
                else:
                    stories = get_story_by_profession(profession)
                    if stories:
                        for story in stories:
                            print(f"Title: {profession.capitalize()} Story\n{story[0]}\n")
                    else:
                        print("Sorry, no stories available for this profession.")
            else:
                print("Please login first.")
        
        
        elif choice == 4:
            if user in locals() and user:
                profession = user[3]
                if not profession:
                    print("You haven't provided a profession.")
                else:
                    shared_stories_content = input("Enter your story: ")
                    view_story = input("View shared stories? y/n")
                    view_story.lower()
                    if view_story == 'y':
                        read_from_file()
                    elif view_story == 'n':
                        break
                    else:
                        print("Invalid choice. Answer y or n")
                        
                
        
        elif choice == 5:
            print("Thank you for using our application. Goodbye.")
            break;

        else:
            print("Invalid choice. Try again.")