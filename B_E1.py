peaks = []
nodes = []
path = []
def create_graph(n):                                        #create peaks, nodes for Kn
    for i in range(n):
        peaks.append(i+1)
        temp1 = peaks[i]
        for j in range(temp1,n+1):
            if(temp1==j):
                continue
            else:
                nodes.append([temp1,j])

def check(nodes):
    degree = 0
    for i in nodes:
        for j in i:
            if (j==1):
                degree+=1
    return (degree%2 == 0)

def find_eulerian_path():                                       #closed path, starting point equals ending point
    i = 0
    path.append(nodes[0])                                       #initialize eulernian closed road with the first node
    previous_temp = path[0]
    nodes.pop(0)
    while True:                                #for each node in the Kn graph except for the first
        if (len(nodes)==0):
            break
        temp = nodes[i]
        reversed_temp = nodes[i][::-1]
        if (previous_temp[1]==temp[0]):
            path.append(temp)
            nodes.pop(i)
            previous_temp=temp
        elif (previous_temp[1]==reversed_temp[0]):
            path.append(reversed_temp)
            nodes.pop(i)
            previous_temp = reversed_temp
        if (i+1>=len(nodes)):
            i=0
        else:
            i+=1
    return path, nodes

while True:
    try:
        n = int(input("Give number to create Kn graph: "))
        break
    except Exception as e:
        print("Invalid input character, try again.\n")
        continue

create_graph(n)
flag = check(nodes)
if (flag):
    nodes_counter = len(nodes)
    path, nodes = find_eulerian_path()
    if (len(nodes) == 0 and len(path) == nodes_counter):
        print("Given graph's peaks: " + str(peaks) + "\nEulerian closed road found in given graph: " + str(path))
    else:
        print("There was an error during processing, please try again later!!")
else:
    print("Eulerian closed road doesn't exist for given graph.")
