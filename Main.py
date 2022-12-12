# Libraries
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt
# Libraries
# Output variable for file print
MainOutput = []
# Output variable for file print
# Read from files
with open('Input_Matrix.txt', 'r') as f:
    Inputs = [[int(num) for num in line.split(',')] for line in f]
f.close()
with open('Output_Matrix.txt', 'r') as f:
    Outputs = [[int(num) for num in line.split(',')] for line in f]
f.close()
with open('Matrix_of_Edges.txt', 'r') as f:
    Edges = [[int(num) for num in line.split(',')] for line in f]
f.close()
with open('Primary_Tokens.txt', 'r') as f:
    PrimaryToken = int(f.readline())
    PrimaryTokens = [[int(num) for num in line.split(',')] for line in f]
f.close()
with open('input.txt', 'r') as f:
    f.readline()
    ProcessingTimes = [int(num) for num in f.readline().split(',')]
    f.readline()
    f.readline()
    NumberOfClocks = int(f.readline())
    f.readline()
    f.readline()
    FrequencyOfClock = int(f.readline())
# Read from files
# Class of actor
class Actor:
    def __init__(self, ID, ProcessingTime, Input, Output):
        self.ID = ID
        self.ProcessingTime = ProcessingTime
        self.Input = deepcopy(Input)
        self.Output = deepcopy(Output)
        self.Busy = 0
# Class of actor
# Making a list of Actors
Actors = []
for i in range(0, len(Edges)):
    id = i
    ProcessingTime = ProcessingTimes[i]
    Input = []
    for j in range(0, len(Inputs)):
        if Inputs[j][2] == i:
            if Inputs[j][0] == -1:
                Input.append([Inputs[j][0], PrimaryToken, Inputs[j][1]])
            else:
                Input.append([Inputs[j][0], PrimaryTokens[Inputs[j][0]][Inputs[j][2]], Inputs[j][1]])
    Busy = 0
    Output = []
    for j in range(0, len(Outputs)):
        if Outputs[j][0] == i:
            if Outputs[j][2] == -2:
                Outputs[j][2] = len(Edges)
            Output.append([Outputs[j][1], Outputs[j][2]])
    AC = Actor(id, ProcessingTime, Input, Output)
    Actors.append(AC)
outp = []
for o in Outputs:
    if o[2] == -2:
        outp = deepcopy(o)
AC = Actor(len(Edges), 100, [[o[0],0,1]], [[1, len(Edges)+1]])
Actors.append(AC)
# Making a list of Actors
# Drawing SDF graph
SDF = nx.DiGraph()
for j in range(0, len(Actors)-1):
    SDF.add_node(str(Actors[j].ID))
    for i in Actors[j].Input:
        if(i[0]!=-1):
            SDF.add_edge(str(i[0]), str(Actors[j].ID))
nx.draw(SDF, node_size=600, with_labels=True)
plt.savefig("path_graph1.png")
plt.show()
# Drawing SDF graph
# Get from inputs
num = 0
def getInput(Actors, z, i):
    global num
    ContinueOrNot = 0
    for j in range(0, len(Actors[z].Input)):
        if Actors[z].Input[j][1] >= Actors[z].Input[j][2]:
            num = num + 1
    if num == len(Actors[z].Input) and Actors[z].Busy == 0 and Actors[z].ID != len(Edges):
        if(Actors[z].ID == 0):
            StartTime.append(i)
        for c in Actors[z].Input:
            c[1] = c[1] - c[2]
        pt = Actors[z].ProcessingTime
        Actors[z].Busy = pt
        ContinueOrNot = 1
        MainOutput.append("Clock Number "+str(i)+" : "+"Actor number "+str(z)+" is ready to get the inputs so inputs get into the actor.")
    else:
        if num != len(Actors[z].Input):
            MainOutput.append("Clock Number "+str(i)+" : "+"All the inputs are not ready to enter the actor number "+str(z)+".")
        if Actors[z].Busy != 0:
            MainOutput.append("Clock Number "+str(i)+" : "+"Actor number "+str(z)+" is still busy.")
    num = 0
    return ContinueOrNot
