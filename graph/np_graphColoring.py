class Graph():
    def __init__(self, vertices:int):
        self.vertices =  vertices
        self.adj = [list() for i in range(self.vertices)]
    
    def addEdge(self,v:int,w:int)->None:
        self.adj[v].append(w)
        self.adj[w].append(v)
    
    def greedyColoring(self):
        result = [-1 for i in range(self.vertices)]
        result[0] = 0
        available = [True for i in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(len(self.adj[i])):
                if result[j] == -1:
                    available[result[j]] = False
            for color in range(self.vertices):
                if available[color]:
                    result[i] = color
                    break
            available = [True for i in range(self.vertices)]
        
        for i in range(self.vertices):
            print(color)
    
g1 = Graph(5)
g1.addEdge(0, 1) 
g1.addEdge(0, 2) 
g1.addEdge(1, 2) 
g1.addEdge(1, 3) 
g1.addEdge(2, 3) 
g1.addEdge(3, 4) 
g1.greedyColoring()
        
