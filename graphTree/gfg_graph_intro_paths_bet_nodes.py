class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = [[] for i in range(V)]

    def addEdge(self,vertex1,vertex2):
        self.graph[vertex1].append(vertex2)

    def countPaths(self, s, d):
        visited = [False] * self.V
        pathCount = [0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]

    def countPathsUtil(self, u, d, visited, pathCount):
        visited[u] = True
        if u == d:
            pathCount[0] += 1
        else:
            i = 0
            while i < len(self.graph[u]):
                if not visited[self.graph[u][i]]:
                    self.countPathsUtil(self.graph[u][i], d, visited, pathCount)
                i += 1

        visited[u] = False


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(1, 3)

    s = 2
    d = 3
    print(g.countPaths(s, d))