class MovieDetails:
    def __init__(self, movie_id):
        self.api = StarWarsAPI()
        self.movie_id = movie_id

    def get_details(self):
        url = f"{self.api.base_url}films/{self.movie_id}/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
