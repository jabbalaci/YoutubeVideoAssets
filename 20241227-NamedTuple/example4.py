#!/usr/bin/env python3

"""
      y
      ^
      |
      |
    1 -     o
      |
------+--|--|----------> x
      |  1  2
      |
"""

# Régi szintaxis, NE használjuk!

from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
Point = namedtuple("Point", "x y")


def main():
    p = Point(x=2, y=1)
    print(p)


##############################################################################

if __name__ == "__main__":
    main()
