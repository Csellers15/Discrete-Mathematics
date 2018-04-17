'''
The Power function returns the power set of the dictionary that is inputted as
the graph.
'''
def power(graph):
    #sets graph equal to a set and a list.
    graph = set(graph)
    graph = list(graph)
    #temporary array used as the holder of the power set
    temp =[]
    #temporary variable that golds the length of the graph
    temp2 = len(graph)
    #iterates through the temp array that is shifted over
    for count in range(1 << temp2):
        # appends the graph at the position of the count to temp
        temp.append([graph[count2]
        # for loop for count 2
        for count2 in range(temp2)
        if (count & (1 << count2))])
        # returns temp
    return (temp)


'''
This method splits the graph into its partite sets assuming that the graph is
bipartite
'''
def partite_sets(graph):
    #temporary sets to hold the values
    setA = []
    setB =[]

    #iterates throhg the keys of the graphs and adds the fist one to set A
    for key in graph:
        setA += key
        break

    #Iterates throught the rest of the keys
    for key in graph:
        #if the key is in set A.
        if key in setA:
            #iterates through the graphs specific key
            for value in graph[key]:
                #if the value of the keys specific location isnt in setB it adds it to setA
                if value not in setB:
                    setB += value
        #if the key isnt in setA it enters this.
        else:
            #iterates through the graphs specific key
            for value in graph[key]:
                #if the value isnt in setA then it adds it to setA
                if value not in setA:
                    setA += value
    #variable for the final set
    finalSet = []
    #appends the values of set a and set b to the final set
    finalSet.append(setA)
    finalSet.append(setB)

    #returns the final set
    return finalSet

'''
Checks if the graph is bipartite or not
'''
def is_bipartite(graph):
    #creates a temprary array and sets calls partite_sets againn making puting the partite sets intto left and right variables
    temp = partite_sets(graph)
    left = temp[0]
    right = temp[1]
    result = True

    # Iterates throught the left array
    for i in left:
        # if the position i is in the right arrray set the result to false
        if i in right:
            result = False
    #Returns false
    return result


'''
Checks if the graph is a perfect matching or not
'''
def is_perfect(graph):
    #sets the partite sets into x and y and status to true.
    status = True
    partite = partite_sets(graph)
    x = power(partite[0])
    y = power(partite[1])

    #iterates through the x array
    for nh in x:
        temp = []
        #iterates through the nodes in nh
        for node in nh:
            #sets temp variable equal to the list of the set of temp and unions it to graph at a specific node
            temp = list(set(temp).union(graph[node]))
        # if the length of temp is less that nh set the status to false
        if len(temp) < len(nh):
            status = False

    #iterates through the y array
    for nh in y:
        temp = []
        #iterates through the nodes in nh
        for node in nh:
            #sets temp variable equal to the list of the set of temp and unions it to graph at a specific node
            temp = list(set(temp).union(graph[node]))
        # if the length of temp is less that nh set the status to false
        if len(temp) < len(nh):
            status = False

    #returns the status variable
    return status



print(power(['A', 'B']))
print(power(['A', 'B', 'C'])  )

print(partite_sets({'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}))
#return ['A'],[“B”,“C”] (or [“B”, “C”], ['A'])
print(partite_sets({'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A','D'], 'D': ['B', 'C']}))
#return ['A', “D”], [“B”, “C”] (or [“B”, “C”], ['A', “D”])

print(is_bipartite({'A': ['B', 'C'], 'B': ['A'],'C': ['A']}))
#return True
print(is_bipartite({'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}))
 #return False

print(is_perfect({'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}))  # return True
print(is_perfect({'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}))  # return False
