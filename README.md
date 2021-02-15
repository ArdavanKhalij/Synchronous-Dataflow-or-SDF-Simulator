# SDF Simulator

It receives some data and simulates the output of the Synchronous Dataflow(SDF). It also make the Gantt graph of each token and also 
a network graph for showing the SDF graph.<br/>
This is my Co-Design Project in university of Kashan.<br/><br/>

# Inputs
**Output Matrix:**<br/>
It is the outputs of each actor. (from,number of tokens,to)<br/>
Remmber the format should be exactly like this, otherwise it doesn't work.<br/>
_Sample:_ <br/>
0,1,1<br/>
1,1,2<br/>
2,1,3<br/>
3,1,-2<br/>
<br/>
-2 in here is the virtual ending node.<br/>
<br/>
**Input Matrix:**<br/>
It is the inputs of each actor. (from,number of tokens,to)<br/>
Remmber the format should be exactly like this, otherwise it doesn't work.<br/>
_Sample:_<br/>
-1,1,0<br/>
0,1,1<br/>
1,1,2<br/>
2,1,3<br/>
<br/>
-1 in here is the virtual starting node.<br/>
<br/>
**Matrix of edges:**<br/>
A matrix of 0 and 1.<br/>
Remmber the format should be exactly like this, otherwise it doesn't work.<br/>
_Sample:_<br/>
0,1,0,0<br/>
0,0,1,0<br/>
0,0,0,1<br/>
0,0,0,0<br/>
<br/>
**Primary Tokens:**<br/>
The primary tokens<br/>
Remmber the format should be exactly like this, otherwise it doesn't work.<br/>
_Sample:_<br/>
10<br/>
0,1,0,0<br/>
0,0,0,0<br/>
0,0,0,1<br/>
0,0,0,0<br/>
<br/>
10 at the first is the primary tokens that are waiting to enter the SDF.<br/>
<br/>
**Processing Time of each node**<br/>
Remmber the format should be exactly like this, otherwise it doesn't work.<br/>
_Sample:_<br/>
3,4,2,3<br/>
<br/>
**Number of clocks**<br/>
Remmber the format should be exactly like this, otherwise it doesn't work.<br/>
_Sample:_<br/>
100<br/>
<br/>
**Frequency of each clock**<br/>
Remmber the format should be exactly like this, otherwise it doesn't work.<br/>
_Sample:_<br/>
2<br/>
<br/>

Github link: https://github.com/ArdavanKhalij/Synchronous-Dataflow-or-SDF-Simulator
