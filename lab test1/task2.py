def recommend_books(books, preferred_genre):
    return [book['title'] for book in books if book['genre'] == preferred_genre]
your_books_list = [
    {'title': 'Dune', 'genre': 'Science Fiction'},
    {'title': 'Pride and Prejudice', 'genre': 'Romance'},
    {'title': 'Neuromancer', 'genre': 'Science Fiction'}
]
user_preferred_genre = 'Science Fiction'
recommended = recommend_books(your_books_list, user_preferred_genre)
print("Recommended:", recommended)