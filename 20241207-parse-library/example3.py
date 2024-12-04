#!/usr/bin/env python3

"""
parse-olás

cél: formázott sztringből adatok kinyerése
ez a sztring interpoláció fordítottjaként is felfogható

egyszerű eset: CSV (comma-separated value)
"""


def main():
    s = "Frank Herbert,Dűne,412"

    parts = s.split(",")
    print(parts)
    author = parts[0]
    title = parts[1]
    pages = parts[2]
    print(author, title, pages)


##############################################################################

if __name__ == "__main__":
    main()
