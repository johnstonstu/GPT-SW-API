import requests

class StarWarsAPI:
    def __init__(self):
        self.base_url = "https://swapi.dev/api/"

    def get_movies(self, page=1):
        url = f"{self.base_url}films/?page={page}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data["results"], data["next"]
        else:
            return [], None
