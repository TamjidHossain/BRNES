#!/usr/bin/env python
# coding: utf-8

# import essential modules
import numpy as np
import pickle

noTarget = 1
tPosList = []

gridWidthList = [10]
gridHeightList = [10]
noAgentList = [10]
noObsList = [2]
eList = [1000]
LoopVal = 1
neighborWeightsList = [0.90]
playModeList = ['random'] 

aPosList = []
aPosListTotal = []
aPosListLoopTotal = []
aPosListCriteriaTotal = []
for t in range(noTarget):
    tPosList.append([(int(gridHeightList[0]/(t+1))-1), (int(gridWidthList[0]/(t+1))-1)])

for CriteriaVal in range(len(gridWidthList)):
    height = gridWidthList[CriteriaVal]
    width = gridHeightList[CriteriaVal]
    Agent = noAgentList[CriteriaVal]
    Obs = noObsList[CriteriaVal]
    epoch = eList[CriteriaVal]
    neighborWeights = neighborWeightsList[CriteriaVal]

    
    for Loop in range(LoopVal):
        sX =[i for i in range(height-1)]
        sY =[i for i in range(width-1)]
        for ep in range(0,epoch):
            for a in range(Agent):
                aPosX = np.random.choice(sX)
                aPosY = np.random.choice(sY)
                if [aPosX, aPosY] not in tPosList:
                    aPosX= aPosX
                    aPosY= aPosY
                else:
                    aPosX = np.random.choice(sX)
                    aPosY = np.random.choice(sY)
                aPosList.append([aPosX, aPosY])
            aPosListTotal.append(aPosList)
            aPosList =[]
#             print(ep, aPosListTotal,"\n")
        aPosListLoopTotal.append(aPosListTotal)
        aPosListTotal=[]
        
    p = aPosListLoopTotal
    with open("./fileOut/Last/positions"+str(CriteriaVal)+"_BRNETp_G10_10", "wb") as Pp:   #Pickling
        pickle.dump(p, Pp)
        
print("################# Random Initialization Done #########################")







