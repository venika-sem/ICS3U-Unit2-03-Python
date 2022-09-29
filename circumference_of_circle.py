#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Sep 2022
# This program calculates the circumference of circle using tau

import constants


def main():
    # this function calculates the circumference of circle using tau

    # input
    radius_of_circle = int(input("Enter the radius of circle (mm): "))

    # process
    circumference_of_circle = constants.TAU * radius_of_circle

    # output
    print("")
    print("The circumference of the circle is {0} mm².".format(circumference_of_circle))

    print("\nDone.")


if __name__ == "__main__":
    main()
