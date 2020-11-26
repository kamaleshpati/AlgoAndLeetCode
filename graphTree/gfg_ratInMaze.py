class Cell:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

def solveMazeRecurrsive(maze:[[int]],size:int,start:Cell,dest:Cell,allowedMoves:[Cell],solution:[[int]])->bool:
    if start.x == dest.x and start.y== dest.y:
        solution[start.x][start.y] = 1
        return True
    
    for i in range(len(allowedMoves)):
        new_x = start.x+allowedMoves[i].x
        new_y = start.y+allowedMoves[i].y
        if new_x >=0 and new_y >= 0 and new_x < size and new_y < size and maze[new_x][new_y] == 1:
            solution[new_x][new_y] = 1
            if solveMazeRecurrsive(maze, size, Cell(new_x,new_y),dest,allowedMoves,solution)==True:
                return True
            solution[new_x][new_y] = 0
    
    return False
            
    

def solveMaze(maze:[[int]],start:Cell,dest:Cell,size:int):
    solution = [[0 for i in range(0,size)]for j in range(0,size)]
    allowedMoves = [Cell(1, 0), Cell(0, 1)]
    if solveMazeRecurrsive(maze,size,start,dest,allowedMoves,solution):
        for i in range(size):
            for j in range(size):
                print(solution[i][j],end="  ")
            print()
    else:
        print("not found solution")



maze = [ [1, 0, 0, 0], 
         [1, 1, 0, 1], 
         [0, 1, 0, 0], 
         [1, 1, 1, 1] ] 
solveMaze(maze,Cell(0,0),Cell(3,3),4)