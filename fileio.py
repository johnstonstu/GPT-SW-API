import json

class MovieFile:
    def __init__(self, filename):
        self.filename = filename

    def read_movies(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def write_movies(self, movies):
        with open(self.filename, "w") as f:
            json.dump(movies, f)
