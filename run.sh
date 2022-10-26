#!/bin/bash


# G: Grid Height and Width (N x N), N: number of agents, O: number of obstacles, E: Total Episode,
# L: number of times the code will run as a loop, Nw: Neighbor weights [0,1]

python RandomInit.py G N O E L Nw   # Example python RandomInit.py 5 5 1 1000 2 0.90
