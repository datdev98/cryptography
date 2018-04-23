import numpy as np

def dot(matrix, other):
    result = matrix.dot(other)
    for (x,y), value in np.ndenumerate(result):
        result.itemset((x,y), value % 26)
    return result

def det(matrix):
    return np.linalg.det(matrix)


P = np.matrix(input('Input plaintext: '))
E = np.matrix(input('Input key: '))

C = dot(P, E)

print(C)

