#!/usr/bin/env python3

import argparse
import re
from queue import Queue

# CLI
parser = argparse.ArgumentParser()
parser.add_argument("in", action="store")
args = parser.parse_args()

parse_kb(f):
    return ()

class Solver:
    def __init__(self, knowlege_base):
        self.kb = knowlege_base






def main():
    with f as open(args.in, "r"):

        knowlege_base = parse_kb(f)

        theorum = Solver(knowlege_base)
        theorum.solve()

if __name__ == "__main__":
    main()
