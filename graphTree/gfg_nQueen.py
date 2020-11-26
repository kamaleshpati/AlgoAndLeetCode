
def isNotInCheckMate(chessBoard:[[int]],size:int,row:int,col:int)->bool:
    for i in range(col):
        if chessBoard[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if chessBoard[i][j] == 1: 
            return False
    for i, j in zip(range(row, size, -1), range(col, -1, -1)): 
        if chessBoard[i][j] == 1: 
            return False
    return True

def findNQueenSolRecursive(chessBoard:[[int]],size:int,start:int)->bool:
    if start >= size:
        return True
    for i in range(size):
        if isNotInCheckMate(chessBoard,size,i,start)==True:
            chessBoard[i][start] = 1

            if findNQueenSolRecursive(chessBoard,size,start+1) == True:
                return True

            chessBoard[i][start] = 0
    return False

def findNQueenSol(size:int)->None:
    chessBoard = [[0 for i in range(0,size)]for j in range(0,size)]
    if findNQueenSolRecursive(chessBoard,size,0):
        for i in range(size):
            for j in range(size):
                print(chessBoard[i][j],end="  ")
            print()
    else:
        print("soln does not exist")

size = 8
findNQueenSol(size)