# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

star_wars_force_awakens = media.Movie('The Force Awakens',
                                      'Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.',
                                      'images/star_wars.jpg',
                                      'https://www.youtube.com/watch?v=sGbxmsDFVnE',
                                      'J.J. Abrams',
                                      'December 18, 2015')
deadpool = media.Movie('Deadpool',
                       'A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.',
                       'images/deadpool.jpg',
                       'https://www.youtube.com/watch?v=ONHBaC-pfsk',
                       'Tim Miller',
                       'February 12, 2016')
raiders_of_the_lost_ark = media.Movie('Raiders of the Lost Ark',
                                      'Archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before the Nazis.',
                                      'images/raiders.jpg',
                                      'https://www.youtube.com/watch?v=4uABsht2bgY',
                                      'Steven Spielberg',
                                      'June 12, 1981')
guardians_of_the_galaxy = media.Movie('Guardians of the Galaxy',
                                      'A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.',
                                      'images/guardians.jpg',
                                      'https://www.youtube.com/watch?v=d96cjJhvlMA',
                                      'James Gunn',
                                      'August 1, 2014')
matrix = media.Movie('The Matrix',
                     'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
                     'images/matrix.jpg',
                     'https://www.youtube.com/watch?v=vKQi3bBA1y8',
                     'The Wachowski Brothers',
                     'April 8, 1999')
memento = media.Movie('Memento',
                      "A man juggles searching for his wife's murderer and keeping his short-term memory loss from being an obstacle.",
                      'images/memento.jpg',
                      'https://www.youtube.com/watch?v=nHozKtsvag0',
                      'Christopher Nolan',
                      'March 16, 2001')

movies = [star_wars_force_awakens, deadpool, raiders_of_the_lost_ark, guardians_of_the_galaxy, matrix, memento]

fresh_tomatoes.open_movies_page(movies)
