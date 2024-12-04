#!/usr/bin/env python3

"""
sztring interpoláció #1
cél: formázott sztring előállítása
"""


def main():
    name = "Géza"
    color = "kék"
    what = "ég"

    # result = f"{name}, {color} az {what}!"
    result = "{0}, {1} az {2}!".format(name, color, what)

    print(result)


##############################################################################

if __name__ == "__main__":
    main()
