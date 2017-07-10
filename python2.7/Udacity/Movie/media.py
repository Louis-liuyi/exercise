import webbrowser

class Movie():
    def __init__(self, movie_titile, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_titile
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
