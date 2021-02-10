#!/usr/bin/env python

"""
Functions of dice rolling code.
"""

import random

def roll(arg):
    """
    returns dice roll of one or two dice
    """

    #print results of dice roll
    if arg == "one":
        print(random.randint(1,6))

    elif arg == "two":
        print(random.randint(1,6),random.randint(1,6))
       


if __name__ == "__main__":
    roll("one")
    roll("two")