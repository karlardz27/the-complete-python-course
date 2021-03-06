# We've already defined a movie class like this:
class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    # let's try to add a method `print_info()` here:
    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")   # <<Your Name>> by Director test

movie_1 = Movie("Your Name", "Director test")
movie_1.print_info()
