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
    s = "mul(11,8)"

    p = parse("mul({a},{b})", s)

    print(p["a"])
    print(p["b"])


##############################################################################

if __name__ == "__main__":
    main()
