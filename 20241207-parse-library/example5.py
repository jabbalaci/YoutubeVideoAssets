#!/usr/bin/env python3

"""
parse-olás

cél: formázott sztringből adatok kinyerése
ez a sztring interpoláció fordítottjaként is felfogható

parse modul használata
NEM része az stdlib-nek! Külön kell feltelepíteni! (pip install parse)
"""

from parse import parse


def main():
    s = "Frank Herbert: Dűne (412 oldal)"

    p = parse("{author}: {title} ({pages} oldal)", s)
    if p:
        print(p["author"])
        print(p["title"])
        print(p["pages"])


##############################################################################

if __name__ == "__main__":
    main()
