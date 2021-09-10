# Python_Hobby_Projects

# Programming Problem:
# Find connected neighbours in a binary matrix and count the number of clusters, based on a given adjacency mode
# "Adjacency modes: 1:Horizontal 2:Vertical 3: Diagonal 4: Horizontal+Vertical 5: Horizontal+Vertical+Diagonal
#  O(N) complexity; Numpy library not allowed: Only basic python 3 allowed.
#
# Input format:
# 1: <Adjacency mode>
# 2: <No. of rows> <No. of cols>
# 3: <Binary matrix: each row in seperate line; elements in a row seperated by space>
#
# Output:
# 1: No. of clusters
# 2: Matrix with each unique element representing a distinct cluster
#
# Example input/output data for diagonal mode, 2X3 matrix
# 1: 3
# 2: 5 4
# 3: 1 1 1 1
#    0 1 1 0
#    0 0 1 0
#    1 1 1 0
#    0 0 1 1
#
# Output
# 1: No. of clusters = 4
# 2: Cluster map:
#    2 3 2 3
#    0 2 3 0
#    0 0 2 0
#    4 2 5 0
#    0 0 2 5
#
