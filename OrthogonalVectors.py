# Suppose I have two vectors: (a1, a2, a3, ..., aN) and (b1, b2, b3, ..., bN). 
# The dot product between these two vectors is defined as:

# a1*b1 + a2*b2 + a3*b3 + ... + aN*bN
# The vectors are classified as orthogonal if the dot product equals zero.

# Complete the function that accepts two sequences as inputs and returns true 
# if the vectors are orthogonal, and false if they are not. The sequences will 
# always be correctly formatted and of the same length, so there is no need to 
# check them first.
# [1, 1, 1], [2, 5, 7]        --> false
# [1, 0, 0, 1], [0, 1, 1, 0]) --> true


def is_orthogonal(u, v): 
    total = 0
    for ix in range(len(u)):
        total += u[ix]*v[ix]
    
    return total == 0