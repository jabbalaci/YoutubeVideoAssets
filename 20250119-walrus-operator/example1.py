#!/usr/bin/env python3


def main():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = [sq for n in li if (sq := n**2) % 2 == 0]
    print(result)


##############################################################################

if __name__ == "__main__":
    main()
