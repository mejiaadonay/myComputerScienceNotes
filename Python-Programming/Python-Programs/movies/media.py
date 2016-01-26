import webbrowser

# Media for movie website
# Author:   Jose Escobar Mejia
# Date:     01/25/2016

# class definition
class Movie():
    # VALID_RATINGS is all upper-case since it is contant class varible.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
