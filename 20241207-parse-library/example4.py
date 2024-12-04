#!/usr/bin/env python3

"""
parse-olás

cél: formázott sztringből adatok kinyerése
ez a sztring interpoláció fordítottjaként is felfogható

reguláris kifejezések használata
"""

import re


def main():
    s = "Frank Herbert: Dűne (412 oldal)"

    m = re.search(r"(.*): (.*) \((\d+) oldal\)", s)
    if m:
        print(m.group(1))
        print(m.group(2))
        print(m.group(3))


##############################################################################

if __name__ == "__main__":
    main()
