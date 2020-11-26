
class Graph():
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        
        else:
            self.graph[u] = []
            self.graph[u].append(v)
    
    def bfs(self,v):
        visited = [False] *(len(self.graph))
        queue = []
        queue.append(v)
        visited[v]=True
        while queue:
            ele = queue.pop(0)
            print(ele)
            for i in self.graph[ele]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        
        
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.bfs(2) 

    