#import media file with the Movie class used to create instances
import fresh_tomatoes
import media

#creating multiple instances of the Movie class
toy_story = media.Movie("Toy Story",
    "https://ia.media-imdb.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SY1000_SX670_AL_.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    "1995")
last_of_the_mohicans = media.Movie("Last of the Mohicans",
    "https://ia.media-imdb.com/images/M/MV5BZDNiYmRkNDYtOWU1NC00NmMxLWFkNmUtMGI5NTJjOTJmYTM5XkEyXkFqcGdeQXVyNzQ1ODk3MTQ@._V1_SY1000_CR0,0,670,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=dn7UHJLcPp4",
    "1992")
cast_away = media.Movie("Cast Away",
    "https://ia.media-imdb.com/images/M/MV5BN2Y5ZTU4YjctMDRmMC00MTg4LWE1M2MtMjk4MzVmOTE4YjkzXkEyXkFqcGdeQXVyNTc1NTQxODI@._V1_.jpg",
    "https://www.youtube.com/watch?v=PJvosb4UCLs",
    "2000")
princess_mononoke = media.Movie("Princess Mononoke",
    "https://ia.media-imdb.com/images/M/MV5BMTVlNWM4NTAtNDQxYi00YWU5LWIwM2MtZmVjYWFmODZiODE5XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,707,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=4OiMOHRDs14",
    "1997")
midnight_in_paris = media.Movie("Midnight in Paris",
    "https://ia.media-imdb.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=FAfR8omt-CY",
    "2011")
the_martian = media.Movie("The Martian",
    "https://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=ej3ioOneTy8",
    "2015")
aladdin = media.Movie("Aladdin",
    "https://ia.media-imdb.com/images/M/MV5BY2Q2NDI1MjUtM2Q5ZS00MTFlLWJiYWEtNTZmNjQ3OGJkZDgxXkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_.jpg",
    "https://www.youtube.com/watch?v=QapaqcDucmg",
    "1992")
hot_fuzz = media.Movie("Hot Fuzz",
    "https://ia.media-imdb.com/images/M/MV5BMzg4MDJhMDMtYmJiMS00ZDZmLThmZWUtYTMwZDM1YTc5MWE2XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY999_CR0,0,672,999_AL_.jpg",
    "https://www.youtube.com/watch?v=ayTnvVpj9t4",
    "2007")
pans_labyrinth = media.Movie("Pan's Labyrinth",
    "https://ia.media-imdb.com/images/M/MV5BMTU3ODg2NjQ5NF5BMl5BanBnXkFtZTcwMDEwODgzMQ@@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=EXe5a9pBNzg",
    "2006")
amelie = media.Movie("Amelie",
    "https://ia.media-imdb.com/images/M/MV5BNDg4NjM1YjMtYmNhZC00MjM0LWFiZmYtNGY1YjA3MzZmODc5XkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=HUECWi5pX7o",
    "2001")
drive = media.Movie("Drive",
    "https://ia.media-imdb.com/images/M/MV5BZjY5ZjQyMjMtMmEwOC00Nzc2LTllYTItMmU2MzJjNTg1NjY0XkEyXkFqcGdeQXVyNjQ1MTMzMDQ@._V1_SY1000_SX675_AL_.jpg",
    "https://www.youtube.com/watch?v=_aybUZFvlto",
    "2011")


#grouping all the movie instances together into a list
movies = [toy_story, last_of_the_mohicans, cast_away, princess_mononoke, midnight_in_paris, the_martian, aladdin, hot_fuzz, pans_labyrinth, amelie, drive]

fresh_tomatoes.open_movies_page(movies)



