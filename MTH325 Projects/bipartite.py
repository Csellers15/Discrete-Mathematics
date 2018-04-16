def power(graph):
    graph = set(graph)
    graph = list(graph)
    temp =[]
    temp2 = len(graph)
    for count in range(1 << temp2):
        temp.append([graph[count2]
        for count2 in range(temp2)
        if (count & (1 << count2))])
    return (temp)


def partite_sets(graph):
    setA = []
    setB =[]

    for key in graph:
        setA += key
        break

    for key in graph:
        if key in setA:
            for value in graph[key]:
                if value not in setB:
                    setB += value
        else:
            for value in graph[key]:
                if value not in setA:
                    setA += value
    finalSet = []
    finalSet.append(setA)
    finalSet.append(setB)

    # print(finalSet)
    return finalSet


def is_bipartite(graph):
    temp = partite_sets(graph)
    left = temp[0]
    right = temp[1]
    result = True

    for i in left:
        if i in right:
            result = False
    return result


def is_perfect(graph):
    status = True
    partite = partite_sets(graph)
    x = power(partite[0])
    y = power(partite[1])          
    
    for nh in x:
        temp = []
        for node in nh:
            temp = list(set(temp).union(graph[node]))
        if len(temp) < len(nh):
            status = False
    
    for nh in y:
        temp = []
        for node in nh:
            temp = list(set(temp).union(graph[node]))
        if len(temp) < len(nh):
            status = False
            
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

print(is_perfect({'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}))  
#return True
print(is_perfect({'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}))  
#return False
