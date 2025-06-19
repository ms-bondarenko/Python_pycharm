from book import Book

library=[
    Book("Мастер и Маргарита" , "М.Булгаков"),
    Book("War of Worlds", "Herbert Wells"),
    Book("Двенадцать", "Блок")
]
for book in library:
    print(f"{book.name} - {book.autor}")