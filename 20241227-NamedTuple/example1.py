#!/usr/bin/env python3

# téma: nevesített tuple (NamedTuple)

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

from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def main():
    t = (2, 1)
    print(t[0])
    print("---")
    p = Point(x=2, y=1)
    print(p)


##############################################################################

if __name__ == "__main__":
    main()
