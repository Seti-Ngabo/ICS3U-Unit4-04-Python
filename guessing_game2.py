#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program uses a while loop
#   with user input

import random


def main():
    # this function uses a while loop
    the_number = random.randint(0, 10)

    # input
    while True:
        random_guess_as_string = input(
            "Enter a random number between 0 and 10(integer): "
        )
        print("")

        try:
            random_guess_as_integer = int(random_guess_as_string)
            if random_guess_as_integer == the_number:
                print("Correct, you are good at guessing.")
                print("Done.")
                break
            elif random_guess_as_integer > the_number:
                print("The number is too high, try again.")
            else:
                print("The number is too low, try again.")

        except Exception:
            print("{0} is an invalid input, try again.".format(random_guess_as_string))

        print("\nDone.")


if __name__ == "__main__":
    main()
