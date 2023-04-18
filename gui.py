import tkinter as tk
from api import StarWarsAPI

class StarWarsAPIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Star Wars API App")

        self.movies_listbox = tk.Listbox(self.root, width=50)
        self.movies_listbox.pack(padx=10, pady=10)

        self.load_button = tk.Button(self.root, text="Load More Movies", command=self.load_movies)
        self.load_button.pack(padx=10, pady=10)

        self.api = StarWarsAPI()
        self.movies = []
        self.next_page = 1

    def run(self):
        self.root.mainloop()

    def load_movies(self):
        movies, next_page = self.api.get_movies(page=self.next_page)
        self.movies += movies
        self.next_page += 1

        self.movies_listbox.delete(0, tk.END)
        for movie in self.movies:
            self.movies_listbox.insert(tk.END, movie["title"])

        if next_page is None:
            self.load_button.config(state=tk.DISABLED)
