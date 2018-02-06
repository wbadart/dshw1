#!/usr/bin/env python3

'''
wbadart-HW1-Q3.py

Implementation of the coding components of Data Science HW1, SVD question.

Referenced the numpy online documentation.
See:

    https://docs.scipy.org/doc/numpy/index.html

And

    https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.svds.html

Will Badart <netid:wbadart>
created: FEB 2018
'''

import numpy as np
from csv import reader
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import svds

GRAPH_PATH = './graph.csv'


if __name__ == '__main__':
    with open(GRAPH_PATH) as fs:
        labels, *data = reader(fs)
    data = [tuple(row[1:]) for row in data]
    data = csc_matrix(np.array(data, dtype=float))
    u, s, vh = svds(data, k=2)
    print('left singular vector U[{}x{}]:'.format(*u.shape))
    print(u)
    print()
    print('singular values:')
    print(s)
