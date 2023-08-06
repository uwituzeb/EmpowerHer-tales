class CommunityForums:
    def __init__(self):
        self.discussions = []

    def add_discussion(self, title, content, author):
        discussion = {
            'title': title,
            'content': content,
            'author': author,
            'comments': []
        }
        self.discussions.append(discussion)

    def add_comment(self, discussion_idx, content, commenter):
        if discussion_idx < 0 or discussion_idx >= len(self.discussions):
            print("Invalid discussion index")
            return

        comment = {
            'content': content,
            'commenter': commenter
        }
        self.discussions[discussion_idx]['comments'].append(comment)

    def display_discussions(self):
        for idx, discussion in enumerate(self.discussions):
            print(f"Discussion {idx + 1}:")
            print(f"Title: {discussion['title']}")
            print(f"Author: {discussion['author']}")
            print(f"Content: {discussion['content']}")
            print("Comments:")
            for comment in discussion['comments']:
                print(f"  {comment['commenter']}: {comment['content']}")
            print("-" * 30)

    def share_inspiring_quote(self, quote, author):
        print("An inspiring quote from {}:\n{}".format(author, quote))


# Example usage
if __name__ == "__main__":
    forums = CommunityForums()

    forums.add_discussion("First Post", "Hello, everyone! This is my first post.", "Eunice")
    forums.add_comment(0, "Welcome! Looking forward to more posts.", "Bernice")
    forums.add_comment(0, "Great to have you here!", "Bob")

    forums.add_discussion("Thoughts on Python", "What do you think about Python programming?", "Sine")
    forums.add_comment(1, "I love Python! It's so versatile and easy to learn.", "Inocente")
    forums.add_comment(1, "Python is my favorite language too!", "Linda")

    forums.display_discussions()

    inspiring_quote = "The only limit to our realization of tomorrow will be our doubts of today. " \
                      "Let us move forward with strong and active faith. - Franklin D. Roosevelt"
    forums.share_inspiring_quote(inspiring_quote, "Franklin D. Roosevelt")
