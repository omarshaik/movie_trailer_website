import media
import fresh_tomatoes

lion_king = media.Movie(title="The Lion King",
                        storyline="Some lion dude dies",
                        poster_image_url="http://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        trailer_youtube_url="https://www.youtube.com/watch?v=MPugv1k7r-s",
                        actors=["Michael Jordan", "LeBron James", "Bugz Bunny", "MonStars"])
print(lion_king.storyline)

movies = [lion_king]

fresh_tomatoes.open_movies_page(movies)

