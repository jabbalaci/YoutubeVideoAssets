#!/usr/bin/env python3

"""
sztring interpoláció #2
cél: formázott sztring előállítása
"""


class Book:
    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.author}: {self.title} ({self.pages} oldal)"


def main():
    book1 = Book("Frank Herbert", "Dűne", 412)
    book2 = Book("Asimov", "Alapítvány", 255)

    print(book1)
    print(book2)


##############################################################################

if __name__ == "__main__":
    main()
