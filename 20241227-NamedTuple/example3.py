#!/usr/bin/env python3

"""
reprezentáljuk a Start és End pontokat

  0123456789          A) verzió            B) verzió
0 ##########
1 #.......E#               j                    x
2 #.##.#####            +------>             +------>
3 #..#.....#            |                    |
4 ##.#####.#          i |                  y |
5 #S.......#            |                    |
6 ##########            v                    v

                      S: (5, 1)             S: (1, 5)
"""

from typing import NamedTuple


class Point(NamedTuple):
    row: int
    col: int


def main():
    start = Point(col=1, row=5)
    print(start)


##############################################################################

if __name__ == "__main__":
    main()
