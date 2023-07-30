# def same_structure_as(original,other):
#     for i in range(0, len(original)):
#         pass


# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# # should return False 
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

a = [1, 2, 3]
b = [10, 20]
c = zip(a, b)
print(set(c))
for el in c:
    print(el)