from media import Movie
from fresh_tomatoes import open_movies_page

# Made a design decision to store the movie data in the form of a dictionary with the thought that this could easily
# be replaced by data coming in the form of key value pairs from a database
movie_database = [{"Name"           : "Shawshank Redemption", 
                   "Story Line"     : "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.", 
                   "Poster"         : "https://fanart.tv/api/download.php?type=download&image=49018&section=3",
                   "Youtube Trailer": "https://www.youtube.com/watch?v=6hB3S9bIaco"},
                  
                  {"Name"           : "The Dark Knight",
                   "Story Line"     : "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice",
                   "Poster"         : "http://paulmmartinblog.files.wordpress.com/2011/07/the_dark_knight_poster.jpg",
                   "Youtube Trailer": "https://www.youtube.com/watch?v=yrJL5JxEYIw"},
                  
                  {"Name"           : "The Chef",
                   "Story Line"     : "A chef who loses his restaurant job starts up a food truck in an effort to reclaim his creative promise, while piecing back together his estranged family.",
                   "Poster"         : "http://cdn.cstatic.net/images/gridfs/533ed329f92ea10f1601b243/CHEF_OS%20.jpg",
                   "Youtube Trailer": "https://www.youtube.com/watch?v=UeF16MCDJtM"}
                  ]


def create_database():
    '''
        Returns a list of movie objects for the data that is in the movie database
    '''
    movie_objects = []
    for movie in movie_database:
        
        # Displaying the movie on the web page only if it has a name and a poster
        if movie.get("Name", None) and movie.get("Poster", None):
            movie_objects.append(Movie(movie_title = movie.get("Name","NA"),
                                movie_storyline = movie.get("Story Line","NA"), 
                                poster_image =  movie.get("Poster","NA"), 
                                trailer_youtube = movie.get("Youtube Trailer","NA")))
    
    return movie_objects

def renderWebPage(movies):
    '''
        Calls the fresh_tomatoes module to create and open the movie catalog web page
    '''
    open_movies_page(movies)

def main():
    movies = create_database()
    open_movies_page(movies)

if __name__ == "__main__":
    main()

