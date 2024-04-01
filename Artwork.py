# Assuming the existing Artwork class is defined, we add a location attribute to its __init__ method.

class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location=None):
        # Existing attributes
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        # New location attribute
        self.location = location  # This should be an instance of MuseumLocation or None

    # Other methods remain unchanged
