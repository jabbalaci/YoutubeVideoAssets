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

from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def main():
    # y,x
    # 2,3
    # 5,8
    # ...
    # t = (3, 2)
    p = Point(y=2, x=3)
    print(p)


##############################################################################

if __name__ == "__main__":
    main()
