#!/usr/bin/python

import numpy 

# Read a matrix
mat = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graphMat = numpy.matrix(mat)

# Get the number of rows/columns
graphMat.shape  # returns (3,4)

# Access any element
graphMat[0,1]
graphMat[2,3]

# Set the value of an element
graphMat[0,1] = -8

# Access an entire row
graphMat[1]

# Access an entire column
graphMat[: , 1]