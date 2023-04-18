import requests
import tkinter as tk

class StarWarsAPIApp:
    def __init__(self):
        # Initialize the GUI
        self.root = tk.Tk()
        self.root.title("Star Wars API App")

        # Create a listbox to display the movie titles
        self.movies_listbox = tk.Listbox(self.root, width=50)
        self.movies_listbox.pack(padx=10, pady=10)

        # Create a button to load more movies
        self.load_button = tk.Button(self.root, text="Load More Movies", command=self.load_movies)
        self.load_button.pack(padx=10, pady=10)

        # Initialize the movie data
        self.movies = []
        self.next_page = "https://swapi.dev/api/films/"

    def run(self):
        # Start the GUI event loop
        self.root.mainloop()

    def load_movies(self):
        # Make a request to the Star Wars API
        response = requests.get(self.next_page)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the JSON data from the response
            data = response.json()

            # Check if there is a next page of movies
            if "next" in data:
                # Add the movies to the list and update the next page URL
                self.movies += data["results"]
                self.next_page = data["next"]

                # Clear the listbox and repopulate it with the updated movie data
                self.movies_listbox.delete(0, tk.END)
                for movie in self.movies:
                    self.movies_listbox.insert(tk.END, movie["title"])
            else:
                # Disable the load button if there are no more movies
                self.load_button.config(state=tk.DISABLED)
        else:
            # Print an error message if the request failed
            print(f"Error: {response.status_code}")



if __name__ == "__main__":
    # Create and run the Star Wars API app
    app = StarWarsAPIApp()
    app.run()
