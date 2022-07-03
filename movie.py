import os
import logging
import json


CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
 
  with open(DATA_FILE, "r") as f:
      movies_title = json.load(f)
  movies = [Movie(movie_title) for movie_title in movies_title]
  return movies

class Movie:
  def __init__(self, title):
      self.title = title.title()
  
  def __str__(self):
    return self.title

  def _get_movies(self):
    with open(DATA_FILE, "r") as f:
      return json.load(f)
  
  def _write_movies(self, movies):
    with open(DATA_FILE, "w") as f:
      json.dump(movies, f, indent=4)

  def add_to_movies(self):
    #Récupérer la liste des films
    movies = self._get_movies()
    #Vérifier si le film est dans la liste 
    if self.title not in movies:
      movies.append(self.title)
      self._write_movies(movies)
      return True
    else:
      logging.warning("Le film {self.title} est déja enregistré.")
      return False

  def remove_from_movies(self):
    #Récupérer la liste des films
    movies = self._get_movies()

    #Vérifier si le film est dans la liste 
    if self.title in movies:
      movies.remove(self.title)
      self._write_movies(movies)

    #Si c'est le cas, enlever le film dela liste et écrire la nouvelle
    # liste de films dnas le fichier json.

if __name__ == "__main__":
  movies = get_movies()
