#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is CCmath software. 
CCmath Website: https://www.ccmath.com/
Erlang Calculator User Manual: https://erlangaddin.ccmath.com/manual/
"""

# Please make sure that demo file is in the same directory with ERLANG.py
# Import ERLANG to call the functions:
import ERLANG  
import math
import numpy as np

# Please make sure you enter User ID correctly: Python-Erlang-betatest
# If you want not no enter UID every time you run the code, add comment to line 29 and uncomment line 30.
# If UID is not correct, you will see -3 as a result of calculations.

# =============================================================================
# ERLANG C:
# =============================================================================

# # Inputs: 
# Forecast = 4
# AHT = 3
# AWT = 0.333

# calc_option=2
# # calc_option defines the type of calculations. (For computational simplicity)
# # Enter 0 for ASA and SL Calculation (1st column of the Excel sheet)
# # Enter 1 for Agents (SL) Calculation (2nd column of the Excel sheet)
# # Enter 2 for Agents (ASA) Calculation (3rd column of the Excel sheet)


# print('------ Erlang C Calculations for Option',calc_option,'------')
# print('INPUTS:')
# print("Forecast:",Forecast)
# print("Average handling time:",AHT)
# print("Average waiting time:",AWT)

# if calc_option==0:
#     # ASA and SL Calculation (1st column):
#     Agents = 14
#     ASA = round(ERLANG.X.ASA(Forecast,AHT,Agents),3)
#     SL = round(ERLANG.X.SLA(Forecast,AHT,Agents,AWT),3)
#     Occupancy = round(Forecast*AHT/Agents,3)
#     print("Number of agents:",Agents)
#     print('OUTPUTS:')
#     print("Average speed of answer:",ASA)
#     print("Service level:",SL)

# elif calc_option==1:
#     # Agents (SL) Calculation (2nd column):
#     SL = 0.8
#     Agents = round(ERLANG.X.AGENTS_SLA(SL, Forecast, AHT, AWT),3)
#     ASA = round(ERLANG.X.ASA(Forecast,AHT,math.ceil(Agents)),3)
#     Occupancy = round(Forecast*AHT/math.ceil(Agents),3)
#     print("Service level:",SL)
#     print('OUTPUTS:')
#     print("Number of agents:",Agents)
#     print("Average speed of answer:",ASA)

# elif calc_option==2:
#     # Agents (ASA) Calculation (3rd column):
#     ASA = 0.333
#     Agents = round(ERLANG.X.AGENTS_ASA(ASA, Forecast, AHT),3)
#     SL = round(ERLANG.X.SLA(Forecast, AHT, math.ceil(Agents), AWT),3)
#     Occupancy = round(Forecast*AHT/math.ceil(Agents),3)
#     print("Average speed of answer:",ASA)
#     print('OUTPUTS:')
#     print("Number of agents:",Agents)
#     print("Service level:",SL)

# print("Occupancy:",Occupancy)




# # Example: How to use arrays of values:
# calc_option=1
# size=5
# print('\n------ Erlang C Calculations for Arrays of Size',size,', Option',calc_option,'------')
# print('INPUTS:')  

# #Inputs:
# # Let us first generate 5 forecast and AHT values randomly.
# # Please note that you can enter the values by yourself.
# Forecast= np.random.randint(3,5,size).tolist()
# print('Forecast:', Forecast)  
# AHT= np.random.randint(3,5,size).tolist()
# print('AHT:', AHT)  
# # Please note that you can enter the values by yourself.
# # I.e. Forecast=[3,4,2,4,3], AHT=[1,2,3,3,4]
# AWT = 0.333
# aht = [1,10,50,80,100,1000000]
# for i in aht:
#     print(i)
#     print(round(ERLANG.X.AGENTS_SLA(0.8, 1, i, 60),3))
#     print("\n")


calc_option=1
import pandas as pd
df = pd.read_csv('erlangTest.csv')

Forecast = df.values[:,1].tolist()
AHT = df.values[:,2].tolist()
AWT = df.values[:,3].tolist()
SL = df.values[:,4].tolist()
size = len(AHT)
calc_option=1


#Outputs:
Occupancy = []
if calc_option==0:
    # ASA and SL Calculation (1st column):
    ASA = []
    SL = []
    Agents = np.random.randint(10,15,size).tolist()
    print('Agents:', Agents)  
    for i in range(size):
        ASA.append(round(ERLANG.X.ASA(Forecast[i], AHT[i], Agents[i]),3))
        SL.append(round(ERLANG.X.SLA(Forecast[i], AHT[i], Agents[i], AWT[i]),3))
        Occupancy.append(round(Forecast[i]*AHT[i]/Agents[i],3))

    df['ASA'] = ASA
    df['SL'] = SL
    df['Occupancy'] = Occupancy
    df.to_csv('erlangTest.csv', index = False)

    
elif calc_option==1:
    # Agents (SL) Calculation (2nd column):
    Agents = []
    ASA = []
    print("Service level:",SL)
    for i in range(size):
        Agents.append(round(ERLANG.X.AGENTS_SLA(SL[i], Forecast[i], AHT[i], AWT[i]),3))
        ASA.append(round(ERLANG.X.ASA(Forecast[i], AHT[i],math.ceil(Agents[i])),3))
        Occupancy.append(round(Forecast[i]*AHT[i]/math.ceil(Agents[i]),3))
    df['Agents'] = Agents
    df['ASA'] = ASA
    df['Occupancy'] = Occupancy
    df.to_csv('erlangTest.csv', index = False)


elif calc_option==2:
    # Agents (ASA) Calculation (3rd column):
    Agents = []
    SL = []
    ASA = 0.333
    print("Average speed of answer:",ASA)
    for i in range(size):
        Agents.append(round(ERLANG.X.AGENTS_ASA(ASA, Forecast[i], AHT[i]),3))
        SL.append(round(ERLANG.X.SLA(Forecast[i], AHT[i], math.ceil(Agents[i]), AWT[i]),3))
        Occupancy.append(round(Forecast[i]*AHT[i]/math.ceil(Agents[i]),3))
    df['Agents'] = Agents
    df['SL'] = SL
    df['Occupancy'] = Occupancy
    df.to_csv('erlangTest.csv', index = False)

# print("Occupancy:",Occupancy)
    
#It is possible to use arrays in Erlang X, Chat, and Blending calculators as well using the same method.



# # =============================================================================
# # ERLANG X:
# # =============================================================================

# # Inputs: 
# Forecast = 4
# AHT = 3
# Patience = 1
# AWT = 0.333
# Lines = 100

# calc_option=0
# # calc_option defines the type of calculations. (For computational simplicity)
# # Enter 0 for ASA and SL Calculation (1st column of the Excel sheet)
# # Enter 1 for Agents (SL) Calculation (2nd column of the Excel sheet)
# # Enter 2 for Agents (ASA) Calculation (3rd column of the Excel sheet)

# print('\n------ Erlang X Calculations for Option',calc_option,'------')
# print('INPUTS:')
# print("Forecast:",Forecast)
# print("Average handling time:",AHT)
# print("Patience:",Patience)
# print("Average waiting time:",AWT)
# print("Lines:",Lines)

# if calc_option==0:
#     # ASA and SL Calculation (1st column):
#     Agents = 14
#     ASA = round(ERLANG.X.ASA(Forecast, AHT, Agents, Lines, Patience, 0),3)
#     SL = round(ERLANG.X.SLA(Forecast, AHT, Agents, AWT, Lines, Patience, 0),3)
#     Abandon = round(ERLANG.X.ABANDON(Forecast, AHT, Agents, Lines, Patience, 0),3)
#     print("Number of agents:",Agents)
#     print('OUTPUTS:')
#     print("Average speed of answer:",ASA)
#     print("Service level:",SL)
#     print("Abandonment:",Abandon)

# elif calc_option==1:
#     # Agents (SL) Calculation (2nd column):
#     SL = 0.8
#     Agents = math.ceil(ERLANG.X.AGENTS_SLA(SL, Forecast, AHT, AWT, Lines, Patience, 0))
#     ASA = round(ERLANG.X.ASA(Forecast, AHT, Agents, Lines, Patience, 0),3)
#     Abandon = round(ERLANG.X.ABANDON(Forecast, AHT, Agents, Lines, Patience, 0),3)
#     print("Service level:",SL)
#     print('OUTPUTS:')
#     print("Number of agents:",Agents)
#     print("Average speed of answer:",ASA)
#     print("Abandonment:",Abandon)

# elif calc_option==2:
#     # Agents (ASA) Calculation (3rd column):
#     Abandon = 0.05
#     Agents = math.ceil(ERLANG.X.AGENTS_ABANDON(Abandon, Forecast, AHT, Lines, AWT, 0))
#     ASA = round(ERLANG.X.ASA(Forecast, AHT, Agents, Lines, Patience, 0),3)
#     SL = round(ERLANG.X.SLA(Forecast, AHT, Agents, AWT, Lines, Patience, 0),3)
#     print("Abandonment:",Abandon)
#     print('OUTPUTS:')
#     print("Number of agents:",Agents)
#     print("Average speed of answer:",ASA)
#     print("Service level:",SL)

# Blocking = round(ERLANG.X.BLOCKING(Forecast, AHT, Agents, Lines, Patience, 0),3)
# Occupancy = round(ERLANG.X.OCCUPANCY(Forecast, AHT, Agents, Lines, Patience, 0),3)
# print("Blocking rate:",Blocking)
# print("Occupancy:",Occupancy)



# # =============================================================================
# # ERLANG BLENDING:
# # =============================================================================

# # No demo sheets available. So, I skip this part.
# """
# print(ERLANG.BL.SLA(3, 4, 15, 0, 2))

