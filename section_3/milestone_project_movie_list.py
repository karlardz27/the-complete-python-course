movies = []

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see the movies, 'f' to find a movie by title, or 'q' to quit: "


def add_movie():
    title = input("Enter you movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def list_movies():
    if movies:
        for movie in movies:
            print(f"{movie}")
    else:
        print("There are no movies.")


def find_movie():
    counter = 0
    title = input("Enter you movie title: ")
    for movie in movies:
        if movie["title"] == title:
            print(f"{movie}")
            counter = counter + 1
    if counter == 0:
        print("There is no movie with that title.")


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            list_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)


menu()
