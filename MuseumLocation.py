# museum_location.py

class MuseumLocation:
    def __init__(self, location_id, name, description):
        """
        Initializes a new MuseumLocation instance.
        
        :param location_id: A unique identifier for the location.
        :param name: The name of the location.
        :param description: A brief description of the location.
        """
        self.location_id = location_id
        self.name = name
        self.description = description
        self.artworks = []  # List to store artworks displayed at this location
        self.exhibitions = []  # List to store exhibitions held at this location

    def add_artwork(self, artwork):
        """
        Adds an artwork to the location.

        :param artwork: The artwork to be added.
        """
        self.artworks.append(artwork)
        artwork.location = self  # Set the location attribute of the artwork

    def add_exhibition(self, exhibition):
        """
        Adds an exhibition to the location.

        :param exhibition: The exhibition to be added.
        """
        self.exhibitions.append(exhibition)
        exhibition.location = self  # Set the location attribute of the exhibition

    def __str__(self):
        return f"Location: {self.name}, Description: {self.description}"
