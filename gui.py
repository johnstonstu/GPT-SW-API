import tkinter as tk
from api import StarWarsAPI
from fileio import *
from search import MovieSearch
from details import *

class StarWarsAPIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Star Wars API App")

        self.movies_listbox = tk.Listbox(self.root, width=50)
        self.movies_listbox.pack(padx=10, pady=10)

        self.load_button = tk.Button(self.root, text="Load More Movies", command=self.load_movies)
        self.load_button.pack(padx=10, pady=10)

        self.planets_button = tk.Button(self.root, text="Load More Planets", command=self.load_planets)
        self.planets_button.pack(padx=10, pady=10)

        self.starships_button = tk.Button(self.root, text="Load More Starships", command=self.load_starships)
        self.starships_button.pack(padx=10, pady=10)

        self.search_label = tk.Label(self.root, text="Search:")
        self.search_label.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_movies)
        self.search_button.pack(side=tk.LEFT, padx=10)

        self.api = StarWarsAPI()
        self.movies = []
        self.planets = []
        self.starships = []
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

    def load_planets(self):
        planets, next_page = self.api.get_planets(page=self.next_page)
        self.planets += planets
        self.next_page += 1

        self.movies_listbox.delete(0, tk.END)
        for planet in self.planets:
            self.movies_listbox.insert(tk.END, planet["name"])

        if next_page is None:
            self.planets_button.config(state=tk.DISABLED)

    def load_starships(self):
        starships, next_page = self.api.get_starships(page=self.next_page)
        self.starships += starships
        self.next_page += 1

        self.movies_listbox.delete(0, tk.END)
        for starship in self.starships:
            self.movies_listbox.insert(tk.END, starship["name"])

        if next_page is None:
            self.starships_button.config(state=tk.DISABLED)

    def search_movies(self):
        query = self.search_entry.get()
        if query:
            movie_search = MovieSearch(self.movies)
            results = movie_search.search(query)
            self.movies_listbox.delete(0, tk.END)
            for result in results:
                self.movies_listbox.insert(tk.END, result)

    def run(self):
        self.root.mainloop()
