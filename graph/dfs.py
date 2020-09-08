class Graph():
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        
        else:
            self.graph[u] = []
            self.graph[u].append(v)
    
    def dfs(self,v):
        visited = [False] *(len(self.graph))
        stack = []
        stack.append(v)
        visited[v]=True
        while stack:
            ele = stack.pop()
            print(ele)
            for i in self.graph[ele]:
                if visited[i] == False:
                    stack.append(i)
                    visited[i] = True
                    
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
g.dfs(2) 