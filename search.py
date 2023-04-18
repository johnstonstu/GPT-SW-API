class MovieSearch:
    def __init__(self, movies):
        self.movies = movies

    def search(self, query):
        results = []
        for movie in self.movies:
            if query.lower() in movie["title"].lower():
                results.append(movie["title"])
        return results
