import webbrowser

#Using parent class Video to have reusable variables for multiple child classes 
class Video():
    def __init__(self, title, poster_image_url):
        self.title = title
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    def __init__(self, title, poster_image_url, trailer_youtube, release_date):
        Video.__init__(self, title, poster_image_url)
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date



