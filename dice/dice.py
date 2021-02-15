#!/usr/bin/env python

"""
Functions of dice rolling code.
"""

import numpy as np

def roll(arg):
    """
    returns dice roll of one or two dice
    """

    #print results of dice roll
    if arg == "one":
        print(np.random.randint(1,6))

    elif arg == "two":
        print(np.random.randint(1,6),np.random.randint(1,6))

    elif arg == "unfair":
        values = [1, 2, 3, 4, 5, 6]
        probs = [0.1, 0.1, 0.1, 0.1, 0.2, 0.4]
        sample = np.random.choice(values, p = probs)
        print (sample)

    elif arg == "unfairpair":
        values = [1, 2, 3, 4, 5, 6]
        probs = [0.1, 0.1, 0.1, 0.1, 0.2, 0.4]
        sample = np.random.choice(values, p = probs)
        sample2 = np.random.choice(values, p = probs)
        print (sample, sample2)


if __name__ == "__main__":
    roll("one")
    roll("two")
    roll("unfair")
    roll("unfairpair")