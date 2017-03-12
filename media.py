# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():

    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_director, movie_release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.director = movie_director
        self.release_date = movie_release_date

    #Open a browser and play the trailer
    def play_trailer(self):
        webbrowser.open(self.trailer)

