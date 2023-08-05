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
    
def write_to_database(profession, content):
    conn = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )
        
    sql = "INSERT INTO shared_stories(profession, story) VALUES (%s, %s)"
    data = (profession, content)
    
    cursor = conn.cursor()
    cursor.execute(sql, data)
    conn.commit()
        
    print("Story shared successfully!")   
    cursor.close()
    conn.close()
  

       





def read_from_database(profession):
    conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database"
        )

    cursor = conn.cursor()
    cursor.execute(
        "SELECT story FROM shared_stories WHERE profession = %s",
    (profession,)
    )
    story = cursor.fetchone()
        
    return story[0] if story else "Sorry, no story available for this profession."

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
            profession = input("Enter a profession: ")
            content = input("Enter your story: ")
            write_to_database(profession, content)
            view_story = input("View shared stories? y/n")
            view_story.lower()

            if view_story == 'y':
                read_profession = input("Enter profession to read story: ")
                result = read_from_database(read_profession)
                print(result)
            elif view_story == 'n':
                break
            else:
                print("Invalid choice. Answer y or n")
                        
                
        
        elif choice == 5:
            print("Thank you for using our application. Goodbye.")
            break;

        else:
            print("Invalid choice. Try again.")