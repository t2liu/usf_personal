"""
Function that finds the best fit line in the sense of least squares 
to a set of data consisting of paired observations in the form (x, y).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def leastSquares(filename):

    #read in only columns 'x' and 'y'
    fields = ['x', 'y']

    fr = pd.read_csv(filename, usecols=fields)

    col1 = np.array(fr.x, dtype=float).reshape(len(fr.x), 1)
    col2 = np.ones(len(fr.x), dtype=float).reshape(len(fr.x), 1)

    b = np.array(fr.y, dtype=float).reshape(len(fr.y), 1)
    matrixA = np.concatenate((col1, col2), axis=1)
    Atranspose = np.transpose(matrixA)

    At_A = np.dot(Atranspose, matrixA)

    At_b = np.dot(Atranspose, b)

    xhat = np.linalg.solve(At_A, At_b)

    slope = xhat.item(0)
    intercept = xhat.item(1)

    print
    print "The slope of the " + filename + " data is..."
    print slope
    print "The intercept of the " + filename + " data is..."
    print intercept

    A_xhat = np.dot(matrixA, xhat)

    minimize = A_xhat - b
    square_minimize = minimize**2
    sum_square = np.sum(square_minimize)

    print "The sum of the squares of the distances for the " + filename + " data is..."
    print sum_square

    line = slope * col1 + intercept

    plt.plot(fr.x, fr.y, '*')
    plt.plot(fr.x, line)
    plt.show()

