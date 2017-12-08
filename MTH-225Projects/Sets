def make_set(l):
    temp = []
    
    for i in l:
      if not i in temp:
          temp.append(i)         
    print(temp)
    return temp    
    
def inter(l1, l2):
    temp = []
    for i in l1:
        for x in l2:
            if x == i and x not in temp:
                temp.append(x)
    print(temp)
    return temp
    
def union(l1, l2):
    temp = []
    for i in l1:
        for x in l2:
            if x != i and x not in temp:
                temp.append(x)
                
    for i in l2:
        for x in l1:
            if x != i and x not in temp:
                temp.append(x)
    print(temp)
    return temp
    
def sym_dif(l1, l2):
    l1 = set(l1)
    l2 = set(l2)
    temp = []
    
    for i in l1:
        if i not in temp:
            temp.append(i)
    
    for j in l2:
        if j not in temp:
            temp.append(j)

    print(temp)
    return temp
    
def power(l):
    l = set(l)
    l = list(l)
    temp =[]
    temp2 = len(l)
    for count in range(1 << temp2):
        temp.append([l[count2] for count2 in range(temp2) if (count & (1 << count2))])
    print (temp)

    

make_set([1,2,3,2,3,2])
make_set(['I', 'want', 'to', 'sleep', 'sleep', 'sleep'])
make_set([1,9])
make_set([]) 
inter([1, 1, 2, 3, 5], [1, 1, 4, 5, 5]) 
inter([4, 5, 5, 4], [1, 2, 3, 1])
inter([3, 4, 5], [4, 4, 3, 5]) 
union([1,1,2,3], [3, 3, 3, 4])
union([1, 3], ['Tom']) 
sym_dif([1, 2, 3], [3, 4, 5]) 
sym_dif([1, 2, 3, 3], [4, 5, 6, 4])
sym_dif(['Tom', 'Jerry'], ['Jerry', 'Tom']) 
power([1,3,5]) 
power([1,1,1])
