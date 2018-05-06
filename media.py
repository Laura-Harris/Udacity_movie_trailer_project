import webbrowser


class Video():
    """Parent class to provide reusable variables for multiple child classes

    Attributes:
        - title(str):               The video title
        - poster_image_url(str):    URL to image of movie poster
    """
    def __init__(self, title, poster_image_url):
        self.title = title
        self.poster_image_url = poster_image_url

    """Reusable method to support showing of videos in child classes"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
    """Child class that stores info about movies.
    Inherits variables from its parent class Video

    Attributes:
        - trailer_youtube_url(str): URL for the trailer on YouTube
        - release_date(str):        The year each movie was released
    """
    def __init__(self, title, poster_image_url, trailer_youtube, release_date):
        Video.__init__(self, title, poster_image_url)
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
