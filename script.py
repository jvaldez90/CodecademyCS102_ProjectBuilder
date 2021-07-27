from books import books
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
    search_titles(books)
  elif search == category[1]:
    # display books.py by AUTHOR
    search_authors(books)
  elif search == category[2]:
    # display booky.py by GENRE
    search_genres(books)
  elif search == category[3]:    
    # display booky.py by year
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
  print()
  for book in books:
    print("=> \'"+ books[book]["title"] + "\' by " + books[book]["author"] + "\n\tCall Number: " + books[book]["call_number"])

def search_authors(books):
  print()
  for book in books:
    print("=> "+ books[book]["author"] + " \n\t\'" + books[book]["title"]+ "\'" + "\n\tCall Number: " + books[book]["call_number"])

def search_genres(books):
  print()
  for book in books:
    print("=> " + books[book]["genre"] + ": \n\t\'" + books[book]["title"] + "\' by " + books[book]["author"] + "\n\tCall Number: " + books[book]["call_number"])

def search_year(books):
  print()
  for book in books:
    print("=> " + str(books[book]["year"]) + ": \n\t\'" + books[book]["title"] + "\' by " + books[book]["author"] + "\n\tCall Number: " + books[book]["call_number"])

# MAIN PROGRAM
greet()
book_search()
