import numpy as np

"""
Define a 10x10 matrix A whose entries are the numbers from 1 to 100 ordered consecutively going across rows
(so a_1,1 = 1, a_2,1 = 11, a_10,1 = 91, etc)
Let v = (1, 2, ...10), and b = (1, 1, ...1).
Compute Av and solve Ax = b and Ax = v using linalg.solve.
Verify your solution by computing Ax.
"""

# 10 by 10 matrix A from 1 to 100 (Note: This is a Singular Matrix!)
A = np.arange(1,101).reshape(10,10)

# 10 by 1 vector from 1 to 10
v = np.arange(1,11).reshape(10,1)

# 10 by 1 vector, all ones
b = np.ones((10,), dtype=np.int).reshape(10,1)

# checking...
# print A
# print v
# print b

# compute Av
print "Computing Av..."
print np.dot(A, v)

# solve for Ax = b
# ERROR: matrix A is a Singular matrix, so x cannot be solved.
# Thus, the next two lines of code are commented out.
# x = np.linalg.solve(A, b)
# print x

# solve for Ax = v
# ERROR: matrix A is still a Singular matrix, so x cannot be solved.
# Thus, the next two lines of code are commented out.
# x2 = np.linalg.solve(A, v)
# print x2

# verify with Ax
# ERROR: cannot verify with Ax because x is still not solved.
# Thus, the next line of code is commented out.
# print np.dot(A, x)

"""
How do we solve this? Add some noise to the matrix!
"""

"""
Use the rand command to build a 10x10 matrix R(e).
Verify now that you can compute the questions above for various values of 1 >> e > 0 for the new matrix A + R(e). 
"""

# epsilon e
e = np.random.random_sample()
print "The epilson is: " + str(e)

# 10 by 10 matrix R(e)
Re = np.random.uniform(-e, e, size=(10, 10))

# 10 by 10 matrix A from 1 to 100 (NOTE: This is a Singular Matrix!)
A = np.arange(1, 101).reshape(10, 10)

# 10 by 1 vector v from 1 to 10
v = np.arange(1, 11).reshape(10, 1)

# 10 by 1 vector b filled with all ones
b = np.ones((10,), dtype=np.int).reshape(10, 1)

# new 10 by 10 matrix Noise or N = A + Re
N = A + Re
print "The new matrix N = A + Re is..."
print N

# solve for Nx = b using linalg.solve
x = np.linalg.solve(N,b)
print "Solution: using linalg.solve, vector x for Nx = b is..."
print x

# solve for Nx = v using linalg.solve
x2 = np.linalg.solve(N,v)
print "Solution: using linalg.solve, vector x2 for Nx = v is..."
print x2

# verify solution for x is correct
# should print vector b
print "Verifying the solution for x..."
print np.dot(N,x)

# verify solution for x2 is correct
# should print vector v
print "Verifying the solution for x2..."
print np.dot(N,x2)

