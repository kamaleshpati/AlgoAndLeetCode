from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,indices,vertex):
        self.graph[indices].append(vertex)

    def DFS(self,start):
        visited = [False] * len(self.graph)
        self.DFSrecursive(visited,start)

    def DFSrecursive(self, visited, start):
        visited[start] = True

        print(start,end=" ")

        for i in self.graph[start]:
            if visited[i] == False:
                visited[i] = True
                self.DFSrecursive(visited,i)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS(2)
