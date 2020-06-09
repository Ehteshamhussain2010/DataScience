import numpy as np

def matrix_mul(A,B):
    R = A.dot(B)
    return R

def matrix_inverse(A):
   R = np.linalg.inv(A)
   return  R

def matrix_eigenvals(A) :
    R= np.linalg.eigvals(A)
    return  R

def matrix_eigenvector(A) :
    R= np.linalg.eig(A)
    return  R

def matrix_rank(B):
    R= np.linalg.matrix_rank(B)
    return

def matrix_det(A):
    R= np.linalg.det(A)
    return R


if __name__ == '__main__':
 A = [2, -5, 6, 3, 2, 4, 2, 1, 3]
 B = [2, 4, 4, 5, -1, 2, 6, 2, 2]
 A = np.array(A).reshape((3, 3))
 B = np.array(B).reshape((3, 3))

 _inverse = matrix_inverse(A)
 _product = matrix_mul(A, B)

 _rank = matrix_rank(A)
 _determinant = matrix_det(A)

 _eignVal = matrix_eigenvals(A)
 _eignenvector = matrix_eigenvector(A)

 print('\n Printing Matrix A')
 print(A)
 print('\n Printing Matrix B')
 print(B)
 print('\n Inverse of Matrix A&B')
 print(_inverse)
 print('\n Product of Matrix A&B')
 print(_product)
 print('\n Rank of Matrix A&B')
 print(_rank)
 print('\n Determinant of Matrix A&B')
 print(_determinant)
 print('\n EigenVal of Matrix A&B')
 print(_eignVal)
 print('\n EigenVector of Matrix A&B')
 print(_eignenvector)