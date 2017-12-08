def arith(s, n, i):
    temp = []
    while i >= 0:
       temp.append(s)
       s = s + n
       i = i - 1
    
    return print(temp)

def geo(s, n, i):
    temp = []
    while i >= 0:
        temp.append(s)
        s = s * n
        i = i - 1
    return print(temp)
    

def recur(c1,c2,s1,s2):
    temp = [s1,s2]                      #temp list with start already in
    count = 8
    while count > 0:
        form = (c1)*(s1) + (c2)*(s2)    #recursive formula
        temp.append(form)
        s1 = temp[-1]                   #goes 1 back (an-1)
        s2 = temp[-2]                   #goes 2 back (an-2)
        count = count - 1
    return print(temp)

def delta_one(l):
    temp = []                       #temp list to perform test
    cur = 0                         #next position counter
    nex = 1                         #next position counter
    for i in range(1,len(l)):
        c = l[cur]
        n = l[nex]
        cur = cur + 1
        nex = nex + 1
        t = n - c
        temp.append(t)
    
    for i in range(1,len(temp)):    #test to see if all in list are the same
        for j in range(2, len(temp)):
            if temp[i] != temp[j]:
                return print(False)
   
    return print(True)              #prints true if passes the for loop test

def delta_two(l):
    cur = 0                         #position current counter
    nex = 1                         #next position counter
    statement = 2                   #counts the while loop down until it hits 0
    while statement > 0:            #loop to perform the math
        for i in range(1,len(l)):
            c = l[cur]
            n = l[nex]
            t = n - c
            l[cur] = t
            cur = cur + 1
            nex = nex + 1
        cur = 0
        nex = 1
        l.pop()
        statement = statement - 1
    
    for i in range(1,len(l)):       #test to see if all in list are the same
        for j in range(2, len(l)):
            if l[i] != l[j]:
                return print(False)
   
    return print(True)

def delta_three(l):
    cur = 0                         #position current counter
    nex = 1                         #next position counter
    statement = 3
    while statement > 0:
        for i in range(1,len(l)):
            c = l[cur]
            n = l[nex]
            t = n - c
            l[cur] = t
            cur = cur + 1
            nex = nex + 1
        cur = 0
        nex = 1
        l.pop()
        statement = statement - 1
        
    for i in range(1,len(l)):       #test to see if all in list are the same
        for j in range(2, len(l)):
            if l[i] != l[j]:
                return print(False)
   
    return print(True)              #prints true if passes the for loop test
