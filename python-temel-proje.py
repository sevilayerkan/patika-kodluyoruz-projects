def flatten(L):
    """
    #Approach 1
    flat = []
    for i in L:
        if isinstance(i, list):
            flatten(i)
        else:
            flat.append(i)
    """
    
    #Approach 2 : List Comprehension
    if type(L) is list:
        return [element for item in L for element in flatten(item)]
    else:
        return [L]



def reversed(L):
    L.reverse()
    return L


#List to be flatten
l1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
l2 = [[3], 2]

print(f'Before flatten: {l1} \nAfter flatten: {flatten(l1)} \n')
print(f'Before flatten: {l2} \nAfter flatten: {flatten(l2)} \n')

#List to reversed
l3 = [[1, 2], [3, 4], [5, 6, 7]]
print(f'Before reverse: {l3}')
print(f'After reverse: {reversed(l3)}')
