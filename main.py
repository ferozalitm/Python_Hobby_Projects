########################################################################################################################
# Author: T M Feroz Ali
# Email: ferozalitm@gmail.com, feroz.tm.ali@gmail.com
# Date: 10/Sep/2021
#
# Problem:
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
########################################################################################################################



# MAIN SCRIPT
########################################################################################################################

import functions as fn
# Reading input data
openMsg = "Type Adjacency mode. 1:Horiz 2:Vert 3: Diag 4: Horiz+Vert 5: Horiz+Vert+Diag \n"
adjMode = int(input(openMsg))
rows_col = list(map(int, input("Input #Rows #Col with space: ").split()))
nrows = rows_col[0]
ncols = rows_col[1]
Mat = []
dataFormat = "Type data in rows. Type 'Enter' after finishing each row \n"
print(dataFormat)
for i in range(1, nrows + 1):
    row = list(map(int, input().split()))
    Mat.append(row)

Mat = fn.padMatrix(Mat)
B = []
class_count = 1
for i in range(1, len(Mat) - 1):
    for j in range(1, len(Mat[0]) - 1):
        if not fn.isPivot(Mat, i, j):
            #(i, j, "not Pivot")
            continue
        else:
            #(i, j, "is Pivot")
            Neigh, Idx = fn.getNeighbours(Mat, i, j, adjMode)
            if fn.isNeighAllOnes(Neigh):
                # NeighAllOnes: Declare new class
                class_count = class_count + 1
                B = fn.addNewClass(B, Idx)
                for (r, s) in Idx:
                    Mat[r][s] = class_count
            else:
                max_class = max(Neigh)
                # assigning all 1s to max_class
                for k, x in enumerate(Neigh):
                    if x == 1:
                        Neigh[k] = max_class
                        #Adding all 1s to max_class in B
                        class_t = fn.MatId2B_id([max_class])
                        B = fn.appendClass(B, class_t[0], [Idx[k]])

                # Find the unique values in Neigh
                # Convert unique(Neigh2) to Bid
                unqNeigh = fn.unique_num(Neigh)
                B_unqNeigh = fn.MatId2B_id(fn.unique_num(Neigh))
                if len(B_unqNeigh) == 1:
                    # if only one class, then append elements to the class
                    B = fn.appendClass(B, B_unqNeigh[0], Idx)
                else:
                    # Else merge Bid classes in B
                    B = fn.mergeMultipleClasses(B, B_unqNeigh)
                # Get all indices of max_class from B and update their values in Mat to max_class
                temp = B[fn.MatId2B_id([max_class])[0]]
                for m, n in temp:
                    Mat[m][n] = max_class

# Some connecting 1s between two clusters may be assigned to a class, and that 1 may not get a chance as a pivot.
# Solution: Repeat exp where pivot2 is any non-zero element, and it has more than two unique neighbors
for i in range(1, len(Mat) - 1):
    for j in range(1, len(Mat[0]) - 1):
        if (Mat[i][j] == 0):
            continue
        else:
            Neigh, Idx = fn.getNeighbours(Mat, i, j, adjMode)
            max_class = max(Neigh)
            unqNeigh = fn.unique_num(Neigh)
            if len(unqNeigh) >= 1:
                B_unqNeigh = fn.MatId2B_id(unqNeigh)
                B = fn.mergeMultipleClasses(B, B_unqNeigh)
                temp = B[fn.MatId2B_id([max_class])[0]]
                for m, n in temp:
                    Mat[m][n] = max_class

# Finding total number of clusters
total_clusters = 0
for x in B:
    if len(x) != 0:
        total_clusters = total_clusters + 1
print("No. of clusters = ", total_clusters)
print("Cluster map:")
Mat_trim = []
for i in range(1, len(Mat) - 1):
        Mat_trim.append(Mat[i][1:len(Mat[0])-1])

fn.print_matrix(Mat_trim)








