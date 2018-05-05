#import media file with the Movie class used to create instances
import fresh_tomatoes
import media

#creating multiple instances of the Movie class
toy_story = media.Movie("Toy Story",
                        "img/toyStory.png",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1995")
last_of_the_mohicans = media.Movie("Last of the Mohicans",
                                   "img/lastOfTheMohicans.png",
                                   "https://www.youtube.com/watch?v=dn7UHJLcPp4",
                                   "1992")
cast_away = media.Movie("Cast Away",
                        "img/castAway.png",
                        "https://www.youtube.com/watch?v=PJvosb4UCLs",
                        "2000")
princess_mononoke = media.Movie("Princess Mononoke",
                                "img/princessMononoke.png",
                                "https://www.youtube.com/watch?v=4OiMOHRDs14",
                                "1997")
midnight_in_paris = media.Movie("Midnight in Paris",
                                "img/midnightInParis.png",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY",
                                "2011")
the_martian = media.Movie("The Martian",
                          "img/theMartian.png",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8",
                          "2015")
aladdin = media.Movie("Aladdin",
                      "img/aladdin.png",
                      "https://www.youtube.com/watch?v=QapaqcDucmg",
                      "1992")
hot_fuzz = media.Movie("Hot Fuzz",
                       "img/hotFuzz.png",
                       "https://www.youtube.com/watch?v=ayTnvVpj9t4",
                       "2007")
pans_labyrinth = media.Movie("Pan's Labyrinth",
                             "img/pansLabyrinth.png",
                             "https://www.youtube.com/watch?v=EXe5a9pBNzg",
                             "2006")
amelie = media.Movie("Amelie",
                     "img/amelie.png",
                     "https://www.youtube.com/watch?v=HUECWi5pX7o",
                     "2001")
drive = media.Movie("Drive",
                    "img/drive.png",
                    "https://www.youtube.com/watch?v=_aybUZFvlto",
                    "2011")


#grouping all the movie instances together into a list
movies = [toy_story, last_of_the_mohicans, cast_away, princess_mononoke, midnight_in_paris, the_martian, aladdin, hot_fuzz, pans_labyrinth, amelie, drive]

fresh_tomatoes.open_movies_page(movies)

