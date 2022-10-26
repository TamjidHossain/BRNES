#!/bin/bash


# G: Grid Height and Width (N x N), N: number of agents, O: number of obstacles, E: Total Episode,
# L: number of times the code will run as a loop, Nw: Neighbor weights [0,1], Ap: Attack Percentage [0,100],
# D: Display environment [on, off], S: Sleep (sec), M: Play mode [random, static]

# Format python RandomInit.py G N O E L Nw Ap D S M
python RandomInit.py 5 5 1 1000 2 0.90 30 on 2 random  

# Format python BRNES.py G N O E L Nw Ap D S M
python BRNES.py 5 5 1 1000 2 0.90 30 on 2 random
