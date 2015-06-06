class Movie():
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, actors):
        """ """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.starring_str = self.starring(actors)

    def starring(self, actors, ret_str=""):
        """ Takes in a list of actors [foo, bar, foobar] and recursively concatenates them
            to return a string in the form 'Starring foo, bar, and foobar.' There's no
            scientific need for this method to be recursive, other than to learn and try recursion.
        """

        # pops the first actor each time so that the string is constructed with the same order as the list of actors passed in.
        actor = actors.pop(0)
        if not actor:
            # if actor is None here it means no valid list of actors was passed in originally, just return an empty str
            return ""
        if not actors:
            # the stack is now empty, only one actor left to add to the string
            # this path exits the recursive function
            return "Starring " + ret_str + "and %s." % actor
        else:
            # adds the actor and recurses the function call
            # 'actors' can be passed in here directly since it was already trimmed earlier by pop()
            ret_str += "%s, " % actor
            return self.starring(actors, ret_str)