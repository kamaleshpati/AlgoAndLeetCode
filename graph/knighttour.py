class Cell:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y


def isValid(pos: Cell,size:int,chessBoard:[[int]]) -> bool:
    if(pos.x >= 0 and pos.y >= 0 and pos.x < size and pos.y < size and chessBoard[pos.x][pos.y] == -1): 
        return True
    return False

def startTourRecurrsive(size:int,chessBoard:[[int]],start:Cell,knightMoves:[Cell],visitedBlocks:int)->bool:
    if visitedBlocks == size**2:
        return True
    
    for i in range(0,len(knightMoves)):
        newPos_x = start.x+knightMoves[i].x
        newPos_y = start.y+knightMoves[i].y

        newPos = Cell(newPos_x,newPos_y)
        if isValid(newPos,size,chessBoard):
            chessBoard[newPos_x][newPos_y] = visitedBlocks
            if startTourRecurrsive(size,chessBoard,newPos,knightMoves,visitedBlocks+1):
                return True
            chessBoard[newPos_x][newPos_y] = -1

    return False


    

def startTour(size:int)->None:
    chessBoard = [[-1 for i in range(0,size)]for j in range(0,size)]
    knightMoves = [Cell(2, 1), Cell(2, -1), Cell(-2, 1), Cell(-2, -1), Cell(1, 2), Cell(1, -2), Cell(-1, 2), Cell(-1, -2)]
    chessBoard[0][0] = 0 #startCount
    visitedBlocks = 1
    # print(chessBoard)
    if startTourRecurrsive(size,chessBoard,Cell(0,0),knightMoves,visitedBlocks):
        for i in range(size):
            for j in range(size):
                print(chessBoard[i][j],end="  ")
            print()
    else:
        print("not found solution")


size = 7
startTour(size)
