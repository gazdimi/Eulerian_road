peaks = []
nodes = []
path = []                                                       #variable to store Eulerian closed road if it exists
def create_graph(n):                                            #create peaks, nodes for Kn graph
    for i in range(n):
        peaks.append(i+1)                                       #create peaks 1,2,...,n
        temp1 = peaks[i]
        for j in range(temp1,n+1):                              #create nodes
            if(temp1==j):
                continue                                        #continue if node [1,1] for example has been created because such nodes don't exist
            else:
                nodes.append([temp1,j])

def check(nodes):                                               #check if Eulerian closed road exists, it exists only when peaks' degree is even
    degree = 0
    for i in nodes:
        for j in i:
            if (j==1):
                degree+=1                                       #in Kn graph all peaks have the same degree, so only first peak's degree is calculated
    return (degree%2 == 0)                                      #return True/False according to the degree

def find_eulerian_path():                                       #find Eulerian closed road, starting point equals ending point
    i = 0
    path.append(nodes[0])                                       #initialize eulernian closed road with the first node
    previous_temp = path[0]                                     #hold previous node added in the Eulerian closed road
    nodes.pop(0)                                                #remove the first nod in nodes, as it has been used
    while True:
        if (len(nodes)==0):                                     #if all nodes have been used and added in right position in Eulerian closed road
            break                                               #end loop
        temp = nodes[i]                                         #store in temp the current node (pair of peaks)
        reversed_temp = nodes[i][::-1]                          #create reversed node for e.g. for node [1,3] store reversed node [3,1]
        if (previous_temp[1]==temp[0]):                         #for example for if previous_temp=[1,3] and current temp is [3,4] then previous_temp[1]=3=temp[0]
            path.append(temp)                                   #add the node to Eulerian closed road
            nodes.pop(i)                                        #remove the node that has been used
            previous_temp=temp
        elif (previous_temp[1]==reversed_temp[0]):              #check if current node can connect with the reversed node
            path.append(reversed_temp)
            nodes.pop(i)
            previous_temp = reversed_temp
        if (i+1>=len(nodes)):                                   #if i identifier is out of range for idenxing nodes list
            i=0                                                 #start index from 0
        else:
            i+=1
    return path, nodes

while True:
    try:
        n = int(input("Give number to create Kn graph: "))      #get user's input number
        if ( n!=1 and n>0):                                     #if n is valid break loop
            break
        else:
            print("Invalid number, can't create graph with only one peak.\n")
            continue
    except Exception as e:
        print("Invalid input character, try again.\n")
        continue

create_graph(n)
flag = check(nodes)                                             #use logic variable to store the result of check function
if (flag):                                                      #case of existing Eulerian closed road
    nodes_counter = len(nodes)                                  #get number of elements stored in nodes
    path, nodes = find_eulerian_path()                          #calculate the Eulerian closed road
    if (len(nodes) == 0 and len(path) == nodes_counter):        #if all nodes have been used (nodes must have 0 elements, and path's elements must be equal to total number of Kn's nodes)
        print("Given graph's peaks: " + str(peaks) + "\nEulerian closed road found in given graph: " + str(path))
    else:
        print("There was an error during processing, please try again later!!")
else:
    print("Eulerian closed road doesn't exist for given graph.")
