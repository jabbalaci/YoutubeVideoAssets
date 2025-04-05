#!/usr/bin/env python3

import readline


def print_commands():
    print("commands: q, help, run")
    print("shortcuts: Ctrl+h (help), Ctrl+r (run)")


def run():
    print("run was called...")


def main():
    print("readline demo")
    print_commands()

    readline.parse_and_bind('"\\C-h": "help\\n"')  # Ctrl+h => insert "help" + Enter
    readline.parse_and_bind('"\\C-r": "run\\n"')  # Ctrl+r => insert "run" + Enter

    while True:
        try:
            inp = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break
        if inp == "":
            continue
        elif inp == "q":
            break
        elif inp == "help":
            print_commands()
        elif inp == "run":
            run()
        else:
            print("unknown command")


##############################################################################

if __name__ == "__main__":
    main()
