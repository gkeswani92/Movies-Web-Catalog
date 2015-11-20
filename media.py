import webbrowser

class Movie(object):
    '''
        This class provides a way to store information about movies
    '''
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        '''
            Opens an instance of a web browser if it is not already open or a tab
            if the web browser is open and plays the youtube trailer
        '''
        webbrowser.open(self.trailer_youtube_url)
    
    