# print(ERLANG.BL.ASA(3, 4, 15, 2))

# print(ERLANG.BL.OCCUPANCY(3, 4, 15, 2))

# print(ERLANG.BL.OUTBOUND(3, 4, 15, 2))

# print(ERLANG.BL.THRESHOLD(3, 4, 15, 0.1, 2))

# print(ERLANG.BL.ASA_SLA(3, 4, 25, 0.8, 5))

# print(ERLANG.BL.OCCUPANCY_SLA(1, 4, 25, 0.2, 100))

# print(ERLANG.BL.OUTBOUND_SLA(1, 4, 25, 0.2, 100))
# """

# # =============================================================================
# # ERLANG CHAT:
# # =============================================================================

# # Inputs: 
# Forecast = 4
# AHT = [3,3.5,4]
# Patience = 1
# AWT = 0.333
# Lines = 100

# calc_option=0
# # calc_option defines the type of calculations. (For computational simplicity)
# # Enter 0 for ASA and SL Calculation (1st column of the Excel sheet)
# # Enter 1 for Agents (SL) Calculation (2nd column of the Excel sheet)

# print('\n------ Erlang Chat Calculations for Option',calc_option,'------')
# print('INPUTS:')
# print("Forecast:",Forecast)
# print("Average handling time:",AHT)
# print("Patience:",Patience)
# print("Average waiting time:",AWT)
# print("Lines:",Lines)

# if calc_option==0:
#     # ASA and SL Calculation (1st column):
#     Agents = 5
#     ASA = round(ERLANG.CHAT.ASA(Forecast, AHT, Agents, Lines, Patience),3)
#     SL = round(ERLANG.CHAT.SLA(Forecast, AHT, Agents, AWT, Lines, Patience),3)
#     print("Number of agents:",Agents)
#     print('OUTPUTS:')
#     print("Average speed of answer:",ASA)
#     print("Service level:",SL)

# elif calc_option==1:
#     # Agents (SL) Calculation (2nd column):
#     SL = 0.8
#     Agents = round(ERLANG.CHAT.AGENTS_SLA(SL, Forecast, AHT, AWT, Lines, Patience),3)
#     ASA = round(ERLANG.CHAT.ASA(Forecast, AHT, Agents, Lines, Patience),3)
#     print("Service level:",SL)
#     print('OUTPUTS:')
#     print("Number of agents:",Agents)
#     print("Average speed of answer:",ASA)

