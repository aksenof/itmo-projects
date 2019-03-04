#!/usr/bin/env

# Autor: Andrey Aksenov
# Contacts: 
# E-mail: aksenov.andrey95@yandex.ru
# Tel: +7(920)460-40-10

# how to install api imdb: pip install imdbpy

from imdb import IMDb
from operator import itemgetter


class Top_Genres(object):
	def __init__(self, n_top):
		self.ia = IMDb()  # load class IMDb to <self.ia>
		self.n_top = n_top  # filter: how many films you want from top250
		self.top250 = [i.movieID for i in self.ia.get_top250_movies()]  # list of ID's of top250
		self.all_genres = []  # list of all genres from all films

	def genres_of_movie(self, id, number):
		movie = self.ia.get_movie(id)
		print(number, movie, movie['genres'])
		list_of_genres = [genre for genre in movie['genres']]
		return list_of_genres

	def processing(self):
		for i in range(self.n_top):
			for j in self.genres_of_movie(self.top250[i], i+1):
				self.all_genres.append(j)
		return self.all_genres

	def rating_of_genres(self):
		rating = [[genre, self.all_genres.count(genre)] for genre in set(self.all_genres)]
		rating.sort(key=itemgetter(1), reverse=True)  # sorted list of top genres
		return rating


if __name__ == "__main__":
	print('start')
	n = int(input("Enter number of films from top250 IMDb: "))
	top_genres = Top_Genres(n)
	top_genres.processing()
	print('rating:')
	for i in top_genres.rating_of_genres():
		print(top_genres.rating_of_genres().index(i)+1, i)
	print('end')
