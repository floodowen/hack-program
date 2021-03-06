#!/usr/bin/env python

"""
Command line argparse for dice.py
"""

import argparse
from dice import roll


def parse_arguments():
    """
    Parses command line arguments using argparse
    """
    # init the argparse class object
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--one",
        help="print dice roll with one die",
        action="store_true")

    parser.add_argument(
        "--two",
        help="print dice roll with two dice",
        action="store_true")

    parser.add_argument(
        "--unfair",
        help="print dice roll with one unfair die",
        action="store_true")

    parser.add_argument(
        "--unfairpair",
        help="print dice roll with two unfair dice",
        action="store_true")

     #returns arg dict-like object containing user arguments.
    args = parser.parse_args()
    return args

def main():
    "runs the command line program"
    # get command line arguments
    args = parse_arguments()

    if args.one:
        roll("one")
    elif args.two:
        roll("two")
    elif args.unfair:
        roll("unfair")
    elif args.unfairpair:
        roll("unfairpair")

if __name__ == "__main__":
    roll("one")
    roll("two")
    roll("unfair")
    roll("unfairpair")



