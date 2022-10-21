import sys

instances = int(sys.stdin.readline())

for i in range(instances):
    numNodes = int(sys.stdin.readline()) # number of nodes in the current graph
    adjList = dict() # adjacency list for each node
    nodes = list() # simple list of nodes
    check = False # handles the case where all nodes are disconnected

    # fills adjList and nodes with the stdin input
    for j in range(numNodes):
        line = sys.stdin.readline().split()
        nodes.append(line[0])
        adjList[line[0]] = line[1:]
        if(len(line[1:]) > 0):
            check = True

    # handles all disconnected case
    if(not check):
        print(" ".join(str(i) for i in nodes))
        continue

    visited = {node:False for node in nodes} # all visited nodes
    parent = {node:None for node in nodes} # a node that caused nother node to be added to the stack

    tree = list() # DFS tree
    stack = list() # stack structure for tracking nodes
    stack.append(nodes[0]) # begin DFS on the first node
    disCount = 1 # handle the case where the first nodes are disconnected

    while(len(stack) != 0):
        # get and remove a node
        node = stack[len(stack) - 1]
        stack.remove(node)

        # handle the case where the first nodes are disconnected
        if(len(adjList[node]) == 0):
            tree.append((parent[node], node))
            visited[node] = True
            adjList[node] = "-"
            stack.append(nodes[disCount])
            disCount += 1
            continue

        if(not visited[node]):
            tree.append((parent[node], node)) # adds edge to DFS tree
            visited[node] = True # marks node as visited

            # adds sorted neighbour nodes to the stack
            # handles order properly
            sortedNodes = list()
            for neighbour in adjList[node]:
                sortedNodes.insert(0, neighbour)
                parent[neighbour] = node
            stack += sortedNodes

    # handles output
    disconnectedNodes = " ".join(str(i) for i in [node for node in adjList if len(adjList[node]) == 0])
    if(len(disconnectedNodes) == 0):
        print(" ".join(str(i) for i in [item[1] for item in tree]))
    else:
        print(" ".join(str(i) for i in [item[1] for item in tree]) + " " + disconnectedNodes)
