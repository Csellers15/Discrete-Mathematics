# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:21:36 2017

Combinations and Permutatoins

By Zachary Thomas, Cole Sellers, Hai Duong, and Matthew Doan
"""

#Factorial function
#Takes a number and decreases it by one and times it by it until it reaches 1
def factorial(number):
    number = float(number)
    total = 1.0
    while number > 0:
        total *= number
        number -= 1
    return total


print ()
print ("Factorial")
print (factorial(5)) #Should return 120
print (factorial(0)) #Should return 1


#Choose function
#Takes two inputs and uses the choose formula.
def choose(n,k):
    num = factorial(float(n)) / ((factorial(float(k))) * (factorial(float(n - k))))
    return num

print ()
print ("Choose")
print (choose(5,3)) #Should return 10
print (choose(5,5)) #Should return 1
print (choose(3,2)) #Should return 5


#Permutation funcion
#Gives total permutations with two numbers input
def perm(n,k):
    num = factorial(float(n)) / (factorial(float(n - k)))
    return num

print ()
print ("Permutations")
print (perm(5,3)) #Should return 60
print (perm(5,5)) #Should return 120
print (perm(5,0)) #Should return 1


#Two lattice paths function
#Finds the total paths in between two points
#Splits a dictionary into two lists, with x in orderTop and y in orderBot
def lat_two(dict):
    orderTop = []
    orderBot = []
    for num in dict:
        orderTop.append(num)
        orderBot.append(dict[num])
        
    #If statement to see if both x's are the same
    if len(orderTop) == 1:
        return 0.0
    
    #Lattice path formula to find total paths, then calls the choose funtion
    top = (orderBot[1] - orderBot[0]) + (orderTop[1] - orderTop[0])
    bot = orderBot[1] - orderBot[0]
    total = choose(top, bot)
    return total    
        
print ()
print ("Two points total lattice paths")    
print (lat_two({0 : 0, 5 : 3})) #Should return 56
print (lat_two({2 : 5, 3 : 5})) #Should return 1
print (lat_two({1 : 2, 3 : 5})) #Should return 10
print (lat_two({3 : 2, 9 : 8})) #Should return 924
print (lat_two({1 : 1, 1 : 1})) #Should return 0


#Three lattice paths function
#Finds the total paths in between three points
#Splits a dictionary into two lists, with x in orderTop and y in orderBot
def lat_three(dict):
    orderTop = []
    orderBot = []
    for num in dict:
        orderTop.append(num)
        orderBot.append(dict[num])
        
    #If statement to see if both x's are the same
    if len(orderTop) == 1:
        return 0.0
    
    #Need two choose calls because there are three points to find paths for
    top = (orderBot[1] - orderBot[0]) + (orderTop[1] - orderTop[0])
    bot = orderBot[1] - orderBot[0]
    top2 = (orderBot[2] - orderBot[1]) + (orderTop[2] - orderTop[1])
    bot2 = orderBot[2] - orderBot[1]
    total = choose(top, bot) * choose(top2, bot2)
    return total    

print ()
print ("Three points total lattice paths")
print (lat_three({0 : 0, 2 : 1, 5 : 3})) #Should return 30
print (lat_three({2 : 5, 3 : 5, 5 : 5})) #Should return 1


#Permutation of 3 items in a list function
#Shows all possible permutations of a list
def list_perm(list):
    totalList = []
    
    # All items in list are the same
    if list[0] == list[1] == list[2]:
      totalList.append(list)
      #Need this here to end the function
      return totalList
    
    # All items in  list are different
    if list[0] != list[1] != list[2]:
      totalList.append(list)
      totalList.append([list[0],list[2],list[1]])
      totalList.append([list[2],list[0],list[1]])
      totalList.append([list[2],list[1],list[0]])
      totalList.append([list[1],list[2],list[0]])
      totalList.append([list[1],list[0],list[2]])
     
    # 2 Items in the list are the same
    if list[0] == list[1]:
      totalList.append(list)
      totalList.append([list[0],list[2],list[1]])
      totalList.append([list[2],list[0],list[1]])
    
    if list[0] == list[2]:
      totalList.append(list)
      totalList.append([list[1],list[0],list[2]])
      totalList.append([list[0],list[2],list[1]])
        
    if list[1] == list[2]:
      totalList.append(list)
      totalList.append([list[1],list[0],list[2]])
      totalList.append([list[1],list[2],list[0]])

    return totalList
  
print ()
print ("Permutation of lists")
print (list_perm([ 1, 2, 3])) #Should return [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
print (list_perm([1,1,3])) #Should return [[1,1,3], [1,3,1], [3,1,1]]
print (list_perm([0,0,1])) #Should return [[0,0,1], [0,1,0], [0,0,1]]
print (list_perm([0,0,0])) #Should return [[0,0,0]]
