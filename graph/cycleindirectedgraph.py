class Graph():
    def __init__(self,nodes_num):
        self.V = nodes_num
        self.graph = {}
    
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        
        else:
            self.graph[u] = []
            self.graph[u].append(v)
            
    def rec_cycle(self, node:any,visited:[],node_stack:[])-> bool:
        visited[node] = True
        node_stack[node] = True
        for value in self.graph[node]:
            if visited[value] == False and node_stack[node] == False:
                if self.rec_cycle(value, visited, node_stack):
                    return True
            else:
                return True
        
        node_stack[node] = False
        return False
            
    def is_cyclic(self)->bool:
        visited = [False] * self.V
        node_stack = [False] * self.V
        for value in range(self.V):
            if node_stack[value] == False:
                if self.rec_cycle(value,visited,node_stack):
                    return True
        return False
                



g = Graph(4)  
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.is_cyclic() == True: 
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")