# Get from inputs
# Main loop
EndTimes = []
StartTime = []
for i in range(0, NumberOfClocks):
    for z in range(0, len(Actors)):
        # Get from inputs
        if getInput(Actors, z, i) == 1:
            continue
        # Get from inputs
        # Shoot the answers
        if z == len(Edges) and Actors[z].Input[0][1] == 1:  # and Actors[kk-1].Input[0][1] > 0:
            if i+4<NumberOfClocks:
                EndTimes.append(i)
            Actors[z].Input[0][1] = 0
        if Actors[z].Busy == 1:
            Actors[z].Busy = 0
            for j in range(0, len(Actors[z].Output)):
                kk = len(Actors)
                index = Actors[z].Output[j][1]
                if index == len(Actors):

                    continue
                InputChangerIndex = 0
                for ip in range(0, len(Actors[index].Input)):
                    if Actors[index].Input[ip][0] == Actors[z].ID:
                        InputChangerIndex = ip
                Actors[index].Input[InputChangerIndex][1] = Actors[index].Input[InputChangerIndex][1] + Actors[z].Output[j][0]
                # Get from inputs
                if getInput(Actors, z, i) == 1:
                    continue
                # Get from inputs
            MainOutput.append("Clock Number "+str(i)+" : "+"Actor number "+str(z)+"shooted and now it is free.")
        elif Actors[z].Busy == 0:
            pass
            MainOutput.append("Clock Number "+str(i)+" : "+"Actor number "+str(z)+" is still free.")
        else:
            Actors[z].Busy = Actors[z].Busy - 1
            MainOutput.append("Clock Number "+str(i)+" : "+"Actor number "+str(z)+" is still busy and it can shoot in "+str(Actors[z].Busy)+" clocks later.")
        # Shoot the answers
# Main loop
# Make Start times right
num=0
print(len(StartTime))
print(len(EndTimes))
for i in PrimaryTokens:
    for j in i:
        if j>0:
            num=num+j
for i in range(0, num):
    StartTime.insert(0, -1)
for i in range(0, len(EndTimes)-len(StartTime)):
    StartTime.insert(0, -1)
# Make Start times right
# Print the result
end = len(EndTimes)-1
for i in range(0, len(EndTimes)):
    if(StartTime[i]==-1):
        print("Token number " + str(i + 1) + " came out in Clock number " + str(EndTimes[i]) + " and after " + str(
            EndTimes[i] / FrequencyOfClock) + " seconds based on the frequency you entered.")
    else:
        print("Token number " + str(i + 1) + " had got in, in clock number " + str(
            StartTime[i]) + " and came out in Clock number " + str(EndTimes[i]) + " and after " + str(
            EndTimes[i] / FrequencyOfClock) + " seconds based on the frequency you entered.")
if len(EndTimes)>num and PrimaryToken!=0:
    print("Latency : "+str(EndTimes[num]-StartTime[num]))
    if len(EndTimes)>num+1:
        print("Throughput : 1/"+str(EndTimes[end] - EndTimes[end-1]))
    else:
        print("Throughput is not available for 1 token.")
else:
    print("Latency and Throughput are not available for 0 token.")
# Print the result
# Chart of process of each Token
fig, gnt = plt.subplots()
gnt.set_ylim(0, len(StartTime))
gnt.set_xlim(0, NumberOfClocks-1)
gnt.set_xlabel('Number of clocks')
gnt.set_ylabel('Tokens')
gnt.grid(True)
for i in range(0, len(EndTimes)):
    if(i % 2 == 0):
        gnt.broken_barh([(StartTime[i], EndTimes[i]-StartTime[i])], (i, 0.9), facecolors=('tab:red'))
    else:
        gnt.broken_barh([(StartTime[i], EndTimes[i] - StartTime[i])], (i, 0.9))
plt.show()
# Chart of process of each Token
# Write on file
with open('Output.txt','w') as f:pass
f.close()
with open('Output.txt','a') as f:
    for i in MainOutput:
        f.write(i+"\n")
# Write on file
