# SDF Simulator

It receives some data and simulates the output of the SDF.\n
This is my Co-Design Project in university of Kashan.\n

# Inputs
**Output Matrix:**
It is the outputs of each actor.
_Sample:_ 
0,1,1
1,1,2
2,1,3
3,1,-2

-2 in here is the virtual ending node.

**Input Matrix:**
It is the inputs of each actor.
_Sample:_
-1,1,0
0,1,1
1,1,2
2,1,3

-1 in here is the virtual starting node.

**Matrix of edges:**
A matrix of 0 and 1.
_Sample:_
0,1,0,0
0,0,1,0
0,0,0,1
0,0,0,0

**Primary Tokens:**
The primary tokens
_Sample:_
10
0,1,0,0
0,0,0,0
0,0,0,1
0,0,0,0

10 at the first is the primary tokens that are waiting to enter the SDF.

**Processing Time of each node**
_Sample:_
3,4,2,3

**Number of clocks**
_Sample:_
100

**Frequency of each clock**
_Sample:_
2


