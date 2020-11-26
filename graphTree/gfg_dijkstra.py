import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.vertices = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
    
    def minDistance(self, dist,sptSet): 
        min = sys.maxsize 
        for v in range(self.vertices): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v
        return min_index 
    
    def setGraph(self,src: int)->None:
        dist = [sys.maxsize] * self.vertices 
        dist[src] = 0
        sptSet = [False] * self.vertices 
        for i in range(self.vertices):
            u = self.minDistance(dist,sptSet)
            sptSet[u] = True
            for v in range(self.vertices): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v]
        
        print(dist)
            
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
g.setGraph(0)
