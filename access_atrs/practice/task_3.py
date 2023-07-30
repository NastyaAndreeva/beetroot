class Post:
    def __init__(self, content, author, number_of_likes):
        self.content = content
        self.author = author
        self.__number_of_likes = number_of_likes

    def display_the_post(self):
        print(self.content)
        print(f"The author is: {self.author}")
        print(f"The number of likes is: {self.__number_of_likes}")

    def dislike(self):
        self.__number_of_likes -= 1

post_1 = Post("I hate Python modifiers!!!", "Anastasiia", 100)
post_1.dislike()
post_1.display_the_post()