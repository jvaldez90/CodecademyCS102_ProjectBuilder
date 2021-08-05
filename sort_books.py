from library_books import books
from collections import OrderedDict
from operator import getitem

# LOCAL VARIABLES
by_titles = {}
by_authors = {}
by_genre = {}
by_year = {}

def sort_by_titles():
  by_titles = OrderedDict(sorted(books.items(), key = lambda x: getitem(x[1], "title")))
  for book in by_titles:
    print("\n---------------------------------------------\n")
    print("Title: \'"+ by_titles[book]["title"] + "\'\n\tAuthor: " + by_titles[book]["author"] + "\n\tYear: " + str(by_titles[book]["year"]) + "\n\tGenre: " + str(by_titles[book]["genre"]) + "\n\tCall Number: " + by_titles[book]["call_number"])
  

def sort_by_authors():
  by_authors = OrderedDict(sorted(books.items(), key = lambda x: getitem(x[1], "author")))
  for book in by_authors:
    print("\n---------------------------------------------\n")
    print("Author: "+ by_authors[book]["author"] + " \n\tTitle: \'" + by_authors[book]["title"]+ "\'\n\tYear: " + str(by_authors[book]["year"]) + "\n\tGenre: " + str(by_authors[book]["genre"]) + "\n\tCall Number: " + by_authors[book]["call_number"])
  

def sort_by_genre():
  by_genre = OrderedDict(sorted(books.items(), key = lambda x: getitem(x[1], "genre")))
  for book in by_genre:
    print("\n---------------------------------------------\n")
    print("Genre: " + str(by_genre[book]["genre"]) + "\n\tTitle: \'" + by_genre[book]["title"] + "\'\n\tAuthor: " + by_genre[book]["author"] + "\n\tYear: " + str(by_genre[book]["year"]) + "\n\tCall Number: " + by_genre[book]["call_number"])
  

def sort_by_year():
  by_year = OrderedDict(sorted(books.items(), key = lambda x: getitem(x[1], "year")))
  for book in by_year:   
    print("\n---------------------------------------------\n")
    print("Year: " + str(by_year[book]["year"]) + "\n\tTitle: \'" + by_year[book]["title"] + "\'\n\tAuthor: " + by_year[book]["author"] + "\n\tGenre: "+ str(by_year[book]["genre"]) + "\n\tCall Number: " + by_year[book]["call_number"])
  
