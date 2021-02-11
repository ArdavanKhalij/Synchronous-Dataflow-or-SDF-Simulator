# Libraries
from copy import deepcopy
# Libraries
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
# Get from inputs
num = 0
def getInput(Actors, z):
    global num
    ContinueOrNot = 0
    for j in range(0, len(Actors[z].Input)):
        if Actors[z].Input[j][1] >= Actors[z].Input[j][2]:
            num = num + 1
    if num == len(Actors[z].Input) and Actors[z].Busy == 0 and Actors[z].ID != len(Edges):
        for c in Actors[z].Input:
            c[1] = c[1] - c[2]
        pt = Actors[z].ProcessingTime
        Actors[z].Busy = pt
        ContinueOrNot = 1
    num = 0
    return ContinueOrNot
# Get from inputs
# Main loop
Times = []
for i in range(0, NumberOfClocks):
    for z in range(0, len(Actors)):
        # Get from inputs
        if getInput(Actors, z) == 1:
            continue
        # Get from inputs
        # Shoot the answers
        if z == len(Edges) and Actors[z].Input[0][1] == 1:  # and Actors[kk-1].Input[0][1] > 0:
            if i+4<NumberOfClocks:
                Times.append(i)
            Actors[z].Input[0][1] = 0
        if Actors[z].Busy == 1:
            Actors[z].Busy = 0
            for j in range(0, len(Actors[z].Output)):
                kk = len(Actors)
                index = Actors[z].Output[j][1]
                if index == 5:
                    continue
                InputChangerIndex = 0
                for ip in range(0, len(Actors[index].Input)):
                    if Actors[index].Input[ip][0] == Actors[z].ID:
                        InputChangerIndex = ip
                Actors[index].Input[InputChangerIndex][1] = Actors[index].Input[InputChangerIndex][1] + Actors[z].Output[j][0]
                # Get from inputs
                if getInput(Actors, z) == 1:
                    continue
                # Get from inputs
        elif Actors[z].Busy == 0:
            pass
        else:
            Actors[z].Busy = Actors[z].Busy - 1
        # Shoot the answers
# Main loop
# Print the result
for i in range(0, len(Times)):
    print("Token number "+str(i+1)+" came out in Clock number "+str(Times[i])+" and after "+str(Times[i]/FrequencyOfClock)+" seconds based on the frequency you entered.")
if len(Times)>0:
    print("Latency : "+str(Times[0]))
    if len(Times)>1:
        end = len(Times)-1
        print("Throughput : 1/"+str(Times[end] - Times[end-1]))
    else:
        print("Throughput is not available for 1 token.")
else:
    print("Latency and Throughput are not available for 0 token.")
# Print the result
