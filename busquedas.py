import sys, os
sys.setrecursionlimit(100000)

from rana_puzzle import rana_puzzle

if __name__ == "__main__":
    puzzle = rana_puzzle("abcvxyz")
    #puzzle = ocho_puzzle("87653H241")
    puzzle.algoritmo_anchura()
    #puzzle.algoritmo_profundidad()
    #puzzle.algoritmo_primero_mejor()
    #puzzle.algoritmo_hill_climbing()
    #puzzle.algoritmo_beam()