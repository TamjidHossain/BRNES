# BRNES: Byzantine Robust Neighbor Experience Sharing in Differentially Private Multiagent Reinforcement Learning
** [submitted to AAMAS 2023] **

This is the codification used in the AAMAS 2023 paper proposing BRNES framework as means of accelerating learning in Multiagent Systems composed of advisee and advisor agents. You are free to use all or part of the codes here presented for any purpose, provided that the paper is properly cited and the original authors properly credited. All the files here shared come with no warranties.

Paper bib entry:

@inproceedings{Hossain2023,<br />
author = {Hossain, Md Tamjid and<br />
Hung La and<br />
Shahriar Badsha},<br />
title = {{Byzantine Robust Neighbor Experience Sharing in Differentially Private Multiagent Reinforcement Learning}},<br />
booktitle = {Proceedings of the 22nd International Conference on Autonomous Agents and Multiagent Systems (AAMAS)},<br />
year = {2023},<br />
note = {Under review}<br />
}

This project was built on Python 3.8. All the experiements are executed in the Predetor-Prey (PP) domain (https://www.ifaamas.org/Proceedings/aamas2017/pdfs/p1722.pdf), we included the version we used in the **PP_environment** folder (slightly different from the standard PP domain). For the graph generation code you will need to install Jupyter Notebook (http://jupyter.readthedocs.io/en/latest/install.html).

## Files
The folder **Main** contains our implementation of all algorithm and experiements

The folder **Main/PP_environment** contains the Predetor-Prey environment (also called as a Pursuit domain) we used for experiements

Finally, the folder **ProcessedFiles** contains already processed .pickle files for graph printing and data visulaization

## How to use <br />
First install python 3.8 from https://www.python.org/downloads/release/python-380/ <br />
Then open up your command terminal/prompt to run the follwoing commands sequentially
1. python RandomInit.py G N O E L Nw Ap D S M   <br />
2. python BRNES.py G N O E L Nw Ap D S M   <br />

where, <br />
G: Grid Height and Width (N x N)<br />
N: number of agents <br />
O: number of obstacles <br />
E: Total Episode <br />
L: number of times the code will run as a loop <br />
Nw: Neighbor weights [0,1] <br />
Ap: Attack Percentage [0,100] <br />
D: Display environment [on, off] <br />
S: Sleep (sec) <br />
M: Play mode [random, static]<br /><br />

Example: <br />
python RandomInit.py 15 10 3 2000 10 0.90 20 on 2 random  <br />
python BRNES.py 15 10 3 2000 10 0.90 20 on 2 random  <br />
python DARL.py 15 10 3 2000 10 0.90 20 on 2 random  <br />
python AdhocTD.py 15 10 3 2000 10 0.90 20 on 2 random  <br />

         
However, it will take a very long time until the experiments are completed. It may be of interest running more than one algorithm at the same time if you have enough computing power. Also, note that, for each framework, if the agents do not attain goal within (GridSize*100) steps in a particular episode, the episode and environment will be reset to the next.

The file name associated with any experiment is appended into a log file (BRNES.txt) that resides inside "Main/OutputFile" directory.<br />
The results (Steps to goal (SG), Time to goal (TG), Rewards, Convergence, Qtable) of any experiment are stored categorically by file name in "Main/SG", "Main/TG", "Main/Reward", "Main/Convergence", "Main/Qtable" respectively as a pickle file. Then, the respective pickle files can be used to reproduce the graphs.


## Contact
For questions about the codification or paper, please send an email to the first author.
