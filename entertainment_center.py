"""import media file with the Movie class used to create instances"""
import fresh_tomatoes
import media

"""creating multiple instances of the Movie class"""
toy_story = media.Movie("Toy Story",
                        "https://bit.ly/2HZA2Yr",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1995")
cast_away = media.Movie("Cast Away",
                        "https://bit.ly/2I10osL",
                        "https://www.youtube.com/watch?v=PJvosb4UCLs",
                        "2000")
princess_mononoke = media.Movie("Princess Mononoke",
                                "https://bit.ly/2rpA6cF",
                                "https://www.youtube.com/watch?v=4OiMOHRDs14",
                                "1997")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "https://bit.ly/2rpw2Jp",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "2011")
the_martian = media.Movie("The Martian",
                          "https://bit.ly/2HSxy1L",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8",
                          "2015")
aladdin = media.Movie("Aladdin",
                      "https://bit.ly/2FPrdOS",
                      "https://www.youtube.com/watch?v=QapaqcDucmg",
                      "1992")
hot_fuzz = media.Movie("Hot Fuzz",
                       "https://bit.ly/2KFsUSF",
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4",
                       "2007")
pans_labyrinth = media.Movie("Pan's Labyrinth",
                             "https://bit.ly/2wnWBom",
                             "https://www.youtube.com/watch?v=EXe5a9pBNzg",
                             "2006")
amelie = media.Movie("Amelie",
                     "https://bit.ly/2KEE22c",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o",
                     "2001")
drive = media.Movie("Drive",
                    "https://bit.ly/2jzRtUz",
                    "https://www.youtube.com/watch?v=_aybUZFvlto",
                    "2011")


"""grouping all the movie instances together into a list"""
movies = [toy_story, cast_away, princess_mononoke, midnight_in_paris,
          the_martian, aladdin, hot_fuzz, pans_labyrinth, amelie, drive]

fresh_tomatoes.open_movies_page(movies)
