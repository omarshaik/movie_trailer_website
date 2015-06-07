import media
import fresh_tomatoes

# create each Movie instance with information to set the instance variables
the_lion_king = media.Movie(title="The Lion King",
                        storyline="Some lion dude dies so another becomes king.",
                        poster_image_url="http://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        trailer_youtube_url="https://www.youtube.com/watch?v=MPugv1k7r-s",
                        actors=["Matthew Broderick", "James Earl Jones", "Jeremy Irons", "Jonathan Taylor Thomas"])

the_bourne_identity = media.Movie(title="The Bourne Identity",
                        storyline="Some dude forgets his identity.",
                        poster_image_url="http://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                        trailer_youtube_url="https://www.youtube.com/watch?v=2tqK_3mKQUw",
                        actors=["Matt Damon", "Franka Potente", "Chris Cooper", "Clive Owen"])

space_jam = media.Movie(title="Space Jam",
                        storyline="Some dude beats aliens at basketball.",
                        poster_image_url="http://upload.wikimedia.org/wikipedia/en/1/14/Space_jam.jpg",
                        trailer_youtube_url="https://www.youtube.com/watch?v=oKNy-MWjkcU",
                        actors=["Michael Jordan", "Wayne Knight", "Theresa Randle", "Danny DeVito"])

the_dark_knight_rises = media.Movie(title="The Dark Knight Rises",
                        storyline="Some dude lives in a batcave and fights crime in the dark night.",
                        poster_image_url="http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                        trailer_youtube_url="https://www.youtube.com/watch?v=GokKUqLcvD8",
                        actors=["Christian Bale", "Michael Caine", "Gary Oldman", "Anne Hathaway"])

# add the movie instances to the list
movies = [the_lion_king, the_bourne_identity, space_jam, the_dark_knight_rises]
# call open_movies_page with the list of movies
fresh_tomatoes.open_movies_page(movies)
