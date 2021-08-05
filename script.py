from library_books import books
from sort_books import *

def greet():
  print("""
  **************************

    WELCOME TO THE LIBRARY 
    BOOK SEARCH CATALOGUE
    
  ***************************
  """)
def goodbye():
  print("""
  *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    THANK YOU FOR USING THE LIBRARY 
        BOOK SEARCH CATALOGUE    
  *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
  """)

def book_search():
  category = ["title", "author", "genre","year"]
  print("How would you like to begin your book search?")
  search = input("Search by: title, author, genre, year\n")
  search = search.lower()
  for item in category:
    if search == item:
      print("Searching by " + search + " … ")
    if search not in category:
      print("Invalid input")
      print("Let's try this again")
      break

  if search == category[0]:
    # display books.py  by TITLE
    print("Here are library books in our collection by "+ search)
    search_titles(books)
  elif search == category[1]:
    # display books.py by AUTHOR
    print("Here are library books in our collection by "+ search)
    search_authors(books)
  elif search == category[2]:
    # display booky.py by GENRE
    print("Here are library books in our collection by "+ search)
    search_genres(books)
  elif search == category[3]:    
    # display booky.py by year
    print("Here are library books in our collection by "+ search)
    search_year(books)

  keep_going = input("\nDo you still want to continue? (y/n) ")
  if keep_going == "y":
    print()
    book_search()
  else:
    if keep_going != "n":
      print("\nInvalid Response.\nAssuming you do not wish to continue.")
    goodbye()
# END OF book_search():

def search_titles(books):
  sort_by_titles()

def search_authors(books):
  sort_by_authors()

def search_genres(books):
  sort_by_genre()
  
def search_year(books):  
  sort_by_year()

# MAIN PROGRAM
greet()
book_search()
