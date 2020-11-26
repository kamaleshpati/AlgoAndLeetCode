class Cell:
    def __init__(self, x, y, level=0, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.level = level


class Chess:
    def __init__(self, size:int, knight_pos:Cell, dest:Cell):
        self.size = size
        self.knight_pos = knight_pos
        self.dest = dest
        self.pos_q = []
        self.pos_q.append(knight_pos)
        self.pos_list = []
        self.pos_list.append(knight_pos)
        self.pos_q.append(knight_pos)
        self.knight_accessed = [Cell(2, 1), Cell(2, -1), Cell(-2, 1), Cell(-2, -1), 
                                Cell(1, 2), Cell(1, -2), Cell(-1, 2), Cell(-1, -2)]


    def check_final_pos(self, pos: Cell) -> bool:
        if pos.x == self.dest.x and pos.y == self.dest.y:
            return True
        else:
            return False
    
    def check_if_visited(self, pos: Cell) -> bool:
        visited = False
        for value in self.pos_list:
            if pos.x == value.x and pos.y == value.y:
                visited=True
                break
            
        return visited

    def check_valid_pos(self, pos: Cell) -> bool:
        if pos.x < 0 or pos.y < 0:
            return False
        elif pos.x >= self.size or pos.y >= self.size:
            return False
        else:
            return True

    

    def find_moves(self):
        if len(self.pos_q)>0:
            pos = self.pos_q.pop(0)
            for i in self.knight_accessed:
                new_pos = Cell(pos.x + i.x, pos.y + i.y, pos.level+1, pos)
                if self.check_final_pos(new_pos):
                    print(new_pos.level)
                    return
                
                elif self.check_if_visited(new_pos):
                    continue
                
                elif self.check_valid_pos(new_pos):
                    self.pos_q.append(new_pos)
                    self.pos_list.append(new_pos)
            self.find_moves()
            


if __name__ == '__main__':
    dest = Cell(30, 30)
    knight = Cell(1, 1)
    p = Chess(30, knight, dest)
    p.find_moves()
