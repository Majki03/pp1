from ebook import Ebook

my_ebook = Ebook("Wiedźmin", "Andzrej Sapkowski", 332)

my_ebook.open_book()

my_ebook.status()

for _ in range(5):
    my_ebook.next()

my_ebook.status()

my_ebook.close_book()