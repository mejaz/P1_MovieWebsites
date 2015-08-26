#class for movies.
class Movies():
    def __init__(self, title, images, url, lead_actors):
        """ Class with different attributes of a Movie """
        self.title = title
        self.poster_image_url = images
        self.trailer_youtube_url = url
        self.lead_actor = lead_actors
