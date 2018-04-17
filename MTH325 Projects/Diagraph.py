import copy

'''
This method takes in the ground and relation and determines if
they are relxexive
'''
def is_reflex(ground, relation):
    # iterates through the ground.
    for element in ground:
        #adds the ground element at a certain poition to compare
        compare = [element, element]
        #if its not in the relation that was passed return false
        if compare not in relation:
            return False
    #return true if it is relxexive
    return True


'''
This method takes in the ground and relation and determines if
they are symmetric
'''
def is_sym(ground, relation):
    #copies relation into the copy variable
    temp = copy.deepcopy(relation)
    #iterates through the copy.
    for element in temp:
        #sets the side by side element to compare
        compare = [element[1], element[0]]
        #if compare is not in temp return false else remove compare from copy
        if compare not in temp:
            return False
        else:
            temp.remove(compare)
    # returns true if it is symmetric
    return True

print(is_reflex(['A','B','C','D','E'], [['A','A'],['A','D'],['B','C'],['B','D'],['C','E'],['D','A'],['E','E']])) #false
print(is_reflex(['A', 'B', 'C'], [['A', 'A'], ['A', 'B'], ['A', 'C'], ['B', 'B'], ['B', 'A'], ['C', 'C'], ['C', 'A']])) #true

print(is_sym(['A','B','C','D','E'], [['A','A'],['A','D'],['B','C'],['B','D'],['C','E'],['D','A'],['E','E']])) #false
print(is_sym(['A', 'B', 'C'], [['A', 'A'], ['A', 'B'], ['A', 'C'], ['B', 'B'], ['B', 'A'], ['C', 'C'], ['C', 'A']])) #true
