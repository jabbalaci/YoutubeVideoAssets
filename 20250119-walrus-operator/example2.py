#!/usr/bin/env python3


def main():
    d = {
        "zero": 0,
        "one": 1,
        "two": 2,
    }

    if (value := d.get("zero")) != None:
        print(value)


##############################################################################

if __name__ == "__main__":
    main()
