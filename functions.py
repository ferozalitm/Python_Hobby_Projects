########################################################################################################################
# FUNCTIONS
########################################################################################################################
def addNewClass(Set, elements):
    classSet = set()
    for x in elements:
        classSet.add(x)
    Set.append(classSet)
    return Set

def appendClass(Set, c1, elements):
    for x in elements:
        Set[c1].add(x)
    return Set

def mergeTwoClasses(Set, c1, c2):
    a = min(c1, c2)
    b = max(c1, c2)
    Set[b].update(Set[a])
    Set[a] = set()
    return Set

def mergeMultipleClasses(Set, classes):
    a = min(classes)
    for i in classes:
        if (a != i):
            Set = mergeTwoClasses(Set, a, i)
    return Set

def padMatrix(Mat):
    a = len(Mat)
    b = len(Mat[0])
    Mat2 = []
    Mat2.append([0] * (b + 2))
    for i in range(a):
        Row = [0]
        Row.extend(Mat[i][:])
        Row.extend([0])
        Mat2.append(Row)
    Mat2.append([0] * (b + 2))
    return Mat2

def isPivot(Mat, a, b):
    if Mat[a][b] == 1:
        return True
    else:
        return False

def getNeighbours_Adj_Horiz(Mat, a, b):
    Neigh = []
    Idx = []
    for j in range(b - 1, b + 2):
        if (Mat[a][j] != 0):
            Neigh.append(Mat[a][j])
            Idx.append((a, j))
    return Neigh, Idx

def getNeighbours_Adj_Vert(Mat, a, b):
    Neigh = []
    Idx = []
    for i in range(a - 1, a + 2):
        if (Mat[i][b] != 0):
            Neigh.append(Mat[i][b])
            Idx.append((i, b))
    return Neigh, Idx

def getNeighbours_Adj_HorizVert(Mat, a, b):
    Neigh = []
    Idx = []
    for i in range(-1, 1, 2):
        if (Mat[a+i][b] != 0):
            Neigh.append(Mat[a+i][b])
            Idx.append((a+i, b))
        if (Mat[a][b+i] != 0):
            Neigh.append(Mat[a][b+i])
            Idx.append((a, b+i))
    # Adding pivot pixel
    Neigh.append(Mat[a][b])
    Idx.append((a, b))
    return Neigh, Idx

def getNeighbours_Adj_Diag(Mat, a, b):
    Neigh = []
    Idx = []
    for i in range(a - 1, a + 2, 2):
        for j in range(b - 1, b + 2, 2):
            if (Mat[i][j] != 0):
                Neigh.append(Mat[i][j])
                Idx.append((i, j))
    # Adding pivot pixel
    Neigh.append(Mat[a][b])
    Idx.append((a, b))
    return Neigh, Idx

def getNeighbours_Adj_HorizVertDiag(Mat, a, b):
    Neigh = []
    Idx = []
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            if (Mat[i][j] != 0):
                Neigh.append(Mat[i][j])
                Idx.append((i, j))
    return Neigh, Idx

def getNeighbours(Mat, a, b, adjMode):
    """
    Non zero entires are counted as neighbours.
    Pivot pixel is also counted as neighbour
    """
    if adjMode == 1:
        Neigh, Idx = getNeighbours_Adj_Horiz(Mat, a, b)
    elif adjMode == 2:
        Neigh, Idx = getNeighbours_Adj_Vert(Mat, a, b)
    elif adjMode == 3:
        Neigh, Idx = getNeighbours_Adj_Diag(Mat, a, b)
    elif adjMode == 4:
        Neigh, Idx = getNeighbours_Adj_HorizVert(Mat, a, b)
    elif adjMode == 5:
        Neigh, Idx = getNeighbours_Adj_HorizVertDiag(Mat, a, b)
    else:
        print("Invalid adjacency mode. Use in range 1:5")
    return Neigh, Idx

def isNeighAllOnes(Neigh):
    neighAllOnes = True
    for i in range(len(Neigh)):
        if (Neigh[i] == 1):
            continue
        else:
            neighAllOnes = False
    return neighAllOnes

def MatId2B_id(Neigh):
    for i, x in enumerate(Neigh):
        Neigh[i] = x - 2
    return Neigh

def unique_num(arr):
    uniq = []
    for x in arr:
        if x not in uniq:
            uniq.append(x)
    uniq.sort()
    return uniq

def print_matrix(matrix):
    no_rows = len(matrix)
    no_cols = len(matrix[0])
    for i in range(0, no_rows):
        for j in range(0, no_cols):
            print(matrix[i][j], end=' ')
        print()
