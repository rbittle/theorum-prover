#!/usr/bin/env python3

import argparse
import re
from queue import Queue

# CLI
parser = argparse.ArgumentParser()
parser.add_argument("input", action="store")
args = parser.parse_args()



def parse_kb(f):
    kb = []
    for line in f.readlines():
        clause = []
        # clean up newlines
        line = line.strip()

        # split by whitespace
        var_array = line.split(" ")
        for var in var_array:
            if var.find("~") == 0:
                # negated values
                var_name = var[1:]
                clause.append((var_name, False))
            else:
                # positive values
                clause.append((var, True))
        kb.append(clause)

    return tuple(kb)

    def unifiable(c1, c2):
        return False

    def unify(c1, c2):
        return []

class Solver:
    def __init__(self, knowlege_base):
        self.kb = knowlege_base

    def solve(self):
        print(self.kb)

        kb = self.kb

        while True: 
            # try to unify clauses in the kb
            for clause1 in kb:
                for clause2 in kb:
                    if unifiable(clause1, clause2):
                        result = unify(clause1, clause2)
                        if result != []:
                            kb.append(result)
                        else:
                            break



def main():
    with open(args.input, "r") as f:

        knowlege_base = parse_kb(f)

        theorum = Solver(knowlege_base)
        theorum.solve()

if __name__ == "__main__":
    main()
