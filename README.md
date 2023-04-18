# Star Wars API App

This is a Python application that accesses the [Star Wars API](https://swapi.dev/) and allows the user to view and search for information about movies, planets, and starships in the Star Wars universe.

## Installation

1. Clone the repository to your local machine.
2. Install the required packages by running the following command in your terminal: `pip install -r requirements.txt`.

## Usage

1. Run the `main.py` file to launch the application.
2. Use the buttons on the GUI to load more data, search for movies, or view details about a selected item.
3. To exit the application, click the "Quit" button or close the window.

## Files

The following files are included in this repository:

- `api.py`: Defines the `StarWarsAPI` class, which is used to access data from the Star Wars API.
- `details.py`: Defines the `Details` class, which is used to display detailed information about a selected item in the GUI.
- `fileio.py`: Defines functions for reading and writing data to a local file.
- `gui.py`: Defines the `StarWarsAPIApp` class, which is used to create the GUI and handle user interactions.
- `main.py`: The main file that launches the application.
- `search.py`: Defines the `MovieSearch` class, which is used to search for movies based on a query string.

## Credits

This application was created by [your name] and is based on the [Star Wars API](https://swapi.dev/).
